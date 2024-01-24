from local_item_class import get_item, change_item


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
        "e_attack": get_item(24),
        "e_hand": get_item(51),
        "e_armor": get_item(16),
        "blessing": 0,
        "fury": 0,
        "y": 0,
        "x": 0,
        "dy": 0, # direction (movement or attack) y -PR-
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
            ],
        "time": 0,
        "moved": True,
        "id_camp": 0,
        "environment": [0, 0, 0, 0],
        "environment_bonus": 0,
        "type": 1, # type of dungeon -PR-
        "camp": [[["surface",1],[0,3],[0,3],[0,3],[0,3],[0,3],[0,3],[0,3],[0,3],[0,3],["fudit_village",1],[3,3],[3,3],[3,3],[3,3],[3,3],[3,3],[3,3],[3,3],[3,3],["stonehouse",1],[1,3],[1,3],[1,3],[1,3],[1,3],[1,3],[1,3],[1,3],[1,3],["gate",1],[3,3],[0,3],[0,3],[0,3],[0,3],[0,3],[0,3],[0,3],[0,3],["thebook",2]],
                ]
        }

    while True:
        w.clear() # ? -PR-
        w.addstr(0, 30, "DUNGEON OF SHADOW IMPS", c.color_pair(2))
        w.addstr(1, 25, "SELECT A CHARACTER TO PLAY WITH", c.color_pair(1))
        w.addstr(2, 37, "0.2.0", c.color_pair(4))
        w.addstr(3, 2, "SELECT A RACE:", c.color_pair(4))
        w.addstr(5, 2, "1 - HUMAN", c.color_pair(1))
        w.addstr(6, 2, "THE MOST VARIOUS RACE IN THE GAME. THEY LIVE ON THE SURFACE", c.color_pair(1))
        w.addstr(8, 2, "2 - FUDISH", c.color_pair(2))
        w.addstr(9, 2, "FONGUS-LOOKING MONSTERS THAT LIVE IN THE WET PARTS OF THE DUNGEON", c.color_pair(2))
        w.addstr(11, 2, "3 - DWARF", c.color_pair(6))
        w.addstr(12, 2, "GOOD MELEE FIGHTERS. BUT NO ONE KNOWS WHERE THEY COME FROM", c.color_pair(6))
        w.addstr(14, 2, "4 - ALGAL", c.color_pair(3))
        w.addstr(15, 2, "THEY LOOK WEAK, LIKE ALGS. THEY TRAVEL AS DRUIDS. WHERE DO THEY COME FROM?", c.color_pair(3))
        w.addstr(17, 2, "5 - CYCLOPE", c.color_pair(7))
        w.addstr(18, 2, "DIRTY AND SMELLY... THEY ARE FROM THE EAST MOUNTAINS", c.color_pair(7))
        #w.addstr(20, 2, "6 - STONE (YOU CAN'T CHOOSE THE CLASS) (EXPERIMENTAL)", c.color_pair(5))
        #w.addstr(21, 2, "STONE MONSTER. GREAT REGENERATION, BUT WEAK HP. DON'T LIKE MASIVE ATTACKS", c.color_pair(5))
        if w.getmaxyx() != (24,80):
            w.addstr(23, 3, "The screen could't resize it self! (24x80)", c.color_pair(3))
            w.addstr(22, 79, "|", c.color_pair(7))
            w.addstr(23, 71, "point --", c.color_pair(7))
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
                if algal(w, c, p):
                    break
            case "5":
                if cyclope(w, c, p):
                    break
            case _:
                pass
    return m, p, path

