from local_item_class import get_item, change_item
from random import randint
from local_scores import scoreboard_print
from local_iostream import loadgame
from os.path import isfile


version = "DoSI_0.5.1"

def character(w, c, p):
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
        "classicgame": True,
        "color": 1,
        "normal_level": True,
        "shift_type_of": 0,#at the depth -PR-
        "skill": 1,
        "maxeat": 3500,
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
        "inteligence": 0,
        "magic_list": False,
        "cur_magic": 0, # like „anty-mana” -PR-
        "gold": 200,
        "armor": 0,
        "basedefend": 50,
        "defend": 0,
        #defend_name": "",
        "attack": 1,
        "attack_acc": 1,
        "attack_damage": 1,
        "attack_hits": 1,
        #"attack_name": "",
        "bow": 1,
        "bow_acc": 1,
        "bow_damage": 1,
        "bow_hits": 1,
        #"hand_name": "1D1 1H60%",
        "e_attack": get_item(24),
        "e_hand": get_item(51),
        "e_armor": get_item(16),
        "blessing": 0,
        "fury": 0,
        "iniciative": 0,
        "y": 0,
        "x": 0,
        "dy": 0, # direction (movement or attack) y -PR-
        "dx": 0,
        "ismage": False,
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
            ],
        "time": 0,
        "moved": True,
        "id_camp": 0,
        "environment": [0, 0, 0, 0],
        "environment_bonus": 0,
        "type": 1, # type of dungeon -PR-
        "_type": 0,
        "camp": [[["surface",0],[0,3],[0,3],[0,3],[0,3],[0,3],[0,3],[0,3],[0,3],[12,3],
                  ["fudit_village",2],[12,3],[12,3],[12,3],[1,3],[1,3],[1,3],[1,3],[1,3],[11,3],
                  ["stonehouse",3],[11,3],[1,3],[1,3],[1,3],[1,3],[1,3],[1,3],[1,3],[13,3],
                  ["gate",1],[13,3],[2,3],[2,3],[2,3],[2,3],[2,3],[2,3],[2,3],[2,3],["thebook",3],
                  [],]
                ]
        }

    while True:
        w.clear() # ? -PR-
        w.addstr(0, 30, "DUNGEON OF SHADOW IMPS", c.color_pair(2))
        w.addstr(1, 25, "SELECT A CHARACTER TO PLAY WITH", c.color_pair(1))
        w.addstr(2, 35, version, c.color_pair(4))
        w.addstr(3, 2, "SELECT A RACE:", c.color_pair(4))
        w.addstr(5, 2, "1 - HUMAN", c.color_pair(1))
        w.addstr(6, 2, "THE MOST VARIOUS RACE IN THE GAME. THEY LIVE ON THE SURFACE", c.color_pair(1))
        w.addstr(8, 2, "2 - FUDISH", c.color_pair(2))
        w.addstr(9, 2, "FONGUS-LOOKING MONSTERS THAT LIVE IN THE WET PARTS OF THE DUNGEON", c.color_pair(2))
        w.addstr(11, 2, "3 - DWARF", c.color_pair(6))
        w.addstr(12, 2, "GOOD MELEE FIGHTERS. BUT NO ONE KNOWS WHERE THEY COME FROM", c.color_pair(6))
        w.addstr(14, 2, "4 - IMP", c.color_pair(3))
        w.addstr(15, 2, "THEY ARE FROM THE BOTTOM OF THE WORLD, THEY KNEW THE WORLD WELL", c.color_pair(3))
        w.addstr(17, 2, "5 - ALGAL", c.color_pair(7))
        w.addstr(18, 2, "THEY LOOK WEAK, LIKE ALGS. THEY TRAVEL AS APPRENTICE. WHO THEY ARE?", c.color_pair(7))
        w.addstr(20, 2, "6 - GNOME", c.color_pair(5))
        w.addstr(21, 2, "HOW HAD YOU OPENED THE DOOR AND KILL THESE RATS?", c.color_pair(5))
        w.addstr(23, 2, "7 - VIEW SCOREBOARD", c.color_pair(4))
        if isfile("save.txt"):
            w.addstr(23, 42, "8 - LOAD SAVED GAME", c.color_pair(4))
        if w.getmaxyx() != (24,80):
            w.addstr(22, 35, "The screen could't resize it self! (24x80)", c.color_pair(1))
            w.addstr(22, 79, "|", c.color_pair(1))
            w.addstr(23, 71, "point --", c.color_pair(1))
        match w.getkey():
            case "1":
                if human(w, c, p):
                    break
            case "2":
                if fudish(w, c, p):
                    break
            case "3":
                if dwarf(w, c, p):
                    break
            case "4":
                if imp(w, c, p):
                    break
            case "5":
                if algal(w, c, p):
                    break
            case "6":
                if gnome(w, c, p):
                    break
            case "7":
                scoreboard_print(w, c)
            case "8":
                t = loadgame()
                if t:
                    return m, t, path
            case _:
                pass
    return m, p, path

