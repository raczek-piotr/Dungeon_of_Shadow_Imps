#import curses as c
from random import randint

from local_output import output, item

from local_translator import translate
from local_input_key import *
from local_enemies_class import enemies_class_is_shoted
from local_equip import get_equip_values #, merge # not needed -PR-
from local_scores import scoreboard_print
from local_spells import spell_menager


def print_menager(w, c, m, p, cm, bc): # m is'n needed, but for formality it is -PR-
    w.clear()
    w.addstr(0, 0, translate("FOOD")+":  "+(translate("STARVING") if p["starving"] else str(p["fullness"])+"/"+str(p["maxeat"])), c.color_pair(4))
    w.addstr(1, 0, translate("LIGHT")+": "+(translate("NO LIGHT") if not p["torch"] else str(p["torchtime"])), c.color_pair(4))
    w.addstr(3, 0, translate("CRITIC CHANCE")+": "+ str(p["environment_bonus"]) + "/10", c.color_pair(8))
    if p["inteligence"] > 0:
        w.addstr(5, 0, "str|dex|int " + str(p["strength"]) + "|" + str(p["dexterity"]) + "|" + str(p["inteligence"]), c.color_pair(4))
    else:
        w.addstr(5, 0, "str|dex " + str(p["strength"]) + "|" + str(p["dexterity"]), c.color_pair(4))
    w.addstr(6, 0, "hp: " + str(p["hp"]) + "/" + str(p["maxhp"]), c.color_pair(4))
    w.addstr(7, 0, "xp: " + str(p["xp"]) + "/" + str(p["needxp"]), c.color_pair(4))
    w.addstr(10, 0,"Equipted:", c.color_pair(4))
    w.addstr(11, 2, item(p["e_attack"], 9, p), c.color_pair(5))
    w.addstr(12, 2, item(p["e_hand"], 9, p), c.color_pair(5))
    w.addstr(13, 2, item(p["e_armor"], 9, p), c.color_pair(5))
    w.addstr(16, 0, "Backpack:", c.color_pair(4))
    w.refresh() # ? -PR-
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
    if t[1] in {"]","}",")","??"}:
        p["BP"][it], p[t[0][1]] = p[t[0][1]], p["BP"][it]
        get_equip_values(p)
        return[translate("YOU EQUIP") + " " + translate(t[0][0]), True]
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
                p["BP"].pop(it)
                if t[0][2] == 0:
                    for q in range(len(p["BP"])):
                        if not p["BP"][q][-2]:
                            p["BP"][q][-2] = True
                            if p["BP"][q][1] in {"?","!"}:
                                p["BP"][q][0] = p["BP"][q][0].copy()
                                if p["BP"][q][1] == "?":
                                    p["BP"][q][0][0] = ["SCROLL OF IDENTYFY","SCROLL OF TELEPORTATION","SCROLL OF BLESSING","TREASURE MAPPING","SCROLL OF DISTURBANCE"][p["BP"][q][0][2]]
                                elif p["BP"][q][1] == "!":
                                    p["BP"][q][0][0] = ["POTION OF HEALING","POTION OF ENHANCEMENT","POTION OF FURY","POTION OF POISON"][p["BP"][q][0][2]]
                    return[translate("YOU READ A") + " " + translate("SCROLL OF IDENTIFY"), True]
                elif t[0][2] == 1:
                    mx, my = m["sx"]-1, m["sy"]-1
                    q = "#"
                    while q[0] not in {".",","," ","]","}",")","$","~","-","*","!","?","<",">","=","%"} or q == "  ":
                        x, y = randint(1, mx), randint(1, my)
                        q = m["r"][y][x]
                    p["x"], p["y"] = x, y
                    return[translate("YOU READ A") + " " + translate("SCROLL OF TELEPORTATION"), True]
                elif t[0][2] == 2:
                    p["blessing"] += 100
                    return[translate("YOU READ A") + " " + translate("SCROLL OF BLESSING"), True]
                elif t[0][2] == 3:
                    for y in range(m["sy"]):
                        for x in range(m["sx"]):
                            if m["r"][y][x][0] in {"]","}",")","$","~","-","*","!","?"}:
                                for y2 in range(y-1, y+2):
                                    for x2 in range(x-1, x+2):
                                        m["v"][y2][x2] = m["r"][y2][x2]
                    return[translate("YOU READ A") + " " + translate("SCROLL OF TREASURE MAPPING"), True]
                elif t[0][2] == 4:
                    return["#!", True] #return[translate("YOU READ A") + " " + translate("SCROLL OF DISTURBANCE"), True]
                else: # CYCLOPE-DIA -PR-
                    if randint(0, 1):
                        p["strength"] += 1
                    else:
                        p["dexterity"] += 1
                    return[translate("YOU READ A") + " " + translate("CYCLOPE-DIA"), True]
            case 3: # potions
                p["BP"].pop(it)
                if t[0][2] == 0:
                    p["hp"] = p["maxhp"]
                    return[translate("YOU DRANK") + " " + translate("POTION OF HEALING"), True]
                elif t[0][2] == 1:
                    p["blessing"] += 25
                    p["fury"] += 25
                    p["hp"] += p["maxhp"]//2
                    if p["hp"] > p["maxhp"]:
                        p["hp"] = p["maxhp"]
                    return[translate("YOU DRANK") + " " + translate("POTION OF ENHANCEMENT"), True]
                elif t[0][2] == 2:
                    p["fury"] += 100
                    return[translate("YOU DRANK") + " " + translate("POTION OF FURY"), True]
                else:
                    p["hp"] -= p["maxhp"]//2
                    c.beep() # alarm the player -PR-
                    return[translate("YOU DRANK") + " " + translate("POTION OF POISON"), True]
                    
        return[translate("YOU CAN'T USE THAT"), False]

    get_equip_values(p)
    return[translate("YOU TOOK A") + " " + translate(t[0][0]), True]
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
    w.addstr(23, 0, translate("WHERE DO YOU WANT TO SHOT?"), c.color_pair(1))
    it = get_in(w)
    dy, dx, t1 = player_move(it)
    if t1 and it != "5":
        enemies_class_is_shoted(m, p, [dy, dx], p["bow"])
        get_equip_values(p)
        return[p["echo"], True]
    return[translate("WRONG DIRECTION!"), False]
    #elif p["arrows_id"] == -1: # return ↑ but... -PR-
    #    return[translate("YOU DON'T HAVE AMMO!"), False]
    #return[translate("YOU CAN'T SHOT THERE!"), False]

