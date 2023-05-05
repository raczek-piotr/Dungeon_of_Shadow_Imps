from random import randint, choice
from local_zero3 import zero3  # or "*" -PR-
from local_map import map_init
from local_item_class import item_class_init, item_class_clear
from local_enemies_class import enemies_class_clear

from local_equip import get_equip_values
from local_translator import translate


item = [
    #[")", {"item": "SOFT LEATHER (", "type": ")", "values": [2, 50, 12], "cost": True, "grouping": False}],
    #[")", {"item": "RING MAIL (", "type": ")", "values": [4, 40, 14], "cost": True, "grouping": False}],
    ["]", {"item": "STAFF [", "type": "]", "values": [3, 80, 10], "cost": True, "grouping": False}],
    ["]", {"item": "SMALL SWORD [", "type": "]", "values": [5, 60, 11], "cost": True, "grouping": False}],
    ["]", {"item": "SWORD [", "type": "]", "values": [7, 60, 13], "cost": True, "grouping": False}],
    ["]", {"item": "SPEAR [", "type": "]", "values": [10, 50, 15], "cost": True, "grouping": False}],
    ["*", {"item": "BREAD", "type": "", "values": [1, "BREADS"], "cost": True, "grouping": True}],
    ["*", {"item": "BREAD", "type": "", "values": [1, "BREADS"], "cost": True, "grouping": True}],
    ["*", {"item": "BREAD", "type": "", "values": [1, "BREADS"], "cost": True, "grouping": True}],
    ["?", {"item": "POTION", "type": "", "values": [1, "POTIONS"], "cost": 50, "grouping": True}],
    ["?", {"item": "POTION", "type": "", "values": [1, "POTIONS"], "cost": 50, "grouping": True}],
    ["?", {"item": "POTION", "type": "", "values": [1, "POTIONS"], "cost": 50, "grouping": True}],
    ["}", {"item": "BOW {", "type": "}", "values": [5, 50, 11], "cost": 60, "grouping": False}],
    ["}", {"item": "BOW {", "type": "}", "values": [5, 50, 11], "cost": 60, "grouping": False}],
    ["}", {"item": "COMPOSIVE BOW {", "type": "}", "values": [4, 80, 12], "cost": 120, "grouping": False}],
    ["}", {"item": "LONG BOW {", "type": "}", "values": [7, 50, 13], "cost": 100, "grouping": False}],    ]

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
    elist = [["r",4,2,1,1,7,False,[]],["r",4,2,1,1,7,False,[]],["r",4,2,1,1,7,False,[]],["g",5,2,2,1,7,True,[]],["g",5,2,2,2,7,True,[]]] # head "", hp, attack, xp, sleep, hear_range, archer T/F, drop []
    for i in range(p["depth"]-2):
        elist.append(["o",8,2,2,1,7,False,[]])
    for i in range((p["depth"]-2)//5):
        elist.append(["k",8,4,4,1,7,False,[]])
    for i in range(1 if p["lw"] > 7 else 0):
        elist.append(["t",32,4,16,1,7,False,[]])
    i = randint(0, len(item)-1)
    ilist = [item[i][0] + zero3(item_class_init(item[i][0], item[i][1]))]
    for i in range(randint(0, 6)):
        ilist.append("$" + zero3(item_class_init("$", randint(1, 39))))
    for i in range(choice([0,0,1,2])):
        ilist.append("*" + zero3(item_class_init("*", {"item": "CORPSE", "type": "", "values": [1, "CORPSES"], "cost": 5, "grouping": True})))
    for i in range(randint(0, 2)):
        ilist.append("-" + zero3(item_class_init("-", {"item": "ARROW", "type": "", "values": [randint(2, 5), "ARROWS"], "cost": 5, "grouping": True})))
    for i in range(randint(0, 2)):
        ilist.append("~" + zero3(item_class_init("~", {"item": "TORCH", "type": "", "values": [1, "TORCHES"], "cost": 20, "grouping": True})))
    p["y"], p["x"] = map_init(m, p, ilist, elist, h[0], h[1]) # 0,1,2

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
        "attack_acc": 1,
        "bow_acc": 1,
        "armor_acc": 0,
        "e_attack": {"item": "DAGGER [", "type": "]", "values": [4, 50, 9], "cost": 40, "grouping": False},
        "e_hand": {"item": "SHORT BOW {", "type": "}", "values": [3, 50, 9], "cost": 40, "grouping": False},
        "e_armor": {"item": "CLOTHES (", "type": ")", "values": [0, 50, 8], "cost": 15, "grouping": False},
        "y": 0,
        "x": 0,
        "dy": 0, # direction y -PR-
        "dx": 0,
        "wasattackby": "",
        "echo": "",
        "torch": False,
        "torchtime": 0,
        "starving": False,
        "fullness": 200,
        "arrows_id": -1,
        "BP": [
               #{"item": "ARROW", "type": "", "values": [12, "ARROWS"], "cost": True, "grouping": True},
               #{"item": "TORCH", "type": "", "values": [1, "TORCHES"], "cost": True, "grouping": True},
# no rings for a time! -PR- {"item": "RING |", "type": "|", "values": ["RING OF POWER |", 1], "cost": True, "grouping": False},
               #{"item": "POTION OF HEALING", "type": "", "values": [2, "POTIONS OF HEALING"], "cost": True, "grouping": True}
                ],
        "spells": [
                ["MORE LIGHT 70t (2)",2,"l70"],
                ["MORE LIGHT 30t (1)",1,"l30"]
                ],
        "time": 0,
        "moved": True,
        "id_camp": 0,
        "camp": [[["surface",0],[0,2],[0,3],"next"],
                ["next",[0,3],[0,1],["the-path",0]],
                [["Manipure",0],[2,2],[2,3],[2,3],[2,3],"next","next"],
                [["Manipure",0],[2,3],[2,3],[2,3],[2,3],[2,1],[0,2],[0,3],[0,1]]]
        }
    get_equip_values(p)
    return m, p, path