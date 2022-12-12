from random import randint, choice
from local_zero3 import zero3  # or "*" -PR-
from local_map import map_init
from local_item_class import item_class_init, item_class_clear
from local_enemies_class import enemies_class_clear
from local_translator import translate

def menager(command = "#R", m = {}, p = {}): # #R - try to reload or start, #S - save, #U - go up, #D - go down -PR-
    match command:
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
    item_class_clear()
    enemies_class_clear()
    elist = [0,1,2]
    ilist = ["]" + zero3(item_class_init("]", {"item": "DAGGER [", "type": "]", "values": [4, 1, 10], "ident": False, "grouping": False}))]
    for i in range(15):
        ilist.append("$" + zero3(item_class_init("$", randint(1, 99))))
    for i in range(2):
        ilist.append("-" + zero3(item_class_init("-", {"item": "ARROW", "type": "", "values": [randint(10, 40), "ARROWS"], "ident": True, "grouping": True})))
    for i in range(randint(0, 2)):
        ilist.append("~" + zero3(item_class_init("~", {"item": "TORCH", "type": "", "values": [1, "TORCHES"], "ident": True, "grouping": True})))
    p["y"], p["x"] = map_init(m, p, ilist, elist, choice([0,2]))#randint(0,2))

def start_data():
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
        "mana": 1,
        "manacounter": 75,
        "maxhp": 20,
        "hp": 1,
        "hpchange": 4,
        "hpcounter": 10,
        "needxp": 5,
        "xp": 0,
        "lw": 1,
        "depth": 1,
        "strength": 10,
        "gold": 0,
        "attack": {"item": "DAGGER [", "type": "]", "values": [4, 1, 10], "ident": True, "grouping": False},
        "hand": {"item": "SHORT BOW {", "type": "}", "values": [3, 1, 10], "ident": True, "grouping": False},
        "armor": {"item": "FUR (", "type": ")", "values": [1, 1, 9], "ident": True, "grouping": False},
        "y": 0,
        "x": 0,
        "newy": 0,
        "newx": 0,
        "wasattackby": "",
        "echo": "",
        "torch": True,
        "torchtime": 350,
        "BP": [
               {"item": "BOW {", "type": "}", "values": [5, 2, 12], "ident": False, "grouping": False},
               {"item": "ARROW", "type": "", "values": [35, "ARROWS"], "ident": True, "grouping": True},
               {"item": "TORCH", "type": "", "values": [1, "TORCHES"], "ident": True, "grouping": True},
# no rings for a time! -PR- {"item": "RING |", "type": "|", "values": ["RING OF POWER |", 1], "ident": True, "grouping": False},
               {"item": "POTION OF HEALING", "type": "", "values": [2, "POTIONS OF HEALING"], "ident": True, "grouping": True}
               ],
        "time": 0,
        "moved": True,
        }
    return m, p, path