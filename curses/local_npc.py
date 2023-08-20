from random import randint, choice
from local_translator import translate
from local_output import item
from local_item_class import get_item
from local_equip import get_equip_values, merge


traders = [{5,7,26,27},
           {9,10,11,12,13,14,15,16},
           {25}]

def npc(w, c, m, p, it, stay):
    it = int(it)
    match it:
        case 0:
            return trader(w, c, m, p, it, "Seller", [
[["ROCK", "ROCKS"], "-", 5, True, 1],
[["ARROW", "ARROWS"], "-", 10, True, 2],
[["BOLT", "BOLTS"], "-", 25, True, 2]])
        case 1:
            return trader(w, c, m, p, it, "Powder Monkey", [["-",  [['9mm AMMO', '9mm AMMOS'], '-', 10, True, 5]]])
        case 2:
            return trader(w, c, m, p, it, "Druid", [[["POTION OF ENHANCEMENT", 3, 1], "!", 1, True, 100],[["POTION OF HEALING", 3, 0], "!", 1, True, 100]])
        case 3:
            return[False, translate("- HEY! I'M DOING MY TOILET, GO AWAY!"), False]
        case _:
            return[False, translate(choice(["- DO YOUR JOB, I WAN'T HELP YOU!", "- ASK BLUE ROBIN FOR HELP", "- WHAT A NICE DAY!", "- WHAT A NICE DAY!", "- HAVE A NICE DAY!", "- IF YOU HAVE NONETHING TO DO, GO TO THE DUNGEON"])), False]

def in_BP(BP, item): #copy is in local_terrain.py
    for i in BP:
        if i[0] == item[0]:
            return True
    return False

def trader(w, c, m, p, it, trader, ilist = []): #it → id, but id is definited by python -PR-
    q = "-"
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
                get_equip_values(p)
                echo = translate("YOU BUY")+" '"+translate(item(i))+"'"
                return[False, echo, True]
            else:
                if len(p["BP"]) < 6 or i[1] == "-" and in_BP(p["BP"], i):
                    echo = translate("YOUR BACKPACK IS FULL!")
                else:
                    echo = translate("YOU DON'T HAVE ENOUGH MONEY!")
                return[False, echo, False]
        elif q in {"PADENTER","\n", ",", "\x1b"}:
            return[False, p["echo"], False]
        w.clear()
        w.addstr(0, 4, trader, c.color_pair(5))
        w.addstr(1, 2, "Your gold: "+str(p["gold"]), c.color_pair(1))
        w.addstr(2, 0, "Items:", c.color_pair(5))
        for i in range(len(ilist)):
            w.addstr(i+3, 2, str(i)+": "+item(ilist[i], 9, False), c.color_pair(1))
            t = str(ilist[i][-1])
            w.addstr(i+3, 68, "COST:", c.color_pair(1))
            w.addstr(i+3, 78-len(t), t, c.color_pair(1))
        w.addstr(23, 62, "Esc: ',' or Enter", c.color_pair(5))
        q = w.getkey()
    return[True, echo, True]