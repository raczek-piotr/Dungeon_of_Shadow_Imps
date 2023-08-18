#import curses as c
from random import randint

from local_output import output, item

from local_translator import translate
from local_input_key import *
from local_enemies_class import enemies_class_is_shoted
from local_equip import get_equip_values #, merge # not needed -PR-


def sort(p): p["BP"].sort(reverse=True, key = lambda key: key[1]+key[0][0])

def print_menager(w, c, m, p, cm, bc): # m is'n needed, but for formality it is -PR-
    w.clear()
    w.addstr(3, 0, "str|dex " + str(p["strength"]) + "|" + str(p["dexterity"]), c.color_pair(4))
    w.addstr(0, 0, translate("FOOD")+":  "+(translate("STARVING") if p["starving"] else str(p["fullness"])), c.color_pair(4))
    w.addstr(1, 0, translate("LIGHT")+": "+(translate("NO LIGHT") if not p["torch"] else str(p["torchtime"])), c.color_pair(4))
    w.addstr(10, 0,"Equipted:", c.color_pair(4))
    w.addstr(11, 2, item(p["e_attack"], 9, p), c.color_pair(5))
    w.addstr(12, 2, item(p["e_hand"], 9, p), c.color_pair(5))
    w.addstr(13, 2, item(p["e_armor"], 9, p), c.color_pair(5))
    w.addstr(14, 2, item(p["e_shield"], 9, p), c.color_pair(5))
    w.addstr(16, 0, "Backpack:", c.color_pair(4))
    w.refresh() # ? -PR-
    t1 = ''
    for i in range(6):
        w.addstr(17+i, 2, str(i+1)+": "+item(p["BP"], i, p), c.color_pair(bc))
    w.addstr(23, 0, "What do you want to do?:", c.color_pair(4))

def item_menager(w, c, m, p):
    print_menager(w, c, m, p, 5, 2)
    it = get_in(w)
    try:
        it = int(it)-1
        if it >= len(p["BP"]) or it < 0:
            return[p["echo"], False]
    except:
        return[p["echo"], False]
    t = p["BP"][it]
    if t[1] in {"]","}",")"}:
        p["BP"][it], p[t[0][1]] = p[t[0][1]], p["BP"][it]
    else:
        match t[0][1]:
            case 0: # food
                p["fullness"] += t[0][2]
                if p["fullness"] > p["maxeat"]:
                    p["fullness"] = p["maxeat"]
                p["starving"] = False
                p["BP"].pop(it)
                return[translate("YOU ATE A") + " " + translate(t[0][0]), True]
            case 1: # light
                p["torchtime"] = t[0][2]
                p["torch"] = True
                p["BP"].pop(it)
                return[translate("YOU LIGHT A") + " " + translate(t[0][0]), True]
            case 2: # scrolls
                if t[0][2] == 0:
                    pass
                elif t[0][2] == 1:
                    mx, my = m["sx"]-2, m["sy"]-2
                    q = "#"
                    while q[0] not in {".",","," ","]","}",")","$","~","-","*","!","?","<",">"} and q != "  ":
                        x, y = randint(1, mx), randint(1, my)
                        q = m["r"][y][x]
                    t["values"][0] -= 1
                    p["x"], p["y"] = x, y
                    p["BP"].pop(it)
                    return[translate("YOU READ A") + " " + translate("SCROLL OF TELEPORT"), True]
                elif t[0][2] == 2:
                    p["blessing"] += 50
                    p["BP"].pop(it)
                    return[translate("YOU READ A") + " " + translate("SCROLL OF BLESSING"), True]
                else:
                    p["hp"] -= p["maxhp"]//2
                    p["BP"].pop(it)
                    return[translate("YOU READ A") + " " + translate("SCROLL OF DARK ENEGY") + " " + translate("DARK ENERGY HITS YOU"), True]
            case 3: # potions
                if t[0][2] == 0:
                    p["hp"] = p["maxhp"]
                    p["BP"].pop(it)
                    return[translate("YOU DRANK") + " " + translate("POTION OF HEALING"), True]
                elif t[0][2] == 1:
                    p["blessing"] += 10
                    p["fury"] += 10
                    p["hp"] += p["maxhp"]//2
                    if p["hp"] > p["maxhp"]:
                        p["hp"] = p["maxhp"]
                    p["BP"].pop(it)
                    return[translate("YOU DRANK") + " " + translate("POTION OF ENHANCEMENT"), True]
                elif t[0][2] == 2:
                    p["fury"] += 50
                    p["BP"].pop(it)
                    return[translate("YOU DRANK") + " " + translate("POTION OF FURY"), True]
                else:
                    p["hp"] -= p["maxhp"]//2
                    p["BP"].pop(it)
                    return[translate("YOU DRANK") + " " + translate("POTION OF POISON"), True]
                    
        return[translate("YOU CAN'T USE THAT"), False]

    get_equip_values(p)
    return[translate("YOU TAKE A") + " " + translate(t[0][0]), True]
    return[translate("WRONG SLOT!"), False]

def drop_menager(w, c, m, p):
    print_menager(w, c, m, p, 5, 3)
    it = get_in(w)
    try:
        it = int(it)-1
        if it >= len(p["BP"]) or it < 0:
            return[p["echo"], False]
    except:
        return[p["echo"], False]
    t = p["BP"].pop(it)
    return[translate("YOU FROWED IT AWAY"), True]

def shot_menager(w, c, m, p):
    w.clear()
    output(w, c, m, p)
    w.addstr(23, 0, translate("WHERE DO YOU WANT TO SHOT?"))
    it = get_in(w)
    dy, dx, t1 = player_move(it)
    enemies_class_is_shoted(m, p, [dy, dx], p["bow"])
    get_equip_values(p)
    return[p["echo"], True]
    #elif p["arrows_id"] == -1: # return ↑ but... -PR-
    #    return[translate("YOU DON'T HAVE ARROWS!"), False]
    #return[translate("YOU CAN'T SHOT THERE!"), False]

def pomoc(w, c, m, p): #not beautyful, but done -PR-
    w.clear()
    w.addstr(0, 0, "Tiles:", c.color_pair(4))
    w.addstr(0, 61, "Version = pre_0.2.0", c.color_pair(1))
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
    w.addstr(20, 2, "+ - use (backpack)     / - sort (no turns used)    ? - help", c.color_pair(5))
    w.addstr(21, 2, ", - drop (backpack)    > - go down    < - go up    0 - shot", c.color_pair(5))
    w.addstr(23, 4, "Don't forget about NumLock!", c.color_pair(2))
    #w.addstr(22, 4, "Not working? NumLock!", c.color_pair(4))
    #w.addstr(23, 0, "Press enter to continue", c.color_pair(4))
    get_in(w)

# def item_menager_keyin(m, p, key):

def keyin(w, c, m, p, pos, key):
    match key:
        #case "-":
        #     pass
        case "+":
             return item_menager(w, c, m, p)
        case ",":
             return drop_menager(w, c, m, p)
        case "0":
             return shot_menager(w, c, m, p)
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
            get_equip_values(p)
            return [p["echo"], False]
        case "?":
            pomoc(w, c, m, p)
            return [p["echo"], False]
        case _:
           # move a player? (but in where!?), -PR- ?
           #		echo, moved?
            return ["? - for help", False]
