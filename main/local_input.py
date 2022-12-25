from random import randint

from local_output import output, item

from local_translator import translate
from local_input_key import *
from local_enemies_class import enemies_class_is_shoted
from local_equip import get_equip_values

def update_BP_mask(p): # is local_terrain
    global BP_mask
    BP_mask = []
    for i in p["BP"]:
        if i["grouping"]:
            BP_mask.append(i["item"])

def item_menager(m, p):
    t1 = "\n       Equipted:\n   " + item(p["e_attack"], 9, p["strength"]) + "\n   " + item(p["e_hand"], 9, p["strength"]) + "\n   " + item(p["e_armor"], 9, p["strength"]) + "\n\n       Backpack:\n"
    for i in range(6):
        t1 += str(i+1)+": "+item(p["BP"], i, p["strength"]) + "\n"
    print("\n\n\n\n\n\n\n\n\n\n\n"+translate("FOOD")+":  "+(translate("STARVING") if p["starving"] else str(p["fullness"]))+"\n"+translate("LIGHT")+": "+(translate("NO LIGHT") if not p["torch"] else str(p["torchtime"]))+t1, end="\nWhat do you want to do?:")
    it = get_in()
    try:
        it = int(it)-1
        if it > len(p["BP"]) or it < 0:
            return["", False]
    except:
        return["", False]
    t = p["BP"][it]
    match t["item"]:
        case "TORCH":
            t["values"][0] -= 1
            p["torchtime"] = 300
            p["torch"] = True
            if t["values"][0] <= 0:
                p["BP"].pop(it)
                update_BP_mask(p)
            return[translate("YOU LIGHT A") + " " + translate("TORCH") + ", " + translate("AND IT WILL GIVE YOU LIGHT FOR") + " " + str(350) + " " + translate("TURNS"), True]
        case "BREAD":
            t["values"][0] -= 1
            p["fullness"] = 400
            p["starving"] = False
            if t["values"][0] <= 0:
                p["BP"].pop(it)
                update_BP_mask(p)
            return[translate("YOU ATE A") + " " + translate("BREAD"), True]
        case "POTION":
            t["values"][0] -= 1
            match randint(0,1):
                case 0:
                    p["hp"] = p["maxhp"]
                case _:
                    p["strength"] += 1
            if t["values"][0] <= 0:
                p["BP"].pop(it)
                update_BP_mask(p)
            return[translate("YOU DRANK A") + " " + translate("POTION"), True]
        case _:
            no = True
            match t["type"]:
                case "]":
                    if p["BP"][it]["values"][2] <= p["strength"]:
                        t = p["BP"].pop(it)
                        p["BP"].append(p["e_attack"])
                        p["e_attack"] = t
                        no = False
                case "}":
                    if p["BP"][it]["values"][2] <= p["strength"]:
                        t = p["BP"].pop(it)
                        p["BP"].append(p["e_hand"])
                        p["e_hand"] = t
                        no = False
                case ")":
                    if p["BP"][it]["values"][2] <= p["strength"]:
                        t = p["BP"].pop(it)
                        p["BP"].append(p["e_armor"])
                        p["e_armor"] = t
                        no = False
            if no:
                return[translate("YOU CAN'T USE THAT"), False]
            get_equip_values(p)
            return[translate("YOU TAKE A") + " " + translate(t["item"]), True]
    return[translate("WRONG SLOT!"), False]

def drop_menager(w, m, p):
    t1 = "\n       Equipted:\n   " + item(p["e_attack"], 9, p["strength"]) + "\n   " + item(p["e_hand"], 9, p["strength"]) + "\n   " + item(p["e_armor"], 9, p["strength"]) + "\n\n       Backpack:\n"
    for i in range(6):
        t1 += str(i+1)+": "+item(p["BP"], i, p["strength"]) + "\n"
    print("\n\n\n\n\n\n\n\n\n\n\n"+translate("FOOD")+":  "+(translate("STARVING") if p["starving"] else str(p["fullness"]))+"\n"+translate("LIGHT")+": "+(translate("NO LIGHT") if not p["torch"] else str(p["torchtime"]))+t1, end="\nWhat do you want to do?:")
    it = get_in()
    try:
        it = int(it)-1
        if it > len(p["BP"]) or it < 0:
            return["", False]
    except:
        return["", False]
    t = p["BP"][it]
    return[translate("YOU FROWED IT AWAY"), True]

def shot_menager(m, p):
    print(output(m, p) + translate("WHERE DO YOU WANT TO SHOT?"))
    it = get_in()
    dy, dx, t1 = player_move(it)
    if (dy != 0 or dx != 0) and p["arrows_id"] != -1:
        enemies_class_is_shoted(m, p, [dy, dx], p["bow"])
        get_equip_values(p)
        return[p["echo"], True]
    if p["arrows_id"] == -1:
        return[translate("YOU DON'T HAVE ARROWS!"), False]
    return[translate("YOU CAN'T SHOT THERE!"), False]

# def item_menager_keyin(m, p, key):
def keyin(m, p, pos, key):
    match key:
        case "-":
             return item_menager(m, p)
        case "0":
             return shot_menager(m, p)
        case "d":
             return drop_menager(m, p)
        case ">":
            if m["r"][pos[0]][pos[1]][0] == ">":
                return ["#D", False]
            return [translate("YOU CAN'T GO DOWN HERE"), False]
        case "<":
            if m["r"][pos[0]][pos[1]][0] == "<":
                return ["#U", False]
            return [translate("YOU CAN'T GO UP HERE"), False]
        case _:
           # move a player? (but in where!?),
           #		echo, moved?
            return ["? - for help", False]