def human(w, c, p):
    w.clear()
    w.addstr(0, 30, "DUNGEON OF SHADOW IMPS", c.color_pair(2))
    w.addstr(1, 25, "SELECT A CHARACTER TO PLAY WITH", c.color_pair(1))
    w.addstr(2, 35, version, c.color_pair(4))
    w.addstr(4, 2, "THE MOST VARIOUS RACE IN THE GAME. THEY LIVE ON THE SURFACE", c.color_pair(1))
    w.addstr(5, 2, "CLASSES (HUMAN):", c.color_pair(4))
    w.addstr(7, 2, "1 - HUMAN WARRIOR", c.color_pair(1))
    w.addstr(9, 2, "2 - HUMAN BANDIT", c.color_pair(1))
    w.addstr(11, 2, "3 - HUMAN DUELIST", c.color_pair(1))
    w.addstr(13, 2, "4 - HUMAN ROGUE", c.color_pair(1))
    w.addstr(15, 2, "5 - HUMAN ARCHER", c.color_pair(1))
    w.addstr(7, 42, "6 - HUMAN PALADIN", c.color_pair(1))
    w.addstr(9, 42, "7 - HUMAN WATER MAGE", c.color_pair(1))
    w.addstr(11, 42, "8 - HUMAN WIZARD", c.color_pair(1))
    w.refresh()
    while True:
        q = w.getkey()
        match q:
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
                p["BP"].append(get_item(1)[:2] + [25] + get_item(1)[3:])
                break
            case "6":
                p["strength"] = 9
                p["dexterity"] = 8
                p["inteligence"] = 10
                p["playertype"] = "HUMAN PALADIN"
                p["e_hand"] = get_item(65)
                p["BP"] = [get_item(6),get_item(7)]
                p["classicgame"] = False
                break
            case "7":
                p["ismage"] = True
                p["strength"] = 7
                p["dexterity"] = 7
                p["inteligence"] = 12
                p["playertype"] = "HUMAN WATER MAGE"
                p["e_hand"] = get_item(63)
                p["BP"] = [get_item(6),get_item(7)]
                p["classicgame"] = False
                break
            case "8":
                p["ismage"] = True
                p["strength"] = 7
                p["dexterity"] = 7
                p["inteligence"] = 12
                p["playertype"] = "HUMAN WIZARD"
                p["e_hand"] = get_item(64)
                p["BP"] = [get_item(6),get_item(7)]
                p["classicgame"] = False
                break
            case _:
                #if q in {"PADENTER","\n", ",", "\x1b", "0"}:
                    return False
    p["gold"] = 350
    p["environment"] = [1, 1, 1, 0]
    item = change_item(8)[1]
    item[-2] = True
    item[0] = ['SCROLL OF IDENTIFY', 2, 0]
    return True

def fudish(w, c, p):
    w.clear()
    w.addstr(0, 30, "DUNGEON OF SHADOW IMPS", c.color_pair(2))
    w.addstr(1, 25, "SELECT A CHARACTER TO PLAY WITH", c.color_pair(1))
    w.addstr(2, 35, version, c.color_pair(4))
    w.addstr(4, 2, "FONGUS-LOOKING MONSTERS THAT LIVE IN THE WET PARTS OF THE DUNGEON", c.color_pair(2))
    w.addstr(5, 2, "CLASSES (FUDISH):", c.color_pair(4))
    w.addstr(7, 2, "1 - FUDISH WARRIOR", c.color_pair(2))
    w.addstr(9, 2, "2 - FUDISH BANDIT", c.color_pair(2))
    w.addstr(11, 2, "3 - FUDISH DUELIST", c.color_pair(2))
    w.addstr(13, 2, "4 - FUDISH ROGUE", c.color_pair(2))
    w.addstr(15, 2, "5 - FUDISH ARCHER", c.color_pair(2))
    w.refresh()
    while True:
        q = w.getkey()
        match q:
            case "2":
                p["strength"] = 11
                p["dexterity"] = 7
                p["playertype"] = "FUDISH WARRIOR"
                break
            case "2":
                p["strength"] = 10
                p["dexterity"] = 8
                p["playertype"] = "HUMAN BANDIT"
                break
            case "3":
                #p["strength"] = 9
                #p["dexterity"] = 9
                p["playertype"] = "FUDISH DUELIST"
                break
            case "4":
                p["strength"] = 8
                p["dexterity"] = 10
                p["playertype"] = "FUDISH ROGUE"
                break
            case "5":
                p["strength"] = 7
                p["dexterity"] = 11
                p["playertype"] = "FUDISH ARCHER"
                p["BP"].append(get_item(1)[:2] + [25] + get_item(1)[3:])
                break
            case _:
                #if q in {"PADENTER","\n", ",", "\x1b", "0"}:
                    return False
    p["color"] = 2
    p["environment"] = [0, 3, 0, 0]
    p["basedefend"] = 60
    p["reg_time"] = 12
    p["maxeat"] = 5000
    item = change_item(9)[1]
    item[-2] = True
    item[0] = ['SCROLL OF TELEPORTATION', 2, 1]
    return True

