import curses as c
from random import randint

from local_output import output, item

from local_translator import translate
from local_input_key import *
from local_enemies_class import enemies_class_is_shoted
from local_equip import get_equip_values


def sort(p): p["BP"].sort(reverse=True, key = lambda key: key["item"][::-1])

def update_BP_mask(p): # is local_terrain too -PR-
    global BP_mask
    BP_mask = []
    for i in p["BP"]:
        if i["grouping"]:
            BP_mask.append(i["item"])

def print_menager(w, m, p, cm, bc): # m is'n needed, but for formality it is -PR-
    c.init_pair(1, 231, 16)
    c.init_pair(2, 46, 16)
    c.init_pair(3, 5, 16)
    c.init_pair(4, 136, 16)
    c.init_pair(5, 245, 16)#148 :) -PR-
    w.clear()
    w.addstr(3, 0, "Mana: " + str(p["mana"]) + "/" + str(p["maxmana"]), c.color_pair(4))
    w.addstr(0, 0, translate("FOOD")+":  "+(translate("STARVING") if p["starving"] else str(p["fullness"])), c.color_pair(4))
    w.addstr(1, 0, translate("LIGHT")+": "+(translate("NO LIGHT") if not p["torch"] else str(p["torchtime"])), c.color_pair(4))
    w.addstr(11, 0,"Equipted:", c.color_pair(4))
    w.addstr(12, 2, item(p["e_attack"], 9, p["strength"]), c.color_pair(5))
    w.addstr(13, 2, item(p["e_hand"], 9, p["strength"]), c.color_pair(5))
    w.addstr(14, 2, item(p["e_armor"], 9, p["strength"]), c.color_pair(5))
    w.addstr(16, 0, "Backpack:", c.color_pair(4))
    w.refresh()
    t1 = ''
    for i in range(len(p["spells"])):
        w.addstr(4+i, 2, str(i+1)+": "+str(p["spells"][i][0]), c.color_pair(cm))
    for i in range(6):
        w.addstr(17+i, 2, str(i+1)+": "+item(p["BP"], i, p["strength"]), c.color_pair(bc))
    w.addstr(23, 0, "What do you want to do?:", c.color_pair(4))
    
def mana_menager(w, m, p):
    print_menager(w, m, p, 2, 5)
    it = get_in(w)
    return[translate("YOU CAN'T CAST A SPELL!"), False]
    #try:
    #    it = int(it)-1
    #    if it >= len(p["BP"]) or it < 0:
    #        return["", False]
    #except:
    #    return["", False]
    #t = p["BP"].pop(it)
    #return[translate("YOU CAST A SPELL!"), True]

def item_menager(w, m, p):
    print_menager(w, m, p, 5, 2)
    it = get_in(w)
    try:
        it = int(it)-1
        if it >= len(p["BP"]) or it < 0:
            return[p["echo"], False]
    except:
        return[p["echo"], False]
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
            p["fullness"] += 400
            if p["fullness"] > 500:
                p["fullness"] = 500
            p["starving"] = False
            if t["values"][0] <= 0:
                p["BP"].pop(it)
                update_BP_mask(p)
            return[translate("YOU ATE A") + " " + translate("BREAD"), True]
        case "CORPSE":
            t["values"][0] -= 1
            p["fullness"] += 200
            if p["fullness"] > 500:
                p["fullness"] = 500
            p["starving"] = False
            if t["values"][0] <= 0:
                p["BP"].pop(it)
                update_BP_mask(p)
            return[translate("YOU ATE A") + " " + translate("CORPSE"), True]
        case "POTION":
            t["values"][0] -= 1
            p["hp"] = p["maxhp"]
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
            return[translate("YOU TAKE A") + " " + translate(t["item"][:-2]), True]
    return[translate("WRONG SLOT!"), False]

