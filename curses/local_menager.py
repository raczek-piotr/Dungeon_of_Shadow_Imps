from random import randint, choice
#from time import sleep
from local_scripts import zero3  # or "*" -PR-
from local_map import map_init
from local_item_class import item_class_init, item_class_clear
from local_enemies_class import enemies_class_clear

from local_equip import get_equip_values
from local_translator import translate


item = [
    #  values": [damage, acc, [str|dex], tier, attacks],
    #["]", {"item": "KNIFE [", "type": "]", "values": [2, 60, [2,2], 1, 1], "cost": 12, "grouping": False}],
    #["]", {"item": "2 KNIFES [", "type": "]", "values": [2, 60, [2,6], 1, 2], "cost": 24, "grouping": False}],

    ["]", {"item": "LONG KNIFE [", "type": "]", "values": [3, 60, [2,5], 1, 1], "cost": 18, "grouping": False}], # Rogue base weapons -PR-
    ["]", {"item": "2 KNIFES [", "type": "]", "values": [2, 60, [3,5], 1, 2], "cost": 24, "grouping": False}],
    ["]", {"item": "SHORT DAGGER [", "type": "]", "values": [4, 75, [4,6], 1, 1], "cost": 30, "grouping": False}],
    ["]", {"item": "DAGGER [", "type": "]", "values": [5, 78, [5,7], 1, 1], "cost": 39, "grouping": False}],
    ["]", {"item": "LONG DAGGER [", "type": "]", "values": [6, 80, [6,8], 1, 1], "cost": 48, "grouping": False}],

    ["]", {"item": "CLUB [", "type": "]", "values": [7, 30, [4,3], 1, 1], "cost": 21, "grouping": False}], # Bandit base weapons -PR-
    ["]", {"item": "WOODEN CLUB [", "type": "]", "values": [10, 33, [6,4], 1, 1], "cost": 33, "grouping": False}],
    ["]", {"item": "MACE [", "type": "]", "values": [8, 30, [7,5], 1, 2], "cost": 48, "grouping": False}],
    ["]", {"item": "FLAIL [", "type": "]", "values": [7, 30, [8,6], 1, 3], "cost": 63, "grouping": False}],

    ["]", {"item": "SHOVEL [", "type": "]", "values": [3, 50, [4,2], 1, 1], "cost": 15, "grouping": False}], # for all  -PR-
    ["]", {"item": "SICKLE [", "type": "]", "values": [2, 70, [2,4], 1, 1], "cost": 14, "grouping": False}],

    ["]", {"item": "PUGINALE [", "type": "]", "values": [6, 40, [6,2], 1, 1], "cost": 24, "grouping": False}], # Warrior base weapons -PR-
    ["]", {"item": "SPEAR [", "type": "]", "values": [11, 30, [7,3], 1, 1], "cost": 33, "grouping": False}],
    ["]", {"item": "PIKE [", "type": "]", "values": [16, 30, [8,4], 1, 1], "cost": 48, "grouping": False}],
    ["]", {"item": "HALBEARD [", "type": "]", "values": [22, 30, [9,5], 1, 1], "cost": 66, "grouping": False}],

    ["]", {"item": "HAND AXE [", "type": "]", "values": [3, 60, [5,2], 1, 1], "cost": 18, "grouping": False}], # help W+B -PR-
    ["]", {"item": "AXE [", "type": "]", "values": [5, 60, [6,3], 2, 1], "cost": 30, "grouping": False}],
    ["]", {"item": "HAEVY AXE [", "type": "]", "values": [8, 60, [7,4], 3, 1], "cost": 48, "grouping": False}],
    ["]", {"item": "BROAD AXE [", "type": "]", "values": [10, 60, [8,5], 4, 1], "cost": 60, "grouping": False}],
    ["]", {"item": "BATTLE AXE [", "type": "]", "values": [10, 60, [8,5], 4, 1], "cost": 60, "grouping": False}],

    ["]", {"item": "SHORT SWORD [", "type": "]", "values": [8, 40, [6,3], 1, 1], "cost": 32, "grouping": False}], # help W+B -PR-
    ["]", {"item": "SWORD [", "type": "]", "values": [12, 40, [7,4], 2, 1], "cost": 48, "grouping": False}],
    ["]", {"item": "LONG SWORD [", "type": "]", "values": [15, 40, [8,5], 3, 1], "cost": 60, "grouping": False}],
    ["]", {"item": "GREAT SWORD [", "type": "]", "values": [16, 40, [9,5], 4, 1], "cost": 64, "grouping": False}],

    ["]", {"item": "FOIL [", "type": "]", "values": [2, 60, [4,4], 1, 2], "cost": 24, "grouping": False}], # Duelist base weapons -PR-
    ["]", {"item": "RAPIER [", "type": "]", "values": [2, 55, [5,5], 1, 3], "cost": 33, "grouping": False}],
    ["]", {"item": "SABRE [", "type": "]", "values": [3, 50, [6,6], 1, 3], "cost": 45, "grouping": False}],
    ["]", {"item": "KATANA [", "type": "]", "values": [7, 40, [7,7], 2, 2], "cost": 56, "grouping": False}],

    #["*", {"item": "BREAD", "type": "", "values": [1, "BREADS"], "cost": 50, "grouping": True}],
    #["?", {"item": "POTION", "type": "", "values": [1, "POTIONS"], "cost": 50, "grouping": True}],
    #["?", {"item": "POTION", "type": "", "values": [1, "POTIONS"], "cost": 50, "grouping": True}],
    #["?", {"item": "POTION", "type": "", "values": [1, "POTIONS"], "cost": 50, "grouping": True}],
    #["?", {"item": "POTION", "type": "", "values": [1, "POTIONS"], "cost": 50, "grouping": True}],
    #["?", {"item": "POTION", "type": "", "values": [1, "POTIONS"], "cost": 50, "grouping": True}],
    #["?", {"item": "POTION", "type": "", "values": [1, "POTIONS"], "cost": 50, "grouping": True}],

    #["}", {"item": "SLING {", "type": "}", "values": [2, 60, [3,4], 1, 1], "cost": 15, "grouping": False}],
    ["}", {"item": "SHORT BOW {", "type": "}", "values": [3, 60, [2,6], 1, 1], "cost": 18, "grouping": False}], # Archer base weapons -PR-
    ["}", {"item": "BOW {", "type": "}", "values": [5, 60, [3,7], 2, 1], "cost": 30, "grouping": False}],
    ["}", {"item": "REFLEXIVE BOW {", "type": "}", "values": [8, 60, [4,8], 3, 1], "cost": 48, "grouping": False}],
    ["}", {"item": "LONGBOW {", "type": "}", "values": [11, 60, [5,9], 4, 1], "cost": 66, "grouping": False}],
    ["}", {"item": "HAND CROSBOW {", "type": "}", "values": [3, 40, [5,3], 1, 1], "cost": 12, "grouping": False}],
    ["}", {"item": "CROSBOW {", "type": "}", "values": [8, 40, [7,7], 4, 1], "cost": 32, "grouping": False}],

    #[")", {"item": "SOFT LEATHER (", "type": ")", "values": [2, 50, 12], "cost": True, "grouping": False}],
    #[")", {"item": "RING MAIL (", "type": ")", "values": [4, 40, 14], "cost": True, "grouping": False}],
    #["]", {"item": "2 DAGGERS [", "type": "]", "values": [3, 60, 6, 2, 2], "cost": 30, "grouping": False}],
    #["}", {"item": "BOW {", "type": "}", "values": [5, 50, 11], "cost": 60, "grouping": False}],
    #["}", {"item": "COMPOSIVE BOW {", "type": "}", "values": [4, 80, 12], "cost": 120, "grouping": False}],
    #["}", {"item": "LONG BOW {", "type": "}", "values": [7, 50, 13], "cost": 100, "grouping": False}],
    ]

