from random import randint, choice
from local_zero3 import zero3  # or "*" -PR-
from local_map import map_init
from local_item_class import item_class_init, item_class_clear
from local_enemies_class import enemies_class_clear

from local_equip import get_equip_values
from local_translator import translate


item = [
    #  values": [damage, acc, strengh, tier, attacks],
    #[")", {"item": "SOFT LEATHER (", "type": ")", "values": [2, 50, 12], "cost": True, "grouping": False}],
    #[")", {"item": "RING MAIL (", "type": ")", "values": [4, 40, 14], "cost": True, "grouping": False}],
    ["]", {"item": "KNIFE [", "type": "]", "values": [2, 60, 4, 1, 1], "cost": 10, "grouping": False}],
    ["]", {"item": "STAFF [", "type": "]", "values": [2, 80, 5, 1, 1], "cost": 5, "grouping": False}],
    ["]", {"item": "DAGGER [", "type": "]", "values": [3, 60, 4, 2, 1], "cost": 15, "grouping": False}],
    ["]", {"item": "SHORT SWORD [", "type": "]", "values": [5, 40, 5, 2, 1], "cost": 20, "grouping": False}],
    ["]", {"item": "2 KNIFES [", "type": "]", "values": [2, 60, 5, 1, 2], "cost": 20, "grouping": False}],
    ["]", {"item": "CLUB [", "type": "]", "values": [3, 80, 5, 2, 1], "cost": 5, "grouping": False}],
    ["]", {"item": "MACE [", "type": "]", "values": [5, 60, 6, 3, 1], "cost": 30, "grouping": False}],
    ["]", {"item": "2 DAGGERS [", "type": "]", "values": [3, 60, 6, 2, 2], "cost": 30, "grouping": False}],
    ["]", {"item": "RAPIER [", "type": "]", "values": [7, 50, 6, 3, 1], "cost": 35, "grouping": False}],
    ["]", {"item": "SWORD [", "type": "]", "values": [8, 60, 7, 4, 1], "cost": 45, "grouping": False}],
    ["]", {"item": "SPEAR [", "type": "]", "values": [10, 50, 7, 4, 1], "cost": 45, "grouping": False}],
    ["*", {"item": "BREAD", "type": "", "values": [1, "BREADS"], "cost": 20, "grouping": True}],
    ["*", {"item": "BREAD", "type": "", "values": [1, "BREADS"], "cost": 20, "grouping": True}],
    ["*", {"item": "BREAD", "type": "", "values": [1, "BREADS"], "cost": 20, "grouping": True}],
    ["?", {"item": "POTION", "type": "", "values": [1, "POTIONS"], "cost": 50, "grouping": True}],
    #["?", {"item": "POTION", "type": "", "values": [1, "POTIONS"], "cost": 50, "grouping": True}],
    #["?", {"item": "POTION", "type": "", "values": [1, "POTIONS"], "cost": 50, "grouping": True}],
    ["}", {"item": "SLING {", "type": "}", "values": [1, 80, 4, 1, 2], "cost": 60, "grouping": False}],
    ["}", {"item": "BOW {", "type": "}", "values": [3, 60, 5, 1, 1], "cost": 60, "grouping": False}]]
    #["}", {"item": "BOW {", "type": "}", "values": [5, 50, 11], "cost": 60, "grouping": False}],
    #["}", {"item": "COMPOSIVE BOW {", "type": "}", "values": [4, 80, 12], "cost": 120, "grouping": False}],
    #["}", {"item": "LONG BOW {", "type": "}", "values": [7, 50, 13], "cost": 100, "grouping": False}],    ]

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
    enemies = [["r",3,1,1,1,7,False,[]], #0 rat
             ["s",4,2,2,1,7,False,("*", {"item": "CORPSE", "type": "", "values": [1, "CORPSES"], "cost": 5, "grouping": True}, 20)], #1 scrapling
             ["t",4,1,2,1,7,True,("*", {"item": "CORPSE", "type": "", "values": [1, "CORPSES"], "cost": 5, "grouping": True}, 20)], #2 scrapling trapper
             ["g",6,2,4,1,7,False,[]], #3 goblin
             ["S",3,3,3,4,4,False,[]], #4 small snake
             ["o",9,2,6,1,7,False,[]], #5 orck
             ["k",6,2,8,1,7,True,[]], #6 halfing
             ["t",5,3,6,0,14,False,[]], #7 thief
             ["c",18,2,12,1,7,False,[]], #8 crab
             ] # head "", hp, attack, xp, sleep, hear_range, archer T/F,←work drop [], percent, armor?
    elist, xp = [], 0
    for i in range((p["depth"]//2-2 if p["depth"]//2-2 > 0 else 0), p["depth"]//2):
        elist.append(enemies[i])
        xp += enemies[i][3]
    while xp < (3+p["lw"]): #5-2=3 -PR-
        i = randint((p["depth"]//2-2 if p["depth"]//2-2 > 0 else 0), p["depth"]//2)
        elist.append(enemies[i])
        xp += enemies[i][3]
    i = randint(0, len(item)-1)
    ilist = [item[i][0] + zero3(item_class_init(item[i][0], item[i][1]))]
    for i in range(randint(0, 6)):
        ilist.append("$" + zero3(item_class_init("$", randint(1, 39))))
    for i in range(choice([0,0,1,2])):
        ilist.append("*" + zero3(item_class_init("*", {"item": "CORPSE", "type": "", "values": [1, "CORPSES"], "cost": 5, "grouping": True})))
    for i in range(randint(0, 2)):
        ilist.append("-" + zero3(item_class_init("-", {"item": "ARROW", "type": "", "values": [randint(2, 5), "ARROWS"], "cost": 5, "grouping": True})))
    for i in range(randint(0, 3)):
        ilist.append("~" + zero3(item_class_init("~", {"item": "TORCH", "type": "", "values": [1, "TORCHES"], "cost": 10, "grouping": True})))
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
        "maxhp": 5,
        "hp": 5,
        "hpchange": 1,
        "hpcounter": 10,
        "needxp": 6,
        "xp": 0,
        "lw": 1,
        "depth": 0,
        "strength": 4,
        "gold": 0,
        "attack": 1,
        "bow": 1,
        "armor": 0,
        "attack_acc": 1,
        "bow_acc": 1,
        "armor_acc": 0,
        "attack_attacks": 1,
        "bow_attacks": 1,
        "e_attack": {"item": "KNIFE [", "type": "]", "values": [2, 60, 4, 1, 1], "cost": 10, "grouping": False},
        "e_hand": {"item": "SHOTING LEATHER {", "type": "}", "values": [1, 60, 4, 1, 1], "cost": 5, "grouping": False},
        "e_armor": {"item": "CLOTHES (", "type": ")", "values": [0, 50, 3, 1, 1], "cost": 5, "grouping": False},
        "y": 0,
        "x": 0,
        "dy": 0, # direction y -PR-
        "dx": 0,
        "wasattackby": "",
        "echo": "",
        "torch": True,
        "torchtime": 50,
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
        "camp": [[["surface",0],[2,2],[2,3],[1,3],[0,3],[0,3],[0,3],[1,3],[2,3],[2,3],[2,3],[1,3],[0,3],[0,3],[1,3],[2,3],[1,3],[0,3],[0,3],[1,3],"next"],
                ["next",[0,3],[0,1],["the-path",0]],
                [["Manipure",0],[2,2],[2,3],[2,3],[2,3],"next","next"],
                [["Manipure",0],[2,3],[2,3],[2,3],[2,3],[2,1],[0,2],[0,3],[0,1]]]
        }
    get_equip_values(p)
    return m, p, path