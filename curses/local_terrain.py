from local_translator import translate
from local_item_class import item_class_get
from local_enemies_class import enemies_class_is_attacked
from local_equip import get_equip_values, update_BP_mask, merge
from local_output import item # for f_weapons -PR-
from local_npc import npc

def type_gold(i):
    if i < 11:
        return "WORTH COPPER"
    if i < 26:
        return "WORTH SILVER"
    return "WORTH GOLD"

def f_gold(m, p, npos, stay):
    npy, npx = npos
    i = int(m["r"][npy][npx][1:4])
    #i = item_class_get(i)
    if stay:
        m["r"][npy][npx] = m["r"][npy][npx][4:]
        m["v"][npy][npx] = m["r"][npy][npx]
        p["gold"] += i
        echo = translate("YOU TAKE")+" "+str(i)+" "+translate(type_gold(i), i)
    else:
        echo = translate("HERE IS")+" "+str(i)+" "+translate(type_gold(i), i)
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
    if m["v"][npy][npx] == "":
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
        echo = translate("HERE IS")+" "+translate(item(i, 9, p))
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
        case "!":
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
            return npc(w, c, m, p, m["r"][npos[0]][npos[1]][1:], stay)
        case _:
        # move a player?, echo, moved?
            it = int(m["r"][npos[0]][npos[1]][1:4])
            enemies_class_is_attacked(m, p, it, p["attack"])
            return [False, p["echo"], True]