enemies_likes_light = [
    ["r",4,1,1,1,7,False,[]], #0 rat
    ["h",4,2,2,1,7,False,[]],#1 hobbit
    ["a",4,2,3,1,7,True,[]],#2 archer
    ["k",8,2,4,1,7,False,[]], #3 kobold
    ["t",5,5,6,1,7,False,[]], #4 thief
    ]#"head", hp, attack, xp, sleep, hear_range, archer Throw/Fight, (←work) max lw to give xp, drop([] percent), armor?
enemies_half_light = [
    ["r",4,1,1,1,7,False,[]], #0 rat
    ["c",8,1,2,1,7,False,[]], #1 crab
    ["z",3,4,3,1,7,False,[]],#2 zombe
    ["k",8,2,4,1,7,False,[]], #3 kobold
    ["t",5,5,6,1,7,False,[]], #4 thief
    ]#"head", hp, attack, xp, sleep, hear_range, archer Throw/Fight, (←work) max lw to give xp, drop([] percent), armor?
enemies_not_light = [
    ["s",3,3,1,4,4,False,[]], #0 small snake
    ["c",8,1,2,1,7,False,[]], #1 crab
    ["z",3,4,3,1,7,False,[]],#2 zombe
    ["g",6,2,4,1,7,True,[]], #3 goblin
    ["o",9,2,6,1,7,False,[]], #4 orck
    ]#"head", hp, attack, xp, sleep, hear_range, archer Throw/Fight, (←work) max lw to give xp, drop([] percent), armor?

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
    w.addstr(2, 37, "0.0.G", c.color_pair(4))
    #sleep(0.5)
    #w.refresh() # w.getkey() makes the same + ... -PR-
    w.addstr(4, 2, "1 - HUMAN WARRIOR", c.color_pair(1))
    w.addstr(5, 2, "2 - HUMAN BANDIT", c.color_pair(1))
    w.addstr(6, 2, "3 - HUMAN DUELIST", c.color_pair(1))
    w.addstr(7, 2, "4 - HUMAN ROGUE", c.color_pair(1))
    w.addstr(8, 2, "5 - HUMAN ARCHER", c.color_pair(1))
    #w.addstr(9, 2, "6 - ELF WARRIOR", c.color_pair(2))
    #w.addstr(8, 2, "5 - ELF SERGEANT", c.color_pair(2))
    #w.addstr(9, 2, "6 - ELF ROUGE", c.color_pair(2))
    #w.addstr(10, 2, "7 - HALFING WARRIOR", c.color_pair(3))
    #w.addstr(11, 2, "8 - HALFING SERGEANT", c.color_pair(3))
    #w.addstr(12, 2, "9 - HALFING ROUGE", c.color_pair(3))
    #w.addstr(13, 2, "/ - FUDIT WARRIOR", c.color_pair(4))
    #w.addstr(14, 2, "* - FUDIT SERGEANT", c.color_pair(4))
    #w.addstr(15, 2, "- - FUDIT ROUGE", c.color_pair(4))
    #w.addstr(16, 2, "+ - HOBBIT WARRIOR", c.color_pair(5))
    #.addstr(17, 2, ", - HOBBIT SERGEANT", c.color_pair(5))
    #w.addstr(18, 2, "0 - HOBBIT ROUGE", c.color_pair(5))
    if w.getmaxyx() != (24,80):
        w.addstr(23, 3, "The screen could't resize it self! (24x80)", c.color_pair(2))
        w.addstr(22, 79, "|", c.color_pair(3))
        w.addstr(23, 71, "point ->", c.color_pair(3))
    while True:
        match w.getkey():
            case "1":
                p["strength"] = 6
                p["dexterity"] = 2
                p["playertype"] = "HUMAN WARRIOR"
                break
            case "2":
                p["strength"] = 5
                p["dexterity"] = 3
                p["playertype"] = "HUMAN BANDIT"
                break
            case "3":
                #p["playertype"] = "HUMAN DUELIST"
                break
            case "4":
                p["strength"] = 3
                p["dexterity"] = 5
                p["playertype"] = "HUMAN ROUGE"
                break
            case "5":
                p["strength"] = 2
                p["dexterity"] = 6
                p["playertype"] = "HUMAN ARCHER"
                p["BP"].append({"item": "ARROW", "type": "", "values": [40, "ARROWS"], "cost": 5, "grouping": True})
                p["arrows_id"] = 1
                break
            case _:
                pass
    w.clear()
    w.addstr(5, 5, "The angel of the LORD came back a second time and touched you and said:", c.color_pair(5))
    w.addstr(6, 13, '"Get up and eat, for the journey is too much for you."', c.color_pair(1))
    w.addstr(23, 67, "1 KINGS 19:7", c.color_pair(5))
    w.getkey()
    global item
    i = 0
    while i < len(item):
        t = item[i][1]["values"][2]
        if t[0] > p["strength"]+3 or t[1] > p["dexterity"]+3:
            item.pop(i)
        else:
            i += 1

