from random import randint, choice
#from time import sleep
from local_scripts import zero3  # or "*" -PR-
from local_map import map_init
from local_enemies_class import enemies_class_clear

from local_equip import get_equip_values
from local_translator import translate
from local_item_class import get_item, disable_disabled_weapons, randitem


def menager(w, c, command = "#R", m = {}, p = {}): # #E - end game #R - try to reload or start, #S - save, #U - go up, #D - go down -PR-
    match command[:2]:
        case "#E":
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
            character(w, c, p)
            prepare_map(m, p)
            return m, p, path

def character(w, c, p):
    w.clear() # ? -PR-
    w.addstr(0, 30, "DUNGEON OF SHADOW IMPS", c.color_pair(2))
    w.addstr(1, 25, "SELECT A CHARACTER TO PLAY WITH", c.color_pair(1))
    w.addstr(2, 37, "0.2.0", c.color_pair(4))
    w.addstr(4, 2, "1 - HUMAN WARRIOR", c.color_pair(1))
    w.addstr(5, 2, "2 - HUMAN BANDIT", c.color_pair(1))
    w.addstr(6, 2, "3 - HUMAN DUELIST", c.color_pair(1))
    w.addstr(7, 2, "4 - HUMAN ROGUE", c.color_pair(1))
    w.addstr(8, 2, "5 - HUMAN ARCHER", c.color_pair(1))
    #w.addstr(9, 2, "6 - HOBBIT WARRIOR", c.color_pair(1))
    if w.getmaxyx() != (24,80):
        w.addstr(23, 3, "The screen could't resize it self! (24x80)", c.color_pair(2))
        w.addstr(22, 79, "|", c.color_pair(3))
        w.addstr(23, 71, "point ->", c.color_pair(3))
    w.refresh() # w.getkey() makes the same + ... -PR-
    while True:
        match w.getkey():
            case "1":
                p["strength"] = 11
                p["dexterity"] = 7
                p["playertype"] = "HUMAN WARRIOR"
                break
            case "2":
                p["strength"] = 10
                p["dexterity"] = 8
                p["playertype"] = "HUMAN BANDIT"
                break
            case "3":
                #p["playertype"] = "HUMAN DUELIST"
                break
            case "4":
                p["strength"] = 8
                p["dexterity"] = 10
                p["playertype"] = "HUMAN ROUGE"
                break
            case "5":
                p["strength"] = 7
                p["dexterity"] = 11
                p["playertype"] = "HUMAN ARCHER"
                #p["BP"].append({"item": "ARROW", "type": "", "values": [40, "ARROWS"], "cost": 5, "grouping": True})
                #p["arrows_id"] = 1
                break
            #case "6":
            #    p["strength"] = 5
            #    p["dexterity"] = 2
            #    p["playertype"] = "HOBBIT WARRIOR"
            #    p["maxhp"], p["hp"] = 10, 10
            #    p["basedefend"] = 70
            #    p["hpcounter"] = 14
            #    p["maxeat"] *= 7 # hobbits and elfish waybread :) -PR-
            #    break
            case _:
                pass
    get_equip_values(p)
    w.clear()
    w.addstr(5, 5, "The angel of the LORD came back a second time and touched YOU and said:", c.color_pair(5))
    w.addstr(6, 13, '"Get up and eat, for the journey is too much for you."', c.color_pair(1))
    w.addstr(23, 65, "~ 1 KINGS 19:7", c.color_pair(5))
    w.getkey()
    #disable_disabled_weapons(p["strength"], p["dexterity"])

def prepare_map(m, p):
    h = p["camp"][p["id_camp"]][p["depth"]].copy()
    while h == "next": # not used -PR-
        p["id_camp"] += 1
        h = p["camp"][p["id_camp"]][p["depth"]]
    if h[0] == "?":
        h[0] = p["type"]
        i = randint(-1, 1)
        if p["type"] + i in {0,1,2}:
            p["type"] += i
    #p["type"] += p["shift_type_of"] # +"shift" -PR-
    enemies_class_clear()
    ilist, xp = [], 0
    if type(h[0]) == int:
        p["normal_level"] = h[0] < 100 # "needs" are enable/disable -PR-
        if p["normal_level"]:
            ilist = randitem(h[0]+5) # +5 -PR-
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
        "playertype": "Human Duelist",
        "normal_level": True,
        "shift_type_of": 0,#at the depth -PR-
        "maxeat": 2000,
        "maxhp": 20,
        "hp": 20,
        "hpchange": 1,
        "hpcounter": 10,
        "needxp": 20,
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
        "e_attack": get_item(24),
        "e_hand": get_item(33),
        "e_armor": get_item(17),
        "blessing": 0,
        "fury": 0,
        "y": 0,
        "x": 0,
        "dy": 0, # direction y -PR-
        "dx": 0,
        "wasattackby": "",
        "echo": "",
        "torch": True,
        "torchtime": 800,
        "starving": False,
        "fullness": 600,
        "BP": [
            get_item(0)[:2] + [20] + get_item(0)[3:],
            get_item(3),
            get_item(8),
            #for testing only{"item": "MAGIC MAPPING", "type": "!", "values": [20, "MAGIC MAPPING"], "cost": 40, "grouping": True},
            ],
        "time": 0,
        "moved": True,
        "id_camp": 0,
        "type": 1, # type of dungeon -PR-
        "camp": [[["surface",0],["?",3],["?",3],["?",3],["?",3],["?",3],["?",3],["?",3],["?",3],["?",3],["?",3],["?",3],["?",3],["?",3],["?",3],["?",3],["?",3],["?",3],["?",3],["?",3],["?",3],["surface",3]],
                ]
        }
    return m, p, path
