from local_item_class import get_item
from local_scores import scoreboard_print
from local_iostream import loadgame
from local_game_exit import game_exit
from consts import version, path

from random import randint
from os.path import isfile

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
        "maxhp": 30,
        "hp": 30,
        "hpchange": 3,
        "reg_time": 10,
        "reg_1/": 10,
        "needxp": 40,
        "xpchange": 40,
        "xp": 0,
        "lw": 1,
        "depth": 40,
        "strength": 9,
        "dexterity": 9,
        "inteligence": 0,
        "magic_list": False,
        "alt": False,
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
        "camp": [[["surface",0],      [10,3],[10,3],[10,3],[0,3], [0,3], [0,3], [0,3], [0,3], [11,3],
                  ["stonehouse",0],   [11,3],[11,3],[11,3],[1,3], [1,3], [1,3], [12,3],[12,3],[12,3],
                  ["fudit_village",0],[12,3],[12,3],[12,3],[1,3], [1,3], [1,3], [1,3], [1,3], [13,3],
                  ["gate",0],         [13,3], [3,3], [3,3],[3,3], [3,3], [3,3], [14,3],[14,3],[14,3], ["thebook",3],
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
        w.addstr(12, 2, "GOOD TANK FIGHTERS. BUT NO ONE KNOWS WHERE THEY COME FROM", c.color_pair(6))
        w.addstr(14, 2, "4 - GNOME", c.color_pair(7))
        w.addstr(15, 2, "HOW HAD YOU OPENED THE DOOR AND KILL ALL THESE RATS?", c.color_pair(7))
        w.addstr(23, 2, "* - VIEW SCOREBOARD", c.color_pair(4))
        #if isfile(path + "save.txt"):
        w.addstr(23, 31, "+ - LOAD SAVED GAME (if saved)", c.color_pair(4))
        w.addstr(23, 68, "q - quit", c.color_pair(4))
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
                if gnome(w, c, p):
                    break
            case "*":
                scoreboard_print(w, c)
            case "+":
                t = loadgame()
                if t:
                    return m, t, path
            case "q":
                game_exit()
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
    w.addstr(9, 42, "7 - HUMAN DRUID", c.color_pair(1))
    w.addstr(11, 42, "8 - HUMAN WATER MAGE", c.color_pair(1))
    w.addstr(13, 42, "9 - HUMAN WIZARD", c.color_pair(1))
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
                p["BP"].append(get_item(1))
                p["BP"][-1][2] = 25
                break
            case "6":
                p["strength"] = 9
                p["dexterity"] = 8
                p["inteligence"] = 9
                p["playertype"] = "HUMAN PALADIN"
                p["e_hand"] = get_item(66)
                p["BP"] = [get_item(6),get_item(7)]
                p["classicgame"] = False
                break
            case "7":
                p["strength"] = 7
                p["dexterity"] = 9
                p["inteligence"] = 10
                p["playertype"] = "HUMAN DRUID"
                p["e_hand"] = get_item(63)
                p["classicgame"] = False
                break
            case "8":
                p["ismage"] = True
                p["strength"] = 7
                p["dexterity"] = 7
                p["inteligence"] = 12
                p["playertype"] = "HUMAN WATER MAGE"
                p["e_hand"] = get_item(64)
                p["BP"] = [get_item(6),get_item(7)]
                p["classicgame"] = False
                break
            case "9":
                p["ismage"] = True
                p["strength"] = 7
                p["dexterity"] = 7
                p["inteligence"] = 12
                p["playertype"] = "HUMAN WIZARD"
                p["e_hand"] = get_item(65)
                p["BP"] = [get_item(6),get_item(7)]
                p["classicgame"] = False
                break
            case _:
                return False
    p["gold"] = 350
    # except last levels…
    p["environment"] = [1, 1, 1, 0]
    return True

def fudish(w, c, p):
    w.clear()
    w.addstr(0, 30, "DUNGEON OF SHADOW IMPS", c.color_pair(2))
    w.addstr(1, 25, "SELECT A CHARACTER TO PLAY WITH", c.color_pair(1))
    w.addstr(2, 35, version, c.color_pair(4))
    w.addstr(4, 2, "FONGUS-LOOKING MONSTERS THAT LIVE IN THE WET PARTS OF THE DUNGEON", c.color_pair(2))
    w.addstr(5, 2, "CLASSES (FUDISH):", c.color_pair(4))
    w.addstr(7, 2, "1 - FUDISH WARRIOR", c.color_pair(1))
    w.addstr(9, 2, "2 - FUDISH BANDIT", c.color_pair(1))
    w.addstr(11, 2, "3 - FUDISH DUELIST", c.color_pair(1))
    w.addstr(13, 2, "4 - FUDISH ROGUE", c.color_pair(1))
    w.addstr(15, 2, "5 - FUDISH ARCHER", c.color_pair(1))
    w.addstr(7, 42, "6 - FUDISH PALADIN", c.color_pair(1))
    w.addstr(9, 42, "7 - FUDISH DRUID", c.color_pair(1))
    w.addstr(11, 42, "8 - FUDISH WATER MAGE", c.color_pair(1))
    w.addstr(13, 42, "9 - FUDISH WIZARD", c.color_pair(1))
    w.refresh()
    while True:
        q = w.getkey()
        match q:
            case "1":
                p["strength"] = 11
                p["dexterity"] = 7
                p["playertype"] = "FUDISH WARRIOR"
                break
            case "2":
                p["strength"] = 10
                p["dexterity"] = 8
                p["playertype"] = "FUDISH BANDIT"
                break
            case "3":
                p["playertype"] = "FUDISH DUELIST"
                break
            case "4":
                p["strength"] = 8
                p["dexterity"] = 10
                p["playertype"] = "FUDISH ROUGE"
                break
            case "5":
                p["strength"] = 7
                p["dexterity"] = 11
                p["playertype"] = "FUDISH ARCHER"
                p["BP"].append(get_item(1))
                p["BP"][-1][2] = 25
                break
            case "6":
                p["strength"] = 9
                p["dexterity"] = 8
                p["inteligence"] = 9
                p["playertype"] = "FUDISH PALADIN"
                p["e_hand"] = get_item(66)
                p["BP"] = [get_item(6),get_item(7)]
                p["classicgame"] = False
                break
            case "7":
                p["strength"] = 7
                p["dexterity"] = 9
                p["inteligence"] = 10
                p["playertype"] = "FUDISH DRUID"
                p["e_hand"] = get_item(63)
                p["classicgame"] = False
                break
            case "8":
                p["ismage"] = True
                p["strength"] = 7
                p["dexterity"] = 7
                p["inteligence"] = 12
                p["playertype"] = "FUDISH WATER MAGE"
                p["e_hand"] = get_item(64)
                p["BP"] = [get_item(6),get_item(7)]
                p["classicgame"] = False
                break
            case "9":
                p["ismage"] = True
                p["strength"] = 7
                p["dexterity"] = 7
                p["inteligence"] = 12
                p["playertype"] = "FUDISH WIZARD"
                p["e_hand"] = get_item(65)
                p["BP"] = [get_item(6),get_item(7)]
                p["classicgame"] = False
                break
            case _:
                return False
    p["color"] = 2
    # self ground boost
    p["environment"] = [0, 5, 0, 0]
    p["basedefend"] = 60
    p["reg_time"] = 12
    p["maxeat"] = 5000
    return True

def dwarf(w, c, p):
    w.clear()
    w.addstr(0, 30, "DUNGEON OF SHADOW IMPS", c.color_pair(2))
    w.addstr(1, 25, "SELECT A CHARACTER TO PLAY WITH", c.color_pair(1))
    w.addstr(2, 35, version, c.color_pair(4))
    w.addstr(4, 2, "GOOD TANK FIGHTERS. BUT NO ONE KNOWS WHERE THEY COME FROM", c.color_pair(6))
    w.addstr(5, 2, "CLASSES (DWARF):", c.color_pair(4))
    w.addstr(7, 2, "1 - DWARF WARRIOR", c.color_pair(6))
    w.addstr(9, 2, "2 - DWARF BANDIT", c.color_pair(6))
    w.addstr(11, 2, "3 - DWARF DUELIST", c.color_pair(6))
    w.addstr(13, 2, "4 - DWARF ROGUE", c.color_pair(6))
    w.addstr(15, 2, "5 - DWARF ARCHER", c.color_pair(6))
    w.refresh()
    while True:
        q = w.getkey()
        match q:
            case "1":
                p["strength"] = 11
                p["dexterity"] = 7
                p["playertype"] = "DWARF WARRIOR"
                break
            case "2":
                p["strength"] = 10
                p["dexterity"] = 8
                p["playertype"] = "DWARF BANDIT"
                break
            case "3":
                p["playertype"] = "DWARF DUELIST"
                break
            case "4":
                p["strength"] = 8
                p["dexterity"] = 10
                p["playertype"] = "DWARF ROUGE"
                break
            case "5":
                p["strength"] = 7
                p["dexterity"] = 11
                p["playertype"] = "DWARF ARCHER"
                p["BP"].append(get_item(1))
                p["BP"][-1][2] = 25
                break
            case _:
                return False
    p["color"] = 6
    # no critic hits
    #p["environment"] = [0, 0, 0, 0]
    p["maxhp"], p["hp"] = 40, 40
    p["hpchange"] = 4
    p["basedefend"] = 20
    p["reg_time"] = 10
    p["reg_1/"] = 16
    return True

def gnome(w, c, p):
    w.clear()
    w.addstr(0, 30, "DUNGEON OF SHADOW IMPS", c.color_pair(2))
    w.addstr(1, 25, "SELECT A CHARACTER TO PLAY WITH", c.color_pair(1))
    w.addstr(2, 35, version, c.color_pair(4))
    w.addstr(4, 2, "HOW HAD YOU OPENED THE DOOR AND KILL THESE RATS?", c.color_pair(7))
    w.addstr(5, 2, "CLASSES (GNOME):", c.color_pair(4))
    w.addstr(7, 2, "1 - GNOME WARRIOR", c.color_pair(7))
    w.addstr(9, 2, "2 - GNOME BANDIT", c.color_pair(7))
    w.addstr(11, 2, "3 - GNOME DUELIST", c.color_pair(7))
    w.addstr(13, 2, "4 - GNOME ROGUE", c.color_pair(7))
    w.addstr(15, 2, "5 - GNOME ARCHER", c.color_pair(7))
    w.addstr(7, 42, "6 - GNOME PALADIN", c.color_pair(7))
    w.addstr(9, 42, "7 - GNOME DRUID", c.color_pair(7))
    w.addstr(11, 42, "8 - GNOME WATER MAGE", c.color_pair(7))
    w.addstr(13, 42, "9 - GNOME WIZARD", c.color_pair(7))
    w.refresh()
    while True:
        q = w.getkey()
        match q:
            case "1":
                p["strength"] = 11
                p["dexterity"] = 7
                p["playertype"] = "GNOME WARRIOR"
                break
            case "2":
                p["strength"] = 10
                p["dexterity"] = 8
                p["playertype"] = "GNOME BANDIT"
                break
            case "3":
                p["playertype"] = "GNOME DUELIST"
                break
            case "4":
                p["strength"] = 8
                p["dexterity"] = 10
                p["playertype"] = "GNOME ROUGE"
                break
            case "5":
                p["strength"] = 7
                p["dexterity"] = 11
                p["playertype"] = "GNOME ARCHER"
                p["BP"].append(get_item(1))
                p["BP"][-1][2] = 25
                break
            case "6":
                p["strength"] = 9
                p["dexterity"] = 8
                p["inteligence"] = 9
                p["playertype"] = "GNOME PALADIN"
                p["e_hand"] = get_item(66)
                p["BP"] = [get_item(6),get_item(7)]
                p["classicgame"] = False
                break
            case "7":
                p["strength"] = 7
                p["dexterity"] = 9
                p["inteligence"] = 10
                p["playertype"] = "GNOME DRUID"
                p["e_hand"] = get_item(63)
                p["classicgame"] = False
                break
            case "8":
                p["ismage"] = True
                p["strength"] = 7
                p["dexterity"] = 7
                p["inteligence"] = 12
                p["playertype"] = "GNOME WATER MAGE"
                p["e_hand"] = get_item(64)
                p["BP"] = [get_item(6),get_item(7)]
                p["classicgame"] = False
                break
            case "9":
                p["ismage"] = True
                p["strength"] = 7
                p["dexterity"] = 7
                p["inteligence"] = 12
                p["playertype"] = "GNOME WIZARD"
                p["e_hand"] = get_item(65)
                p["BP"] = [get_item(6),get_item(7)]
                p["classicgame"] = False
                break
            case _:
                return False
    p["color"] = 7
    p["iniciative"] = 1
    p["environment"] = [1, 1, 1, 1]
    p["maxhp"], p["hp"] = 20, 20
    p["hpchange"] = 2
    p["basedefend"] = 60
    p["reg_time"] = 6
    p["reg_1/"] = 10
    return True