def dwarf(w, c, p):
    w.clear()
    w.addstr(0, 30, "DUNGEON OF SHADOW IMPS", c.color_pair(2))
    w.addstr(1, 25, "SELECT A CHARACTER TO PLAY WITH", c.color_pair(1))
    w.addstr(2, 35, version, c.color_pair(4))
    w.addstr(4, 2, "GOOD MELEE FIGHTERS. BUT NO ONE KNOWS WHERE THEY COME FROM", c.color_pair(6))
    w.addstr(5, 2, "CLASSES (DWARF):", c.color_pair(4))
    w.addstr(7, 2, "1 - DWARWISH STEELCLAD", c.color_pair(6))
    w.addstr(9, 2, "2 - DWARWISH MINER", c.color_pair(6))
    w.addstr(11, 2, "3 - DWARWISH SCOUT", c.color_pair(6))
    w.refresh()
    while True:
        q = w.getkey()
        match q:
            case "1":
                p["strength"] = 11
                p["dexterity"] = 7
                p["playertype"] = "DWARWISH STEELCLAD"
                p["e_attack"] = get_item(25)
                break
            case "2":
                p["strength"] = 10
                p["dexterity"] = 8
                p["playertype"] = "DWARWISH MINER"
                p["e_attack"] = get_item(28)
                break
            case "3":
                #p["strength"] = 9
                #p["dexterity"] = 9
                p["playertype"] = "DWARWISH SCOUT"
                p["e_attack"] = get_item(27)
                break
            case _:
                #if q in {"PADENTER","\n", ",", "\x1b", "0"}:
                    return False
    p["color"] = 6
    p["environment"] = [0, 0, 1, 1]
    p["maxhp"], p["hp"] = 30, 30
    p["hpchange"] = 3
    p["basedefend"] = 30
    p["reg_time"] = 10
    p["reg_1/"] = 8
    p["e_hand"] = get_item(60)
    p["BP"] = [get_item(6),get_item(7),(get_item(3)[:2] + [50] + get_item(3)[3:])]
    p["e_armor"] = get_item(17)
    item = change_item(13)[1]
    item[-2] = True
    item[0] = ['POTION OF ENHANCEMENT', 3, 1]
    return True

def imp(w, c, p):
    w.clear()
    w.addstr(0, 30, "DUNGEON OF SHADOW IMPS", c.color_pair(2))
    w.addstr(1, 25, "SELECT A CHARACTER TO PLAY WITH", c.color_pair(1))
    w.addstr(2, 35, version, c.color_pair(4))
    w.addstr(4, 2, "THEY ARE FROM THE BOTTOM OF THE WORLD, THEY KNEW THE WORLD WELL", c.color_pair(3))
    w.addstr(5, 2, "CLASSES (IMP):", c.color_pair(4))
    w.addstr(7, 2, "1 - IMP LINE SOLDIER", c.color_pair(3))
    w.addstr(9, 2, "2 - IMP PALADIN", c.color_pair(3))
    w.refresh()
    while True:
        q = w.getkey()
        match q:
            case "1":
                p["strength"] = 10
                p["dexterity"] = 8
                p["playertype"] = "IMP LINE SOLDIER"
                p["e_hand"] = get_item(60)
                p["BP"] = [get_item(6),get_item(7),(get_item(3)[:2] + [50] + get_item(3)[3:])]
                break
            case "2":
                p["strength"] = 9
                p["dexterity"] = 8
                p["inteligence"] = 10
                p["playertype"] = "IMP PALADIN"
                p["e_hand"] = get_item(65)
                p["BP"] = [get_item(6),get_item(7)]
                p["classicgame"] = False
                break
            case _:
                #if q in {"PADENTER","\n", ",", "\x1b", "0"}:
                    return False
    p["color"] = 3
    p["environment"] = [1, 1, 2, 2]
    p["maxhp"], p["hp"] = 20, 20
    p["basedefend"] = 40
    item = change_item(11)[1]
    item[-2] = True
    item[0] = ['TREASURE MAPPING', 2, 3]
    return True

