from random import randint, choice
from local_translator import translate
from local_output import item
from local_item_class import get_item
from local_equip import get_equip_values, update_BP_mask, merge, f_BP_mask


traders = [{2,3,49,23,24},
           {14,35,23,38},
           {9,4,12}]

def npc(w, c, m, p, it, stay):
    it = int(it)
    match it:
        case 0:
            return trader(w, c, m, p, it, "Seller")
        case 1:
            return[False, translate("- DO YOU JOB!"), False]
            return trader(w, c, m, p, it, "Mayor")
        case 2:
            return trader(w, c, m, p, it, "Blue The Robin")
        case 3:
            return[False, translate("- HEY! I'M DOING MY TOILET, GO AWAY!"), False]
        case _:
            return[False, translate(choice(["- DO YOUR JOB, I WAN'T HELP YOU!", "- ASK BLUE ROBIN FOR HELP", "- WHAT A NICE DAY!", "- WHAT A NICE DAY!", "- HAVE A NICE DAY!", "- IF YOU HAVE NONETHING TO DO, GO TO THE DUNGEON"])), False]

def trader(w, c, m, p, it, trader): #it → id, but id is definited by python -PR-
    q = "-"
    ilist = [get_item(i) for i in traders[it]]
    slots = {str(i) for i in range(len(ilist))}
    while True:
        if q in slots:
            i = ilist[int(q)]
            if (len(p["BP"]) < 6 or i["item"] in f_BP_mask() and i["grouping"]) and p["gold"] >= i["cost"]:
                p["gold"] -= i["cost"]
                p["BP"].append(i)
                merge(p)
                update_BP_mask(p)
                get_equip_values(p)
                echo = translate("YOU BUY")+" "+translate(i["item"][:-2] if i["item"][-1] in {"[","{","("} else i["item"])
                return[False, echo, True]
            else:
                if len(p["BP"]) < 6:
                    echo = translate("YOU DON'T HAVE ENOUGH MONEY!")
                else:
                    echo = translate("YOUR'S BACKPACK IS FULL!")
                return[False, echo, False]
        elif q in {"PADENTER","\n", ",", "\x1b"}:
            return[False, p["echo"], False]
        w.clear()
        w.addstr(0, 4, trader, c.color_pair(5))
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