def human(w, c, p):
    w.clear()
    w.addstr(0, 30, "DUNGEON OF SHADOW IMPS", c.color_pair(2))
    w.addstr(1, 25, "SELECT A CHARACTER TO PLAY WITH", c.color_pair(1))
    w.addstr(2, 37, "0.2.0", c.color_pair(4))
    w.addstr(3, 2, "CLASSES (HUMAN):", c.color_pair(4))
    w.addstr(5, 2, "1 - HUMAN WARRIOR", c.color_pair(1))
    w.addstr(7, 2, "2 - HUMAN BANDIT", c.color_pair(1))
    w.addstr(9, 2, "3 - HUMAN DUELIST", c.color_pair(1))
    w.addstr(11, 2, "4 - HUMAN ROGUE", c.color_pair(1))
    w.addstr(13, 2, "5 - HUMAN ARCHER", c.color_pair(1))
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
            case _:
                if q in {"PADENTER","\n", ",", "\x1b"}:
                    return False
    p["environment"] = [2, 1, 0, 0]
    p["maxeat"] = 2500
    item = change_item(8)
    item[-2] = True
    item[0] = ['SCROLL OF IDENTIFY', 2, 0]
    return True

def fudish(w, c, p):
    w.clear()
    w.addstr(0, 30, "DUNGEON OF SHADOW IMPS", c.color_pair(2))
    w.addstr(1, 25, "SELECT A CHARACTER TO PLAY WITH", c.color_pair(1))
    w.addstr(2, 37, "0.2.0", c.color_pair(4))
    w.addstr(3, 2, "CLASSES (FUDISH):", c.color_pair(4))
    w.addstr(5, 2, "1 - FUDISH BARBARIAN", c.color_pair(2))
    w.addstr(7, 2, "2 - FUDISH DUELIST", c.color_pair(2))
    w.addstr(9, 2, "3 - FUDISH ROGUE", c.color_pair(2))
    w.addstr(11, 2, "4 - FUDISH ARCHER", c.color_pair(2))
    w.refresh()
    while True:
        q = w.getkey()
        match q:
            case "1":
                p["strength"] = 10
                p["dexterity"] = 8
                p["playertype"] = "FUDISH BARBARIAN"
                break
            case "2":
                p["strength"] = 9
                p["dexterity"] = 9
                p["playertype"] = "FUDISH DUELIST"
                break
            case "3":
                p["strength"] = 8
                p["dexterity"] = 10
                p["playertype"] = "FUDISH ROGUE"
                break
            case "4":
                p["strength"] = 7
                p["dexterity"] = 11
                p["playertype"] = "FUDISH ARCHER"
                p["BP"].append(get_item(1)[:2] + [25] + get_item(1)[3:])
                break
            case _:
                if q in {"PADENTER","\n", ",", "\x1b"}:
                    return False
    p["environment"] = [0, 2, 1, 0]
    p["basedefend"] = 60
    p["reg_time"] = 12
    p["maxeat"] = 5000
    item = change_item(9)
    item[-2] = True
    item[0] = ['SCROLL OF TELEPORTATION', 2, 1]
    return True

def dwarf(w, c, p):
    w.clear()
    w.addstr(0, 30, "DUNGEON OF SHADOW IMPS", c.color_pair(2))
    w.addstr(1, 25, "SELECT A CHARACTER TO PLAY WITH", c.color_pair(1))
    w.addstr(2, 37, "0.2.0", c.color_pair(4))
    w.addstr(3, 2, "CLASSES (DWARF):", c.color_pair(4))
    w.addstr(5, 2, "1 - DWARF WARRIOR", c.color_pair(6))
    w.addstr(7, 2, "2 - DWARF MINER", c.color_pair(6))
    w.addstr(9, 2, "3 - DWARF SCOUT", c.color_pair(6))
    w.refresh()
    while True:
        q = w.getkey()
        match q:
            case "1":
                p["strength"] = 11
                p["dexterity"] = 7
                p["playertype"] = "DWARF WARRIOR"
                p["e_attack"] = get_item(28)
                p["BP"] = [(get_item(3)[:2] + [50] + get_item(3)[3:]), get_item(7)]
                break
            case "2":
                p["strength"] = 10
                p["dexterity"] = 8
                p["playertype"] = "DWARF MINER"
                p["e_attack"] = get_item(28)
                p["BP"] = [(get_item(3)[:2] + [100] + get_item(3)[3:]), get_item(7)]
                break
            case "3":
                p["strength"] = 9
                p["dexterity"] = 9
                p["playertype"] = "DWARF SCOUT"
                p["e_attack"] = get_item(27)
                p["BP"] = [(get_item(3)[:2] + [50] + get_item(3)[3:]), get_item(7)]
                break
            case _:
                if q in {"PADENTER","\n", ",", "\x1b"}:
                    return False
    p["environment"] = [0, 0, 2, 1]
    p["maxhp"], p["hp"] = 30, 30
    p["hpchange"] = 3
    p["basedefend"] = 30
    p["reg_time"] = 10
    p["reg_1/"] = 9
    p["gold"] = 50
    p["e_hand"] = get_item(60)
    p["e_armor"] = get_item(17)
    item = change_item(14)
    item[-2] = True
    item[0] = ['POTION OF ENHANCEMENT', 3, 1]
    return True

