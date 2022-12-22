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

def f_gold(w, m, p, npos, stay):
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

def f_door(w, m, p, npos, stay):
    npy, npx = npos[0], npos[1]
    m["r"][npy][npx] = ","
    m["v"][npy][npx] = ","
    echo = "Otworzyłeś drzwi"
    return[False, echo, True]

def f_block(w, m, p, npos, stay):
    npy, npx = npos[0], npos[1]
    m["r"][npy][npx] = " "
    m["v"][npy][npx] = " "
    echo = translate("YOU DESTROYED WEEK WALL")
    return[False, echo, True]

def f_arrows(w, m, p, npos, stay):
    npy, npx = npos
    i = int(m["r"][npy][npx][1:4])
    i = item_class_get(i)
    if stay:
        if len(p["BP"]) < 6 or i["item"] in BP_mask:
            p["BP"].append(i)
            merge(p)
            update_BP_mask(p)
            get_equip_values(p)
            echo = translate("YOU TAKE")+" "+str(i["values"][0])+"x "+translate("ARROWS", i["values"][0])
            m["r"][npy][npx] = m["r"][npy][npx][4:]
            m["v"][npy][npx] = m["r"][npy][npx]
        else:
            echo = translate("YOUR'S BACKPACK IS FULL!")
            return[False, echo, False]
    else:
        echo = translate("HERE ARE")+" "+str(i["values"][0])+"x "+translate("ARROWS", 0 if i["values"][0] == 1 else i["values"][0])
    return[True, echo, True]

def f_items(w, m, p, npos, stay):
    npy, npx = npos
    i = int(m["r"][npy][npx][1:4])
    i = item_class_get(i)
    if stay:
        if len(p["BP"]) < 6 or i["item"] in BP_mask:
            p["BP"].append(i)
            merge(p)
            update_BP_mask(p)
            get_equip_values(p)
            echo = translate("YOU TAKE")+" "+str(i["values"][0])+"x "+(translate(i["values"][-1], i["values"][0]) if i["values"][0] > 1 else translate(i["item"], 1))
            m["r"][npy][npx] = m["r"][npy][npx][4:]
            m["v"][npy][npx] = m["r"][npy][npx]
        else:
            echo = translate("YOUR'S BACKPACK IS FULL!")
            return[False, echo, False]
    else:
        echo = translate("HERE ARE" if i["values"][0] > 1 else "HERE IS")+" "+str(i["values"][0])+"x "+(translate(i["values"][-1], i["values"][0]) if i["values"][0] > 1 else translate(i["item"], 1))
    return[True, echo, True]

def f_weapons(w, m, p, npos, stay):
    npy, npx = npos
    i = int(m["r"][npy][npx][1:4])
    i = item_class_get(i)
    if stay:
        if len(p["BP"]) < 6:
            p["BP"].append(i)
            update_BP_mask(p)
            get_equip_values(p)
            echo = translate("YOU TAKE")+" "+translate(str(i["item"][:-2])+" "+("["+str(i["values"][0])+"]" if i["ident"] else "[?]"))
            m["r"][npy][npx] = m["r"][npy][npx][4:]
            m["v"][npy][npx] = m["r"][npy][npx]
        else:
            echo = translate("YOUR'S BACKPACK IS FULL!")
            return[False, echo, False]
    else:
        echo = translate("HERE IS")+" "+translate(str(i["item"][:-2])+" "+("["+str(i["values"][0])+"]" if i["ident"] else "[?]"))
    return[True, echo, True]

def f_torch(w, m, p, npos, stay):
    npy, npx = npos
    i = int(m["r"][npy][npx][1:4])
    i = item_class_get(i)
    if stay:
        if len(p["BP"]) < 6 or i["item"] in BP_mask:
            p["BP"].append(i)
            merge(p)
            update_BP_mask(p)
            get_equip_values(p)
            echo = translate("YOU TAKE")+" "+translate("TORCH")
            m["r"][npy][npx] = m["r"][npy][npx][4:]
            m["v"][npy][npx] = m["r"][npy][npx]
        else:
            echo = translate("YOUR'S BACKPACK IS FULL!")
            return[False, echo, False]
    else:
        echo = translate("HERE IS")+" "+translate("TORCH", 1)
    return[True, echo, True]

def terrain(w, m, p, npos, stay):
    # ramp, vmap, p, gold, baner, backpack, echo, moved
    match m["r"][npos[0]][npos[1]][0]:
        case "$":
            return f_gold(w, m, p, npos, stay)
        case "-":
            return f_items(w, m, p, npos, stay)
        case "*":
            return f_items(w, m, p, npos, stay)
        case "?":
            return f_items(w, m, p, npos, stay)
        # # case "!":
        # #     return f_orantium(rmap, vmap, p, np, gold, baner, backpack, direction)
        case "+":
            return f_door(w, m, p, npos, stay)
        case ":":
            return f_block(w, m, p, npos, stay)
        case "]":
            return f_weapons(w, m, p, npos, stay)
        case "}":
            return f_weapons(w, m, p, npos, stay)
        case ")":
            return f_weapons(w, m, p, npos, stay)
        case "~":
            return f_torch(w, m, p, npos, stay)
        # case "?":
        #     return f_potion(rmap, vmap, p, np, gold, baner, backpack, direction)
        case "=":
            return [False, translate("THIS TILE IS CLOSED"), False]
        case ".":
            return [True, "", True]
        case ",":
            return [True, "", True]
        case " ":
            return [True, "", True]
        case "^":
            return [False, translate("HERE IS A VERY STEP HILL, YOU CAN'T GET HERE"), False]
        case "#":
            return [False, translate("HERE IS A WALL"), False]
        case ">":
            return [True, "Tu są schody na dół", True]
        case "<":
            return [True, "Tu są schody do góry", True]
        case _:
        # move a player?, echo, moved?
            it = int(m["r"][npos[0]][npos[1]][1:4])
            enemies_class_is_attacked(m, p, it, p["attack"])
            return [False, p["echo"], True]