def prepare_map(m, p):
    h = p["camp"][p["id_camp"]][p["depth"]].copy()
    while h == "next": # not used -PR-
        p["id_camp"] += 1
        h = p["camp"][p["id_camp"]][p["depth"]]
    if h[0] == "?":
        h[0] = p["type"]
        i = randint(-1, 1)
        if p["type"] + i in {0,1,2,3}:
            p["type"] += i
    item_class_clear()
    enemies_class_clear()
    elist, ilist, xp = [], [], 0
    for _ in range(randint(0, 5)):
        i = randint(0, len(item)-1)
        ilist.append(item[i][0] + zero3(item_class_init(item[i][0], item[i][1].copy())))
    if type(h[0]) == int:
        p["normal_level"] = h[0] < 100 # needs are disable/enable -PR-
        if p["normal_level"]:
            #global enemies_likes_light, enemies_half_light, enemies_not_light
            enemies = [enemies_likes_light, enemies_half_light, enemies_not_light, enemies_half_light]
            enemies = enemies[h[0]%4]
            t = (p["depth"]//2-2 if p["depth"]//2-2 > 0 else 0) #min_range -PR-
            for i in range(t, p["depth"]//2):
                elist.append(enemies[i])
                xp += enemies[i][3]
            while xp < (4+2*p["depth"]): #difficulty -PR-
                i = randint(t, p["depth"]//2)
                elist.append(enemies[i])
                xp += enemies[i][3]
            for i in range(randint(0, 5)):
                ilist.append("$" + zero3(item_class_init("$", randint(1, 39))))
            for i in range(choice([0,0,1,2])):
                ilist.append("*" + zero3(item_class_init("*", {"item": "CORPSE", "type": "", "values": [1, "CORPSES"], "cost": 5, "grouping": True})))
            for i in range(randint(0, 2)):
                ilist.append("-" + zero3(item_class_init("-", {"item": "ARROW", "type": "", "values": [randint(2, 5), "ARROWS"], "cost": 5, "grouping": True})))
            for i in range(randint(0, 1)):
                ilist.append("~" + zero3(item_class_init("~", {"item": "TORCH", "type": "", "values": [1, "TORCHES"], "cost": 10, "grouping": True})))
        else:
            enemies = [enemies_likes_light, enemies_half_light, enemies_not_light,]
    p["y"], p["x"] = map_init(m, p, ilist, elist, h[0], h[1]) # 0,1,2,3

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
        "playertype": "Human Duelist",
        "specials": "", # not used -PR-
        "normal_level": True,
        #"name": "qwe",#at the death
        "maxhp": 10,
        "hp": 10,
        "hpchange": 2,
        "hpcounter": 10,
        "needxp": 20,
        "xp": 0,
        "lw": 1,
        "depth": 0,
        "strength": 4,
        "dexterity": 4,
        "gold": 0,
        "attack": 1,
        "bow": 1,
        "armor": 0,
        "attack_acc": 1,
        "bow_acc": 1,
        "armor_acc": 0,
        "attack_attacks": 1,
        "bow_attacks": 1,
        "e_attack": {"item": "KNIFE [", "type": "]", "values": [2, 60, [2,2], 1, 1], "cost": 12, "grouping": False},
        "e_hand": {"item": "SLING {", "type": "}", "values": [1, 60, [2,2], 1, 1], "cost": 6, "grouping": False},
        "e_armor": {"item": "CLOTHES (", "type": ")", "values": [0, 50, [2,2], 1, 1], "cost": 10, "grouping": False},
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
        "time": 0,
        "moved": True,
        "id_camp": 0,
        "type": 1, # type of dungeon -PR-
        "camp": [[["surface",0],["?",2],["?",3],["?",3],["?",3],["?",3],["?",3],["?",3],["?",3],["?",3],[100,3],["?",3],["?",3],["?",3],["?",3],["?",3]],
        #        ["next",[0,3],[0,1],["the-path",0]],
        #        [["Manipure",0],[2,2],[2,3],[2,3],[2,3],"next","next"],
                [["Manipure",0],[2,3],[2,3],[2,3],[2,3],[2,1],[0,2],[0,3],[0,1]]]
        #"camp": [[[3,2],[1,3],[0,3],[0,3],[0,3],[1,3],[2,3],[2,3],[2,3],[1,3],[0,3],[0,3],[1,3],[2,2]],
        #        [["Manipure",0],[2,2],[2,3],[2,3],[2,3],"next","next"],
        #        [["Manipure",0],[2,3],[2,3],[2,3],[2,3],[2,1],[0,2],[0,3],[0,1]]]
        }
    get_equip_values(p)
    return m, p, path
