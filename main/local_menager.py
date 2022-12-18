from random import randint, choice
from local_zero3 import zero3  # or "*" -PR-
from local_map import map_init
from local_item_class import item_class_init, item_class_clear
from local_enemies_class import enemies_class_clear

from local_equip import get_equip_values
from local_translator import translate

s_maps = [0]
    

def menager(command = "#R", m = {}, p = {}): # #E - end game #R - try to reload or start, #S - save, #U - go up, #D - go down -PR-
    match command:
        case "#E":
            p["echo"] = translate(choice(["YOU SLOWLY CLOSED YOUR EYES", "YOU DIED", "YOU NEVER KNOW WHAT HAPPENED", "YOU THINK - OH NO, WHAT I HAVE DONE!"]))
        case "#U":
            p["depth"] -= 1
            prepare_map(m, p)
            p["echo"] = translate("YOU WENT UP")
        case "#D":
            p["depth"] += 1
            prepare_map(m, p)
            p["echo"] = translate("YOU WENT DOWN")
        case "#R":
            m, p, path = start_data() # only here the data in needed to give it back -PR-
            prepare_map(m, p)
            return m, p, path


def prepare_map(m, p):
    h = p["camp"][p["id_camp"]][p["depth"]]
    while p["camp"][p["id_camp"]][p["depth"]] == "next":
        p["id_camp"] += 1
        h = p["camp"][p["id_camp"]][p["depth"]]
    item_class_clear()
    enemies_class_clear()
    elist = [["r",4,2,1,1,7,False,[]],["r",4,2,1,1,7,False,[]],["r",4,2,1,1,7,False,[]],["g",5,2,2,1,7,True,[]],["g",5,2,1,2,7,True,[]]] # head "", hp, attack, xp, sleep, hear_range, archer T/F, drop []
    for i in range(p["depth"]-2):
        elist.append(["o",8,2,2,1,7,False,[]])
    for i in range((p["depth"]-2)//5):
        elist.append(["k",8,4,4,1,7,False,[]])
    for i in range(1 if p["lw"] > 7 else 0):
        elist.append(["t",32,5,20,1,7,False,[]])
    for i in range(randint(0, randint(0, 1))):
        elist.append(["a",1,10,4,1,7,True,[]])
    ilist = ["]" + zero3(item_class_init("]", {"item": "DAGGER [", "type": "]", "values": [4, 1, 10], "ident": False, "grouping": False}))]
    for i in range(randint(0, 6)):
        ilist.append("$" + zero3(item_class_init("$", randint(1, 39))))
    for i in range(randint(0, 2)):
        ilist.append("-" + zero3(item_class_init("-", {"item": "ARROW", "type": "", "values": [randint(2, 5), "ARROWS"], "ident": True, "grouping": True})))
    for i in range(randint(0, 2)):
        ilist.append("~" + zero3(item_class_init("~", {"item": "TORCH", "type": "", "values": [1, "TORCHES"], "ident": True, "grouping": True})))
    p["y"], p["x"] = map_init(m, p, ilist, elist, h[0], h[1]) # 0,1,2,

def start_data():
    global s_maps
    t = [i for i in range(2, 10, 2)]
    for i in range(2):
        s_maps.append(t.pop(randint(0,len(t)-1)))
    s_maps.sort()
    path = "data/"
    m = {
        "r": [],
        "v": [],
        "o": [],
        "m": [],
        "sy": 5,
        "sx": 5,
        }
    p = {
        "playertype": "Human Warrior",
        "specials": "",
        "name": "qwe",
        "maxmana": 2,
        "mana": 2,
        "manacounter": 75,
        "maxhp": 20,
        "hp": 20,
        "hpchange": 4,
        "hpcounter": 10,
        "needxp": 10,
        "xp": 0,
        "lw": 1,
        "depth": 0,
        "strength": 10,
        "gold": 0,
        "attack": 1,
        "bow": 1,
        "armor": 0,
        "food": 500,
        "e_attack": {"item": "DAGGER [", "type": "]", "values": [4, 1, 10], "ident": True, "grouping": False},
        "e_hand": {"item": "SHORT BOW {", "type": "}", "values": [3, 1, 10], "ident": True, "grouping": False},
        "e_armor": {"item": "FUR (", "type": ")", "values": [1, 1, 9], "ident": True, "grouping": False},
        "y": 0,
        "x": 0,
        "dy": 0, # direction y -PR-
        "dx": 0,
        "wasattackby": "",
        "echo": "",
        "torch": False,
        "torchtime": 0,
        "arrows_id": -1,
        "BP": [
               #{"item": "ARROW", "type": "", "values": [12, "ARROWS"], "ident": True, "grouping": True},
               #{"item": "TORCH", "type": "", "values": [1, "TORCHES"], "ident": True, "grouping": True},
# no rings for a time! -PR- {"item": "RING |", "type": "|", "values": ["RING OF POWER |", 1], "ident": True, "grouping": False},
               #{"item": "POTION OF HEALING", "type": "", "values": [2, "POTIONS OF HEALING"], "ident": True, "grouping": True}
               ],
        "time": 0,
        "moved": True,
        "id_camp": 0,
        "camp": [[["surface",0],[2,2],[2,3],"next"],
                ["next",[2,3],[2,1],["the-path",0]],
                [["Manipure",0],[2,2],[2,3],[2,1]]],
        }
    get_equip_values(p)
    return m, p, path