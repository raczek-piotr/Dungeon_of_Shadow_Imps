from random import randint, choice
from local_translator import translate
from local_output import item
from local_item_class import get_item
from local_equip import get_equip_values, merge
from local_iostream import trades_save
from local_iostream import trades_load


traders = []
def load_traders(p):
    global traders
    if traders != []:
        return
    traders = [{5,6,7,51},
           {60, 61, randint(27, 50), randint(27, 50), randint(27, 50), 52, 56},
           {26},
           {},
           {61, 62, randint(27, 50), randint(27, 50), randint(27, 50), randint(27, 50), randint(52, 59)},
           {5,7, randint(27, 50), randint(27, 50)},
           {4,7, randint(27, 50), randint(27, 50), randint(27, 50), randint(27, 50)}]
    if p["classicgame"] == False:
        traders[2] = {26, 63, 66}
        traders[5] = {5,7, randint(63, 66), randint(27, 50), randint(27, 50)}
        traders[6] = {4,7, randint(63, 66), randint(27, 50), randint(27, 50), randint(27, 50), randint(27, 50)}

def trades_do_save():
    global traders
    return trades_save(traders)
def trades_do_load():
    global traders
    traders = trades_load()

def npc(w, c, m, p, it, stay):
    it = int(it)
    match it:
        case 0:
            return trader(w, c, m, p, it, "Trader", [
[["ROCK", "ROCKS"], "-", 25, True, 1],
])
        case 1:
            return trader(w, c, m, p, it, "Armory", [
[["ARROW", "ARROWS"], "-", 25, True, 2],
[["BOLT", "BOLTS"], "-", 25, True, 2],
[['9mm AMMO', '9mm AMMOS'], '-', 10, True, 5],
])
        case 2:
            return trader(w, c, m, p, it, "Druid", [[["POTION OF ENHANCEMENT", 3, 1], "!", 1, True, 120],[["POTION OF HEALING", 3, 0], "!", 1, True, 120]])
        case 3:
            return[False, translate("- I DON'T KNOW WHAT TO THINK ABOUT YOUR DREAM!"), False]
        case 4:
            return trader(w, c, m, p, it, "Armory", [
[["ARROW", "ARROWS"], "-", 25, True, 2],
[["BOLT", "BOLTS"], "-", 25, True, 2],
[['9mm AMMO', '9mm AMMOS'], '-', 10, True, 5],
])
        case 5:
            return trader(w, c, m, p, it, "Lost Dwarwish Trader", [[["POTION OF HEALING", 3, 0], "!", 1, True, 120], [["POTION OF ENHANCEMENT", 3, 1], "!", 1, True, 120],[['9mm AMMO', '9mm AMMOS'], '-', 10, True, 5],[["BOLT", "BOLTS"], "-", 25, True, 2]])
        case 6:
            return trader(w, c, m, p, it, "Guardian", [[["SCROLL IDENTIFY", 2, 0], "?", 1, True, 100]])
        case 7:
            return[False, translate(), False]
        case 8:
            return[False, translate("- SHERIF IS EMBARRASSED"), False]
        case 9:
            return[False, translate(choice(["- DO YOUR JOB, I WAN'T HELP YOU!", "- FIND THE BOOK OF BOOKS", "- CIVILIZATION? NO, NOBODY LIVE HERE LIKE HIM... I NEVER SEE HIM", "- BRING LIGHT TO YOUR VILLAGE!", "- THE DRUID IS BETWEEN THE RIVERS"])), False]
        case 10:
            return[False, translate(choice(["- FOOD? WE ATE MOLD... IT IS EVERYWERE!", "- FUNGAL GARDENS ARE BELOW US, WITH MOLD!"])), False]
    return[False, p["echo"], False]

def in_BP(BP, item): #copy is in local_terrain.py
    for i in BP:
        if i[0] == item[0]:
            return True
    return False

