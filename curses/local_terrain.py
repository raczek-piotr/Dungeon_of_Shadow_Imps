from local_translator import translate
from local_item_class import item_class_get
from local_enemies_class import enemies_class_is_attacked
from local_equip import get_equip_values
#from local_items import *
BP_mask = []


def update_BP_mask(p): # is local_input
    global BP_mask
    BP_mask = []
    for i in p["BP"]:
        if i["grouping"]:
            BP_mask.append(i["item"])

def merge(p): # polacz (PL) -PR-
    i = 0
    while i < len(p["BP"]):
        j = 1
        while j < len(p["BP"]):
            if i == j:
                j += 1
                continue
            if p["BP"][i]["grouping"] and p["BP"][i]["item"] + " " + p["BP"][i]["type"] == p["BP"][j]["item"] + " " + p["BP"][j]["type"]:
                t1 = p["BP"].pop(j)
                p["BP"][i]["values"][0] += t1["values"][0]
            else:
                j += 1
        i += 1

def f_gold(m, p, npos, stay):
    npy, npx = npos
    i = int(m["r"][npy][npx][1:4])
    i = item_class_get(i)
    if stay:
        m["r"][npy][npx] = m["r"][npy][npx][4:]
        m["v"][npy][npx] = m["r"][npy][npx]
        p["gold"] += i
        echo = translate("YOU TAKE")+" "+str(i)+" "+translate("GOLD", i)
    else:
        echo = translate("HERE IS")+" "+str(i)+" "+translate("GOLD", i)
    return[True, echo, True]

def f_door(m, p, npos, stay):
    npy, npx = npos[0], npos[1]
    m["r"][npy][npx] = ","
    m["v"][npy][npx] = ","
    echo = "Otworzyłeś drzwi"
    return[False, echo, True]

def f_block(m, p, npos, stay):
    npy, npx = npos[0], npos[1]
    m["r"][npy][npx] = m["r"][npy][npx][1:]
    m["v"][npy][npx] = m["v"][npy][npx][1:]
    if m["r"][npy][npx] == "":
        m["v"][npy][npx] = " "
    echo = translate("YOU DESTROYED WEEK WALL")
    return[False, echo, True]

def f_items(m, p, npos, stay):
    npy, npx = npos
    i = int(m["r"][npy][npx][1:4])
    i = item_class_get(i)
    if stay:
        if len(p["BP"]) < 6 or i["item"] in BP_mask:
            p["BP"].append(i)
            merge(p)
            update_BP_mask(p)
            get_equip_values(p)
            echo = translate("YOU TAKE")+" "+str(i["values"][0])+"x "+(translate(i["values"][-1], i["values"][0]) if i["values"][0] > 1 else translate(i["item"], 0))
            m["r"][npy][npx] = m["r"][npy][npx][4:]
            m["v"][npy][npx] = m["r"][npy][npx]
        else:
            echo = translate("YOUR'S BACKPACK IS FULL!")
            return[False, echo, False]
    else:
        echo = translate("HERE ARE" if i["values"][0] > 1 else "HERE IS")+" "+str(i["values"][0])+"x "+(translate(i["values"][-1], i["values"][0]) if i["values"][0] > 1 else translate(i["item"], 1))
    return[True, echo, True]

def f_weapons(m, p, npos, stay):
    npy, npx = npos
    i = int(m["r"][npy][npx][1:4])
    i = item_class_get(i)
    if stay:
        if len(p["BP"]) < 6:
            p["BP"].append(i)
            update_BP_mask(p)
            get_equip_values(p)
            echo = translate("YOU TAKE")+" "+translate(str(i["item"][:-2])+" "+(i["item"][-1]+str(i["values"][0])+"x"+str(i["values"][4])+i["type"]))
            m["r"][npy][npx] = m["r"][npy][npx][4:]
            m["v"][npy][npx] = m["r"][npy][npx]
        else:
            echo = translate("YOUR'S BACKPACK IS FULL!")
            return[False, echo, False]
    else:
        echo = translate("HERE IS")+" "+translate(str(i["item"][:-2])+" "+(i["item"][-1]+str(i["values"][0])+"x"+str(i["values"][4])+i["type"]))
    return[True, echo, True]

