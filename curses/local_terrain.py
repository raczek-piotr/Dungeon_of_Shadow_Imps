from random import randint

from local_translator import translate
from local_item_class import get_item
from local_enemies_class import enemies_class_is_attacked
from local_equip import get_equip_values, merge
from local_output import item # for f_weapons -PR-
from local_npc import npc

from local_output import item

def type_gold(i):
    if i < 11:
        return "WORTH COPPER"
    if i < 26:
        return "WORTH SILVER"
    return "WORTH GOLD"

def f_gold(m, p, npos, stay):
    npy, npx = npos
    i = int(m["r"][npy][npx][1:4])
    #i = get_item(i)
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
    m["r"][npy][npx] = m["r"][npy][npx][1:]
    m["v"][npy][npx] = m["v"][npy][npx][1:]
    if m["v"][npy][npx] == "":
        m["v"][npy][npx] = " "
    echo = translate("YOU OPEN A DOOR")
    return[False, echo, True]

def f_block(m, p, npos, stay):
    npy, npx = npos[0], npos[1]
    m["r"][npy][npx] = m["r"][npy][npx][1:]
    m["v"][npy][npx] = m["v"][npy][npx][1:]
    if m["v"][npy][npx] == "":
        m["v"][npy][npx] = " "
    echo = translate("WEEK WALL FALLED DOWN")
    return[False, echo, True]

def in_BP(BP, item): #copy is in local_npc.py
    for i in BP:
        if i[0] == item[0]:
            return True
    return False

def f_items(m, p, npos, stay):
    npy, npx = npos
    i = int(m["r"][npy][npx][1:4])
    i = get_item(i)
    if stay:
        if len(p["BP"]) < 6:# or i[1] == "-" and in_BP(p["BP"], i):
            p["BP"].append(i)
            merge(p)
            get_equip_values(p)
            m["r"][npy][npx] = m["r"][npy][npx][4:]
            m["v"][npy][npx] = m["r"][npy][npx]
            #if item[1] == "-":
            echo = translate("YOU TAKE")+" '"+translate(item(i, 9, p))+"'"
        else:
            echo = translate("YOUR BACKPACK IS FULL!")
            return[False, echo, False]
    else:
        echo = translate("HERE IS")+" '"+translate(item(i, 9, p))+"'"
    return[True, echo, True]

def f_some_items(m, p, npos, stay): #only "-" -PR-
    npy, npx = npos
    i = int(m["r"][npy][npx][1:4])
    i = get_item(i)
    if stay:
        if len(p["BP"]) < 6 or i[1] == "-" and in_BP(p["BP"], i):
            i[2] = randint(1,9)
            p["BP"].append(i)
            merge(p)
            get_equip_values(p)
            m["r"][npy][npx] = m["r"][npy][npx][4:]
            m["v"][npy][npx] = m["r"][npy][npx]
            #if item[1] == "-":
            echo = translate("YOU TAKE")+" '"+translate(item(i))+"'"
        else:
            echo = translate("YOUR BACKPACK IS FULL!")
            return[False, echo, False]
    else:
        echo = translate("HERE ARE A FEW")+" '"+translate(item(i,10))+"'"
    return[True, echo, True]

def terrain(w, c, m, p, npos, stay):
    # ramp, vmap, p, gold, baner, backpack, echo, moved
    match m["r"][npos[0]][npos[1]][0]:
        case "-":
            return f_some_items(m, p, npos, stay)
        case "$":
            return f_gold(m, p, npos, stay)
        case "*":
            return f_items(m, p, npos, stay)
        case "?":
            return f_items(m, p, npos, stay)
        case "!":
            return f_items(m, p, npos, stay)
        case "~":
            return f_items(m, p, npos, stay)
        case "+":
            return f_door(m, p, npos, stay)
        case ":":
            return f_block(m, p, npos, stay)
        case "]":
            return f_items(m, p, npos, stay)
        case "}":
            return f_items(m, p, npos, stay)
        case ")":
            return f_items(m, p, npos, stay)
        case "=":
            return [True, translate("SHALLOW WATER"), True]
        case "%":
            return [True, translate("NATURE AROUND YOU"), True]
        case "&":
            return [False, translate("HERE IS LAVA!"), False]
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