def trader(w, c, m, p, it, trader, ilist = []): #it → id, but id is definited (as a function) by python -PR-
    q = ""
    for i in traders[it]:
        ilist.append(get_item(i)) 
    slots = {str(i) for i in range(len(ilist))}
    for i in ilist:
        if i[1] == "-":
            i[-1] *= i[2]
    while True:
        if q in slots:
            i = ilist[int(q)]
            if (len(p["BP"]) < 6 or i[1] == "-" and in_BP(p["BP"], i)) and p["gold"] >= i[-1]:
                p["gold"] -= i[-1]
                if i[1] == "-":
                    i[-1] //= i[2]
                p["BP"].append(i)
                merge(p)
                #get_equip_values(p)
                echo = translate("YOU BUY")+" '"+translate(item(i, 9, p))+"'"
                return[False, echo, True]
            else:
                if len(p["BP"]) < 6 or i[1] == "-" and in_BP(p["BP"], i):
                    echo = translate("YOU DON'T HAVE ENOUGH MONEY!")
                else:
                    echo = translate("YOUR BACKPACK IS FULL!")
                return[False, echo, False]
        elif q in {"s","-"}:
            return seller(w, c, m, p, it, trader, ilist)
        elif q in {"PADENTER","\n", ",", "\x1b"}:
            return[False, p["echo"], False]
        w.clear()
        w.addstr(0, 4, trader, c.color_pair(5))
        w.addstr(1, 2, "Your gold: "+str(p["gold"]), c.color_pair(1))
        w.addstr(2, 0, "Items:", c.color_pair(5))
        for i in range(len(ilist)):
            w.addstr(i+3, 2, str(i)+": "+item(ilist[i], 9, p), c.color_pair(1))
            t = str(ilist[i][-1])
            w.addstr(i+3, 68, "COST:", c.color_pair(1))
            w.addstr(i+3, 78-len(t), t, c.color_pair(1))
        w.addstr(22, 0, "'s' or '-' to sell something", c.color_pair(4))
        w.addstr(23, 60, "Esc: ',' or 'Enter'", c.color_pair(5))
        q = w.getkey()
    return[True, echo, True]

def seller(w, c, m, p, it, trader, ilist = []): #it → id, but id is definited by python -PR-
    q = ""
    slots = {str(i) for i in range(len(p["BP"]))}
    for i in ilist:
        if i[1] == "-":
            i[-1] *= i[2]
    while True:
        if q in slots:
            q = int(q)
            echo = translate("YOU SELL")+" '"+translate(item(p["BP"], q, p))+"'"
            t = p["BP"][q][-1] * p["BP"][q][3]
            if p["BP"][q][1] == "-":
                t *= p["BP"][q][2]
            if p["BP"][q][1] == "!":
                t = 0
            t = t // 25
            p["gold"] += t
            p["BP"].pop(q)
            #merge(p)
            #get_equip_values(p)
            return[False, echo, True]
        #elif q in {"PADMINUS","-","s","S"}: #PADMINUS for windows; doesn't work -PR-
        #    seller(w, c, m, p, it, trader, ilist)
        #    return[False, p["echo"], False]
        elif q in {"PADENTER","\n", ",", "\x1b"}:
            return[False, p["echo"], False]
        w.clear()
        w.addstr(0, 4, trader, c.color_pair(5))
        w.addstr(1, 2, "Your gold: "+str(p["gold"]), c.color_pair(1))
        w.addstr(2, 0, "Items:", c.color_pair(5))
        for i in range(len(p["BP"])):
            w.addstr(i+3, 2, str(i)+": "+item(p["BP"], i, p), c.color_pair(1))
            t = p["BP"][i][-1] * p["BP"][i][3]
            if p["BP"][i][1] == "-":
                t *= p["BP"][i][2]
            t = str(t // 25)
            w.addstr(i+3, 68, "SELL:", c.color_pair(1))
            w.addstr(i+3, 78-len(t), t, c.color_pair(1))
        w.addstr(22, 0, "What do you want to sell?:", c.color_pair(4))
        w.addstr(23, 62, "Esc: ',' or Enter", c.color_pair(5))
        q = w.getkey()
    return[True, echo, True]