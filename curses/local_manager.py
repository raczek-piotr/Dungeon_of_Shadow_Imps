from random import randint, choice
from local_iostream import write2log
#from time import sleep
from local_scripts import zero3
from local_map import map_init
from local_enemies_class import enemies_class_clear
from local_character import character
from local_scores import scoreboard_append, scoreboard_print
from local_npc import load_traders

from local_equip import get_equip_values
from local_translator import translate
from local_item_class import get_item, randitem, mage_items
from local_output import output


_type = 1 # local (script) permanent variable -PR-
c_type = [0,2,1,2,3,3] # color_type -PR-


def manager(w, c, command = "#R", m = {}, p = {}): # #E - end game #R - try to reload or start, #S - save, #U - go up, #D - go down -PR-
    match command[:2]:
        case "#E": # END -PR-
            get_equip_values(p)
            score = scoreboard_append(w, c, p)
            write2log("player ends his game with score: "+str(score))
            w.clear()
            output(w, c, m, p)
            w.addstr(23, 0, translate(choice(["YOU SLOWLY CLOSED YOUR EYES", "YOU DIED", "YOU NEVER KNOW WHAT HAPPENED", "YOU THINK - OH NO, WHAT I HAVE DONE!"]))+"...")
            w.addstr(23, 56, "score: "+str(score), c.color_pair(2))
            w.getkey()
        case "#!": # SCROLL OF DISTURBANCES -PR-
            d = p["depth"] % 10
            p["depth"] = (p["depth"]+randint(1, 9))%10 + 10*d
            p["hp"] = p["mhp"]
            prepare_map(c, m, p)
            p["echo"] = translate("YOU READ A") + " " + translate("SCROLL OF DISTURBANCE")
        case "#U": # UP-starir -PR-
            p["depth"] -= 1
            prepare_map(c, m, p)
            p["echo"] = translate("YOU WENT UPSTAIRS, AND THE DOOR CLOSED BEHIND YOU")
        case "#D": # DOWN-starir -PR-
            p["depth"] += 1
            if p["depth"] >= 40:
                p["echo"] = "#"
                scoreboard_append(w, c, p, True) # Win The Game
            else:
                prepare_map(c, m, p)
                if command[2:] == "!":
                    p["echo"] = translate("YOU FALL DOWN!")
                    p["hp"] -= p["maxhp"]//2
                    if p["hp"] <= 0: # not working (nothing changes) -PR-
                        p["echo"] = translate("YOU FALL DOWNSTAIRS AND DIED!") # not working -PR-
                else:
                    p["echo"] = translate("YOU WENT DOWNSTAIRS, AND THE DOOR CLOSED BEHIND YOU")
        case "#R": # RESET -PR-
            c.init_pair(1, 231, -1)
            c.init_pair(2, 46, -1)
            c.init_pair(3, 5, -1)
            c.init_pair(4, 136, -1)
            c.init_pair(5, 245, -1)
            c.init_pair(6, 57, -1)
            c.init_pair(7, 196, -1)
            c.init_pair(8, 41, -1) #It don't need to be definited here -PR-
            c.init_pair(9, 238, -1)
            m, p, path = character(w, c, p) # I have to return the first data -PR-
            if p["ismage"]:
                mage_items()
            load_traders(p)
            get_equip_values(p)
            scoreboard_print(w, c)
            w.clear()
            w.addstr(5, 4, "The angel of the LORD came back a second time and touched 'you' and said:", c.color_pair(5))
            w.addstr(6, 13, '"Get up and eat, for the journey is too much for you."', c.color_pair(1))
            w.addstr(23, 65, "~ 1 KINGS 19:7", c.color_pair(5))
            w.getkey()
            prepare_map(c, m, p)
            return m, p, path

def prepare_map(c, m, p):
    global _type, c_type
    h = p["camp"][p["id_camp"]][p["depth"]].copy()
    while h == "next": # not used -PR-
        p["id_camp"] += 1
        h = p["camp"][p["id_camp"]][p["depth"]].copy()
    if h[0] in {0,1,2,3}:
        i = randint(-1, 1)
        if _type + i in {0,1,2}:
            _type += i
        p["type"] = _type + h[0] #h[0] is shift
        type_of = p["type"]
    elif h[0] in {10,11,12,13,15}:
        p["type"] = h[0] - 10
        type_of = p["type"]
    else: #int
        type_of = h[0]
        p["type"] = h[1]
    enemies_class_clear()
    ilist = []
    if type(h[0]) == int:
        p["normal_level"] = True # "needs" are enable/disable -PR-
        ilist = randitem(h[0]+5, 8, 58)+randitem(2, 0, 4)# + arrows -PR-
        for _ in range(randint(0,3+p["type"])):
            ilist.append("$"+zero3(randint(3,5+5*p["type"])))
        if p["type"] == 2:
            ilist += randitem(4, 4, 4)
    #else:
    #    p["normal_level"] = False
    print(p["type"])
    typ = c_type[p["type"]] # TYPe -PR-
    if typ < 0:
        typ = 0
    elif typ > 3:
        typ = 3
    if typ == 0:
        c.init_pair(8, 245, -1)
    elif typ == 1:
        c.init_pair(8, 41, -1)
    elif typ == 2:
        c.init_pair(8, 238, -1)
    else: # == 3
        c.init_pair(8, 196, -1)
    p["environment_bonus"] = p["environment"][typ]
    p["y"], p["x"] = map_init(m, p, ilist, type_of, h[1])