def algal(w, c, p):
    w.clear()
    w.addstr(0, 30, "DUNGEON OF SHADOW IMPS", c.color_pair(2))
    w.addstr(1, 25, "SELECT A CHARACTER TO PLAY WITH", c.color_pair(1))
    w.addstr(2, 37, "0.2.0", c.color_pair(4))
    w.addstr(3, 2, "CLASSES (ALGAL):", c.color_pair(4))
    w.addstr(5, 2, "1 - ALGAL WANDERER", c.color_pair(3))
    w.addstr(7, 2, "2 - ALGAL TRAVELER", c.color_pair(3))
    w.refresh()
    while True:
        q = w.getkey()
        match q:
            case "1":
                p["strength"] = 9
                p["dexterity"] = 9
                p["playertype"] = "ALGAL WANDERER"
                break
            case "2":
                p["strength"] = 8
                p["dexterity"] = 10
                p["playertype"] = "ALGAL TRAVELER"
                break
            case _:
                if q in {"PADENTER","\n", ",", "\x1b"}:
                    return False
    p["environment"] = [1, 1, 1, 1]
    p["maxhp"], p["hp"] = 10, 10
    p["hpchange"] = 1
    p["basedefend"] = 70
    p["reg_time"] = 16
    p["reg_1/"] = 5
    p["maxeat"] = 1750
    p["gold"] = 100
    item = change_item(12)
    item[-2] = True
    item[0] = ['POTION OF HEALING', 3, 0]
    item = change_item(15)
    item[-2] = True
    item[0] = ['POTION OF POISON', 3, 3]
    p["BP"].append(get_item(12))
    return True

def cyclope(w, c, p):
    w.clear()
    w.addstr(0, 30, "DUNGEON OF SHADOW IMPS", c.color_pair(2))
    w.addstr(1, 25, "SELECT A CHARACTER TO PLAY WITH", c.color_pair(1))
    w.addstr(2, 37, "0.2.0", c.color_pair(4))
    w.addstr(3, 2, "CLASSES (CYCLOPE):", c.color_pair(4))
    w.addstr(5, 2, "1 - CYCLOPE BEASTMAN", c.color_pair(7))
    w.addstr(7, 2, "2 - CYCLOPE HUNTER", c.color_pair(7))
    w.refresh()
    while True:
        q = w.getkey()
        match q:
            case "1":
                p["strength"] = 10
                p["dexterity"] = 8
                p["playertype"] = "CYCLOPE BEASTMAN"
                break
            case "2":
                p["strength"] = 8
                p["dexterity"] = 10
                p["playertype"] = "CYCLOPE HUNTER"
                break
            case _:
                if q in {"PADENTER","\n", ",", "\x1b"}:
                    return False
    p["environment"] = [0, 0, 0, 0]
    p["maxhp"], p["hp"] = 20, 20
    p["hpchange"] = 2
    p["basedefend"] = 40
    p["reg_time"] = 10
    p["reg_1/"] = 10
    p["gold"] = 50
    p["max_eat"] = 3000
    p["e_attack"] = [['ROUGH CLUB', 'e_attack'], ']', [1, 4, 2, 30, 7, 7], True, 225]
    p["BP"].append([['CYCLOPE-DIA', 2, 4], '?', 1, True, 500])
    item = change_item(11)
    item[-2] = True
    item[0] = ['TREASURE MAPPING', 2, 3]
    return True