from random import randint, choice
from local_scripts import zero3  # or "*" -PR-
from local_map import map_init
from local_item_class import item_class_init, item_class_clear
from local_enemies_class import enemies_class_clear

from local_equip import get_equip_values
from local_translator import translate


item = [
    #  values": [damage, acc, strengh, tier, attacks],
    ["]", {"item": "KNIFE [", "type": "]", "values": [2, 60, [3,3], 1, 1], "cost": 12, "grouping": False}],
    ["]", {"item": "2 KNIFES [", "type": "]", "values": [2, 60, [3,5], 1, 2], "cost": 24, "grouping": False}],
    ["]", {"item": "DAGGER [", "type": "]", "values": [5, 80, [4,6], 1, 1], "cost": 40, "grouping": False}],
    ["]", {"item": "2 DAGGERS [", "type": "]", "values": [5, 80, [5,7], 1, 2], "cost": 80, "grouping": False}],
    ["]", {"item": "ASSASIN BLADES [", "type": "]", "values": [8, 80, [6,8], 1, 2], "cost": 128, "grouping": False}],

    ["]", {"item": "SHORT SWORD [", "type": "]", "values": [7, 50, [5,5], 2, 1], "cost": 35, "grouping": False}],
    ["]", {"item": "SWORD [", "type": "]", "values": [11, 50, [6,6], 3, 1], "cost": 55, "grouping": False}],

    ["]", {"item": "PUGINALE [", "type": "]", "values": [4, 42, [5,3], 1, 1], "cost": 21, "grouping": False}],
    ["]", {"item": "SPEAR [", "type": "]", "values": [18, 30, [7,5], 3, 1], "cost": 54, "grouping": False}],
    ["]", {"item": "HAEVY SPEAR [", "type": "]", "values": [40, 30, [8,6], 4, 1], "cost": 120, "grouping": False}],

    ["]", {"item": "HAND AXE [", "type": "]", "values": [3, 60, [4,4], 1, 1], "cost": 18, "grouping": False}],
    ["]", {"item": "AXE [", "type": "]", "values": [6, 58, [5,5], 2, 1], "cost": 35, "grouping": False}],
    ["]", {"item": "HAEVY AXE [", "type": "]", "values": [9, 61, [6,6], 3, 1], "cost": 55, "grouping": False}],
    ["]", {"item": "BATTLE AXE [", "type": "]", "values": [20, 65, [7,7], 4, 1], "cost": 130, "grouping": False}],

    ["]", {"item": "SICKLE [", "type": "]", "values": [4, 50, [4,4], 1, 1], "cost": 20, "grouping": False}],

    ["*", {"item": "BREAD", "type": "", "values": [1, "BREADS"], "cost": 50, "grouping": True}],
    ["?", {"item": "POTION", "type": "", "values": [1, "POTIONS"], "cost": 50, "grouping": True}],
    ["?", {"item": "POTION", "type": "", "values": [1, "POTIONS"], "cost": 50, "grouping": True}],
    ["?", {"item": "POTION", "type": "", "values": [1, "POTIONS"], "cost": 50, "grouping": True}],
    ["?", {"item": "POTION", "type": "", "values": [1, "POTIONS"], "cost": 50, "grouping": True}],
    ["?", {"item": "POTION", "type": "", "values": [1, "POTIONS"], "cost": 50, "grouping": True}],
    ["?", {"item": "POTION", "type": "", "values": [1, "POTIONS"], "cost": 50, "grouping": True}],

    #["}", {"item": "SLING {", "type": "}", "values": [2, 60, [3,4], 1, 1], "cost": 15, "grouping": False}],
    ["}", {"item": "SHORT BOW {", "type": "}", "values": [3, 60, [4,4], 1, 1], "cost": 18, "grouping": False}],
    ["}", {"item": "HAND CROSBOW {", "type": "}", "values": [4, 30, [5,3], 1, 1], "cost": 12, "grouping": False}],
    ["}", {"item": "BOW {", "type": "}", "values": [4, 70, [5,5], 2, 1], "cost": 28, "grouping": False}],
    ["}", {"item": "LIGHT CROSBOW {", "type": "}", "values": [6, 30, [6,4], 2, 1], "cost": 18, "grouping": False}],
    ["}", {"item": "LONGBOW {", "type": "}", "values": [5, 60, [5,7], 3, 1], "cost": 35, "grouping": False}],
    ["}", {"item": "CROSBOW {", "type": "}", "values": [12, 30, [7,5], 3, 1], "cost": 36, "grouping": False}],
    [")", {"item": "HELMET (", "type": ")", "values": [1, 50, [6,4], 1, 1], "cost": 10, "grouping": False},],
    [")", {"item": "SHIELD (", "type": ")", "values": [2, 50, [8,6], 2, 1], "cost": 20, "grouping": False},],
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

def menager(command = "#R", m = {}, p = {}): # #E - end game #R - try to reload or start, #S - save, #U - go up, #D - go down -PR-
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
            prepare_map(m, p)
            return m, p, path


def prepare_map(m, p):
    h = p["camp"][p["id_camp"]][p["depth"]]
    while h == "next":
        p["id_camp"] += 1
        h = p["camp"][p["id_camp"]][p["depth"]]
    h[0] = choice(h[0])
    item_class_clear()
    enemies_class_clear()
    i = randint(0, len(item)-1)
    elist, ilist, xp = [], [item[i][0] + zero3(item_class_init(item[i][0], item[i][1]))], 0
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
            for i in range(randint(0, 6)):
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
        "playertype": "Human Powder Monkey",
        "specials": "", # not used -PR-
        "normal_level": True,
        "name": "qwe",
        "manacounter": 75,
        "maxhp": 10,
        "hp": 10,
        "hpchange": 1,
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
        "e_attack": {"item": "KNIFE [", "type": "]", "values": [2, 60, [3,3], 1, 1], "cost": 10, "grouping": False},
        "e_hand": {"item": "GLOVE {", "type": "}", "values": [1, 60, [3,3], 1, 1], "cost": 5, "grouping": False},
        "e_armor": {"item": "CLOTHES (", "type": ")", "values": [0, 50, [3,3], 1, 1], "cost": 5, "grouping": False},
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
        "camp": [[[["surface"],0],[[0,1],2],[[0],3],[[0,1],3],[[1],3],[[1,2],3],[[2],3],[[2,3],3],[[3],3],[[2,3],3],[[100],3],[[1],3],[[0,1],3],[[0,1],3],[[1],3],[[2],3],[[1],3],[[0],3],[[0],3],[[1],3],"next"],
        #        ["next",[0,3],[0,1],["the-path",0]],
        #        [["Manipure",0],[2,2],[2,3],[2,3],[2,3],"next","next"],
                [["Manipure",0],[2,3],[2,3],[2,3],[2,3],[2,1],[0,2],[0,3],[0,1]]]
        #"camp": [[[3,2],[1,3],[0,3],[0,3],[0,3],[1,3],[2,3],[2,3],[2,3],[1,3],[0,3],[0,3],[1,3],[2,2]],
        #        [["Manipure",0],[2,2],[2,3],[2,3],[2,3],"next","next"],
        #        [["Manipure",0],[2,3],[2,3],[2,3],[2,3],[2,1],[0,2],[0,3],[0,1]]]
        }
    get_equip_values(p)
    return m, p, path