def help(w, c, m, p): #not beautyful, but done -PR-
    w.clear()
    w.addstr(0, 0, "Game tiles:", c.color_pair(4))
    w.addstr(1, 2, "@/  - you/", c.color_pair(1))
    w.addstr(1, 4, "@", c.color_pair(2))
    w.addstr(1, 12, "NPC", c.color_pair(2))
    w.addstr(1, 28, ". - light tile", c.color_pair(5))
    w.addstr(1, 54, "  - dark tile", c.color_pair(4))
    w.addstr(2, 2, "# - wall", c.color_pair(5))
    w.addstr(2, 28, "+ - closed door", c.color_pair(4))
    w.addstr(2, 54, ", - open door", c.color_pair(4))
    w.addstr(3, 2, "> - stairs down", c.color_pair(1))
    w.addstr(3, 28, "< - stairs up", c.color_pair(1))
    w.addstr(3, 54, '^ - very steep hill', c.color_pair(1))

    w.addstr(4, 2, '% - tree/forest', c.color_pair(2))
    w.addstr(4, 28, '= - water/river/lake', c.color_pair(6))
    w.addstr(4, 54, '& - lava', c.color_pair(7))

    w.addstr(6, 0, "Game items:", c.color_pair(4))

    w.addstr(7, 2, "] - melee weapon", c.color_pair(2))
    w.addstr(7, 28, "} - ranged weapon", c.color_pair(2))
    w.addstr(7, 54, ") - armor", c.color_pair(2))

    w.addstr(8, 2, "~ - torch", c.color_pair(2))
    w.addstr(8, 28, "* - food", c.color_pair(2))
    w.addstr(8, 54, "- - arrows", c.color_pair(2))

    w.addstr(9, 2, "? - scroll or a book", c.color_pair(2))
    w.addstr(9, 28, "! - potion", c.color_pair(2))
    w.addstr(13, 2, "* - to see scoreboard", c.color_pair(2))


    w.addstr(16, 0, "Movement:", c.color_pair(4))
    w.addstr(17, 4, "7 8 9", c.color_pair(1))
    w.addstr(18, 4, "4 5 6   5 - wait or take item from the flor", c.color_pair(1))
    w.addstr(19, 4, "1 2 3", c.color_pair(1))
    w.addstr(20, 2, "+ - use (backpack)     ? - help", c.color_pair(5))
    w.addstr(21, 2, ", - drop (backpack)    > - go down    < - go up    0 - shot / cast a spell", c.color_pair(5))
    w.addstr(23, 4, "Don't forget about NumLock!", c.color_pair(2))
    w.addstr(23, 61, "Version = Base_0.5", c.color_pair(1))
    #w.addstr(22, 4, "Not working? NumLock!", c.color_pair(4))
    #w.addstr(23, 0, "Press enter to continue", c.color_pair(4))
    w.getkey()

    if p["classicgame"]:
        return

    w.clear()
    w.addstr(0, 0, "Using spells (colors):", c.color_pair(4))
    w.addstr(2, 2, "You can use this spell", c.color_pair(1))
    w.addstr(3, 2, "You can't use this spell (your PC inteligence is to low...)", c.color_pair(5))
    w.addstr(4, 2, "You can't use this spell (your PC need to be on tile with nature)", c.color_pair(2))
    w.addstr(5, 2, "You can't use this spell (your PC need to be on tile with water)", c.color_pair(6))
    w.addstr(23, 4, "Don't forget about NumLock!", c.color_pair(2))
    w.addstr(23, 61, "Version = Base_0.5", c.color_pair(1))
    w.getkey()

# def item_menager_keyin(m, p, key):

def keyin(w, c, m, p, pos, key):
    match key:
        #case "-":
        #    pass
        case "+":
            return item_menager(w, c, m, p)
        case ",":
            return drop_menager(w, c, m, p)
        case "0":
            if p["magic_list"]:
                return spell_menager(w, c, m, p)
            return shot_menager(w, c, m, p)
        case ">":
            if m["r"][pos[0]][pos[1]][0] == ">":
                return ["#D", False]
            return [translate("YOU CAN'T GO DOWN HERE"), False]
        case "<":
            if m["r"][pos[0]][pos[1]][0] == "<":
                return ["#U", False]
            return [translate("YOU CAN'T GO UP HERE"), False]
        #case "/":
        #    sort(p)
        #    get_equip_values(p)
        #    return [p["echo"], False]
        case "?":
            help(w, c, m, p)
            return [p["echo"], False]
        case "*":
            scoreboard_print(w, c)
            return [p["echo"], False]
        case _:
           # move a player? (but in where!?), -PR- ?
           #		echo, moved?
            return ["? - for help", False]