def f_trader(w, c, m, p, npos, stay):
    from local_output import item
    q = ""
    ilist = [{"item": "SHOVEL [", "type": "]", "values": [3, 50, [4,2], 1, 1], "cost": 15, "grouping": False},
             {"item": "SICKLE [", "type": "]", "values": [2, 70, [2,4], 1, 1], "cost": 14, "grouping": False},
             {"item": "BREAD", "type": "", "values": [1, "BREADS"], "cost": 7, "grouping": True},
             {"item": "TORCH", "type": "", "values": [1, "TORCHES"], "cost": 5, "grouping": True}]
    while True:
        if q in {"0","1","2","3"}:
            i = ilist[int(q)].copy()
            if len(p["BP"]) < 6 and p["gold"] >= i["cost"]:
                p["gold"] -= i["cost"]
                p["BP"].append(i)
                #update_BP_mask(p)
                get_equip_values(p)
                echo = translate("YOU BUY")+" "+translate(i["item"][:-2] if i["item"][-1] in {"[","{","("} else i["item"])
                return[False, echo, True]
            else:
                if len(p["BP"]) < 6:
                    echo = translate("YOU DON'T HAVE ENOUGH MONEY!")
                else:
                    echo = translate("YOUR'S BACKPACK IS FULL!")
                return[False, echo, False]
        elif q in {"PADENTER","\n", ","}:
            return[False, p["echo"], False]
        w.clear()
        w.addstr(0, 37, "Trader:", c.color_pair(5))
        w.addstr(1, 2, "Your gold: "+str(p["gold"]), c.color_pair(1))
        w.addstr(2, 0, "Items:", c.color_pair(5))
        for i in range(len(ilist)):
            w.addstr(i+3, 2, str(i)+": "+item(ilist[i], 9, p), c.color_pair(1))
            t = str(ilist[i]["cost"])
            w.addstr(i+3, 68, "COST:", c.color_pair(1))
            w.addstr(i+3, 78-len(t), t, c.color_pair(1))
        w.addstr(23, 62, "Esc: ',' or Enter", c.color_pair(5))
        q = w.getkey()
    return[True, echo, True]

def terrain(w, c, m, p, npos, stay):
    # ramp, vmap, p, gold, baner, backpack, echo, moved
    match m["r"][npos[0]][npos[1]][0]:
        case "$":
            return f_gold(m, p, npos, stay)
        case "-":
            return f_items(m, p, npos, stay)
        case "*":
            return f_items(m, p, npos, stay)
        case "?":
            return f_items(m, p, npos, stay)
        case "~":
            return f_items(m, p, npos, stay)
        # # case "!":
        # #     return f_orantium(rmap, vmap, p, np, gold, baner, backpack, direction)
        case "+":
            return f_door(m, p, npos, stay)
        case ":":
            return f_block(m, p, npos, stay)
        case "]":
            return f_weapons(m, p, npos, stay)
        case "}":
            return f_weapons(m, p, npos, stay)
        case ")":
            return f_weapons(m, p, npos, stay)
        # case "?":
        #     return f_potion(rmap, vmap, p, np, gold, baner, backpack, direction)
        case "=":
            return [False, translate("THIS TILE IS CLOSED"), False]
        case ".":
            return [True, "", True]
        case ",":
            return [True, "", True]
        case " ":
            if m["r"][npos[0]][npos[1]] == "  ":
                if p["torch"]:
                    return [False, translate("HERE IS A DIVIDE!"), False]
                return [True, "#D!", True]
            return [True, "", True]
        case "^":
            return [False, translate("HERE IS A VERY STEP HILL, YOU CAN'T GET HERE"), False]
        case "#":
            return [False, translate("HERE IS A WALL"), False]
        case ">":
            return [True, translate("HERE ARE STAIRS DOWN"), True]
        case "<":
            return [True, translate("HERE ARE STAIRS UP"), True]
        case "@":
            return f_trader(w, c, m, p, npos, stay)
        case _:
        # move a player?, echo, moved?
            it = int(m["r"][npos[0]][npos[1]][1:4])
            enemies_class_is_attacked(m, p, it, p["attack"])
            return [False, p["echo"], True]
