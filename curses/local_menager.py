from random import randint, choice
#from time import sleep
from local_scripts import zero3  # or "*" -PR-
from local_map import map_init
from local_enemies_class import enemies_class_clear
from local_character import character
from local_scores import scoreboard_append, scoreboard_print

from local_equip import get_equip_values
from local_translator import translate
from local_item_class import get_item, randitem


_type = 1 #local permanent variable -PR-


def menager(w, c, command = "#R", m = {}, p = {}): # #E - end game #R - try to reload or start, #S - save, #U - go up, #D - go down -PR-
    match command[:2]:
        case "#E":
            scoreboard_append(w, c, p)
            p["echo"] = translate(choice(["YOU SLOWLY CLOSED YOUR EYES", "YOU DIED", "YOU NEVER KNOW WHAT HAPPENED", "YOU THINK - OH NO, WHAT I HAVE DONE!"]))
        case "#U":
            p["depth"] -= 1
            prepare_map(m, p)
            p["echo"] = translate("YOU WENT UPSTAIRS, AND THE DOOR CLOCED BEHIND YOU")
        case "#D":
            p["depth"] += 1
            prepare_map(m, p)
            if command[2:] == "!":
                p["echo"] = translate("YOU FALL DOWNSTAIRS!")
                p["hp"] -= p["maxhp"]//2
                #if p["hp"] <= 0: # not working (nothing changes) -PR-
                #    p["echo"] = translate("YOU FALL DOWNSTAIRS AND DIED!") # not working -PR-
            else:
                p["echo"] = translate("YOU WENT DOWNSTAIRS, AND THE DOOR CLOCED BEHIND YOU")
        case "#R":
            m, p, path = start_data() # only here the data in needed to give it back -PR-
            c.init_pair(1, 231, 16)
            c.init_pair(2, 46, 16)
            c.init_pair(3, 5, 16)
            c.init_pair(4, 136, 16)
            c.init_pair(5, 245, 16)#148 :) -PR-
            c.init_pair(6, 57, 16)
            c.init_pair(7, 196, 16)
            character(w, c, p)
            get_equip_values(p)
            scoreboard_print(w, c)
            w.clear()
            w.addstr(5, 5, "The angel of the LORD came back a second time and touched YOU and said:", c.color_pair(5))
            w.addstr(6, 13, '"Get up and eat, for the journey is too much for you."', c.color_pair(1))
            w.addstr(23, 65, "~ 1 KINGS 19:7", c.color_pair(5))
            w.getkey()
            prepare_map(m, p)
            return m, p, path

def prepare_map(m, p):
    global _type #local permanent variable -PR-
    h = p["camp"][p["id_camp"]][p["depth"]].copy()
    while h == "next": # not used -PR-
        p["id_camp"] += 1
        h = p["camp"][p["id_camp"]][p["depth"]].copy()
    if h[0] in {0,1}:
        i = randint(-1, 1)
        if _type + i in {0,1,2}:
            p["type"] = _type + h[0] #h[0] is shift
    enemies_class_clear()
    ilist = []
#    with open("logfile.txt", "a") as log:
#        log.write(str(h)+"\n")
#        log.write(str(_type)+"\n")
#        log.write(str(p)+"\n")
#        log.write(str(m)+"\n\n\n")
    if type(h[0]) == int:
        p["normal_level"] = True # "needs" are enable/disable -PR-
        ilist = randitem(h[0]+5, 8, 58)+randitem(2, 0, 4)# + arrows -PR-
        for _ in range(randint(0,3+p["type"])):
            ilist.append("$"+zero3(randint(3,5+5*p["type"])))
    #else:
    #    p["normal_level"] = False 
    p["y"], p["x"] = map_init(m, p, ilist, h[0], h[1])

def start_data():
    path = "data/"
    m = {
        "r": [],
        "v": [],
        "m": [],
        "sy": 5,
        "sx": 5,
        }
    p = {
        "playertype": "HUMAN DUELIST",
        "normal_level": True,
        "shift_type_of": 0,#at the depth -PR-
        "skill": 1,
        "maxeat": 2000,
        "maxhp": 20,
        "hp": 20,
        "hpchange": 2,
        "reg_time": 10,
        "reg_1/": 10,
        "needxp": 40,
        "xpchange": 40,
        "xp": 0,
        "lw": 1,
        "depth": 0,
        "strength": 9,
        "dexterity": 9,
        "gold": 250,
        "attack": 1,
        "bow": 1,
        "armor": 0,
        "attack_acc": 1,
        "bow_acc": 1,
        "basedefend": 50,
        "defend": 0,
        "attack_damage": 1,
        "bow_damage": 1,
        "attack_hits": 1,
        "bow_hits": 1,
        "e_attack": get_item(23),
        "e_hand": get_item(50),
        "e_armor": get_item(16),
        "blessing": 0,
        "fury": 0,
        "y": 0,
        "x": 0,
        "dy": 0, # direction y -PR-
        "dx": 0,
        "wasattackby": "",
        "echo": "",
        "torch": True,
        "torchtime": 1200,
        "starving": False,
        "fullness": 1500,
        "BP": [
            get_item(0)[:2] + [20] + get_item(0)[3:],
            get_item(6),
            get_item(7),
            #for testing only{"item": "MAGIC MAPPING", "type": "!", "values": [20, "MAGIC MAPPING"], "cost": 40, "grouping": True},
            ],
        "time": 0,
        "moved": True,
        "id_camp": 0,
        "type": 1, # type of dungeon -PR-
        "camp": [[["surface",0],[0,3],[0,3],[0,3],[0,3],[0,3],[0,3],[0,3],[0,3],[0,3],["fudit_village",3],[3,3],[3,3],[3,3],[1,3],[1,3],[1,3],[1,3],[1,3],[1,3],["surface",3]],
                ]
        }
    return m, p, path