def drop_menager(w, m, p):
    print_menager(w, m, p, 5, 3)
    it = get_in(w)
    try:
        it = int(it)-1
        if it >= len(p["BP"]) or it < 0:
            return[p["echo"], False]
    except:
        return[p["echo"], False]
    t = p["BP"].pop(it)
    return[translate("YOU FROWED IT AWAY"), True]

def shot_menager(w, m, p):
    w.clear()
    output(w, m, p)
    w.addstr(23, 0, translate("WHERE DO YOU WANT TO SHOT?"))
    it = get_in(w)
    dy, dx, t1 = player_move(it)
    if (dy != 0 or dx != 0) and p["arrows_id"] != -1:
        enemies_class_is_shoted(m, p, [dy, dx], p["bow"])
        get_equip_values(p)
        return[p["echo"], True]
    if p["arrows_id"] == -1:
        return[translate("YOU DON'T HAVE ARROWS!"), False]
    return[translate("YOU CAN'T SHOT THERE!"), False]

def pomoc(w, m, p): #not beautyful, but done -PR-
    w.clear()
    w.addstr(0, 0, "Tiles:", c.color_pair(4))
    w.addstr(0, 58, "Version = curses_0.0.E", c.color_pair(1))
    w.addstr(1, 2, "@ - you", c.color_pair(5))
    w.addstr(2, 2, "# - wall", c.color_pair(5))
    w.addstr(3, 2, "+ - closed door", c.color_pair(5))
    w.addstr(4, 2, ", - open door", c.color_pair(5))
    w.addstr(5, 2, ". - light tile", c.color_pair(5))
    w.addstr(6, 2, '= - closed tile (You have to kill a Boss "B")', c.color_pair(5))
    w.addstr(7, 2, "> - stairs down", c.color_pair(5))
    w.addstr(8, 2, "< - stairs up", c.color_pair(5))
    w.addstr(9, 2, "] - weapon", c.color_pair(5))
    w.addstr(10, 2, "} - ranged weapon", c.color_pair(5))
    w.addstr(11, 2, ") - armor", c.color_pair(5))
    w.addstr(12, 2, "- - arrows", c.color_pair(5))
    w.addstr(13, 2, "~ - torch", c.color_pair(5))
    w.addstr(14, 2, "? - mixture", c.color_pair(5))
    
    w.addstr(16, 0, "Movement:", c.color_pair(4))
    w.addstr(17, 4, "7 8 9", c.color_pair(1))
    w.addstr(18, 4, "4 5 6   5 - wait or take item from the flor", c.color_pair(1))
    w.addstr(19, 4, "1 2 3", c.color_pair(1))
    w.addstr(20, 2, "- - use (mana)    + - use (backpack)    / - sort (no turns used)", c.color_pair(5))
    w.addstr(21, 2, "0 - shot          , - drop (backpack)", c.color_pair(5))
    w.addstr(23, 4, "Don't forget about NumLock!", c.color_pair(2))
    #w.addstr(22, 4, "Not working? NumLock!", c.color_pair(4))
    #w.addstr(23, 0, "Press enter to continue", c.color_pair(4))
    get_in(w)

# def item_menager_keyin(m, p, key):

def keyin(w, m, p, pos, key):
    match key:
        case "-":
             return mana_menager(w, m, p)
        case "+":
             return item_menager(w, m, p)
        case ",":
             return drop_menager(w, m, p)
        case "0":
             return shot_menager(w, m, p)
        case ">":
            if m["r"][pos[0]][pos[1]][0] == ">":
                return ["#D", False]
            return [translate("YOU CAN'T GO DOWN HERE"), False]
        case "<":
            if m["r"][pos[0]][pos[1]][0] == "<":
                return ["#U", False]
            return [translate("YOU CAN'T GO UP HERE"), False]
        case "/":
            sort(p)
            return [p["echo"], False]
        case "?":
            pomoc(w, m, p)
            return [p["echo"], False]
        case _:
           # move a player? (but in where!?),
           #		echo, moved?
            return ["? - for help", False]