def algal(w, c, p):
    w.clear()
    w.addstr(0, 30, "DUNGEON OF SHADOW IMPS", c.color_pair(2))
    w.addstr(1, 25, "SELECT A CHARACTER TO PLAY WITH", c.color_pair(1))
    w.addstr(2, 35, version, c.color_pair(4))
    w.addstr(4, 2, "THEY LOOK WEAK, LIKE ALGS. THEY TRAVEL AS APPRENTICE. WHO THEY ARE?", c.color_pair(7))
    w.addstr(5, 2, "CLASSES (ALGAL):", c.color_pair(4))
    w.addstr(7, 2, "1 - ALGAL PALADIN", c.color_pair(7))
    w.addstr(9, 2, "2 - ALGAL DRUID", c.color_pair(7))
    w.addstr(11, 2, "3 - ALGAL WATER MAGE", c.color_pair(7))
    w.addstr(13, 2, "4 - ALGAL WIZARD", c.color_pair(7))
    w.refresh()
    while True:
        q = w.getkey()
        match q:
            case "1":
                p["strength"] = 9
                p["dexterity"] = 8
                p["inteligence"] = 10
                p["playertype"] = "ALGAL PALADIN"
                p["e_hand"] = get_item(65)
                p["BP"] = [get_item(6),get_item(7)]
                break
            case "2":
                p["strength"] = 7
                p["dexterity"] = 9
                p["inteligence"] = 10
                p["playertype"] = "ALGAL DRUID"
                p["e_hand"] = get_item(65)
                p["BP"] = [get_item(6),get_item(7),get_item(62)]
                break
            case "3":
                p["ismage"] = True
                p["strength"] = 7
                p["dexterity"] = 7
                p["inteligence"] = 12
                p["playertype"] = "ALGAL WATER MAGE"
                p["e_hand"] = get_item(63)
                p["BP"] = [get_item(6),get_item(7)]
                break
            case "4":
                p["ismage"] = True
                p["strength"] = 7
                p["dexterity"] = 7
                p["inteligence"] = 12
                p["playertype"] = "ALGAL WIZARD"
                p["e_hand"] = get_item(64)
                p["BP"] = [get_item(6),get_item(7)]
                break
            case _:
               #if q in {"PADENTER","\n", ",", "\x1b", "0"}:
                    return False
    p["color"] = 7
    p["environment"] = [1, 1, 1, 0]
    p["maxhp"], p["hp"] = 10, 10
    p["hpchange"] = 1
    p["basedefend"] = 70
    p["reg_time"] = 16
    p["reg_1/"] = 5
    p["maxeat"] = 5000
    item = change_item(12)[1]
    item[-2] = True
    item[0] = ['POTION OF HEALING', 3, 0]
    item = change_item(15)[1]
    item[-2] = True
    item[0] = ['POTION OF POISON', 3, 3]
    p["classicgame"] = False # all algals use magic -PR-
    return True

def gnome(w, c, p):
    w.clear()
    w.addstr(0, 30, "DUNGEON OF SHADOW IMPS", c.color_pair(2))
    w.addstr(1, 25, "SELECT A CHARACTER TO PLAY WITH", c.color_pair(1))
    w.addstr(2, 35, version, c.color_pair(4))
    w.addstr(4, 2, "HOW HAD YOU OPENED THE DOOR AND KILL THESE RATS?", c.color_pair(5))
    w.addstr(5, 2, "CLASSES (FUDISH):", c.color_pair(4))
    w.addstr(7, 2, "1 - GNOMISH DUELIST", c.color_pair(5))
    w.addstr(9, 2, "2 - GNOMISH ROGUE", c.color_pair(5))
    w.addstr(11, 2, "3 - GNOMISH ARCHER", c.color_pair(5))
    w.addstr(13, 2, "4 - GNOMISH DRUID", c.color_pair(5))
    w.refresh()
    while True:
        q = w.getkey()
        match q:
            case "1":
                p["playertype"] = "GNOMISH DUELIST"
                break
            case "2":
                p["strength"] = 8
                p["dexterity"] = 10
                p["playertype"] = "GNOMISH ROGUE"
                break
            case "3":
                p["strength"] = 7
                p["dexterity"] = 11
                p["playertype"] = "GNOMISH ARCHER"
                p["BP"].append(get_item(1)[:2] + [25] + get_item(1)[3:])
                break
            case "4":
                p["strength"] = 7
                p["dexterity"] = 9
                p["inteligence"] = 10
                p["playertype"] = "GNOMISH DRUID"
                p["e_hand"] = get_item(65)
                p["BP"] = [get_item(6),get_item(7),get_item(62)]
                p["classicgame"] = False
                break
            case _:
                #if q in {"PADENTER","\n", ",", "\x1b", "0"}:
                    return False
    p["iniciative"] = 1
    p["color"] = 5
    p["environment"] = [1, 0, 0, 1]
    p["maxhp"], p["hp"] = 10, 10
    p["hpchange"] = 1
    p["basedefend"] = 70
    p["reg_time"] = 10
    p["reg_1/"] = 5
    return True
