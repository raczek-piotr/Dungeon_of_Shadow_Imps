from local_item_class import get_item, change_item


def character(w, c, p):
    while True:
        w.clear() # ? -PR-
        w.addstr(0, 30, "DUNGEON OF SHADOW IMPS", c.color_pair(2))
        w.addstr(1, 25, "SELECT A CHARACTER TO PLAY WITH", c.color_pair(1))
        w.addstr(2, 37, "0.2.0", c.color_pair(4))
        w.addstr(3, 2, "SELECT A RACE:", c.color_pair(4))
        w.addstr(5, 2, "1 - HUMAN", c.color_pair(1))
        w.addstr(6, 2, "THE MOST VARIOUS RACE IN THE GAME. THEY LIVE ON THE SURFACE", c.color_pair(1))
        w.addstr(8, 2, "2 - FUNGAL", c.color_pair(2))
        w.addstr(9, 2, "FONGUS-LOOKING MONSTERS THAT LIVE IN THE WET PARTS OF THE DUNGEON", c.color_pair(2))
        w.addstr(11, 2, "3 - DWARF", c.color_pair(6))
        w.addstr(12, 2, "GOOD MELEE FIGHTERS. BUT NO ONE KNOWS WHERE THEY COME FROM", c.color_pair(6))
        w.addstr(14, 2, "4 - ALGAL", c.color_pair(3))
        w.addstr(15, 2, "THEY LOOK WEAK, LIKE ALGS. THEY TRAVEL AS DRUIDS. WHERE DO THEY COME FROM?", c.color_pair(3))
        w.addstr(17, 2, "5 - KOBOLD", c.color_pair(7))
        w.addstr(18, 2, "NOT VERY LIKED BY HUMANS, STRANGE MONSTERS. THEY TRAVEL A LOT IN THEIR LIVES", c.color_pair(7))
        w.addstr(20, 2, "6 - STONE (YOU CAN'T CHOOSE THE CLASS) (EXPERIMENTAL)", c.color_pair(5))
        w.addstr(21, 2, "STONE MONSTER. GREAT REGENERATION, BUT WEAK HP. DON'T LIKE MASIVE ATTACKS", c.color_pair(5))
        if w.getmaxyx() != (24,80):
            w.addstr(23, 3, "The screen could't resize it self! (24x80)", c.color_pair(3))
            w.addstr(22, 79, "|", c.color_pair(7))
            w.addstr(23, 71, "point ->", c.color_pair(7))
        match w.getkey():
            case "1":
                if human(w, c, p):
                    break
            case "2":
                if fudit(w, c, p):
                    break
            case "3":
                if dwarf(w, c, p):
                    break
            case "4":
                if algal(w, c, p):
                    break
            case "5":
                if kobold(w, c, p):
                    break
            case "6":
                p["strength"] = 11
                p["dexterity"] = 7
                p["playertype"] = "STONE"
                p["maxhp"], p["hp"] = 10, 10
                p["hpchange"] = 1
                p["basedefend"] = 30
                p["reg_time"] = 2
                p["reg_1/"] = 5
                p["maxeat"] = 2500
                p["gold"] = 100
                break
            case _:
                pass

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
    p["maxeat"] = 2500
    item = change_item(8)
    item[-2] = True
    item[0] = ['SCROLL OF IDENTIFY', 2, 0]
    return True

def fudit(w, c, p):
    w.clear()
    w.addstr(0, 30, "DUNGEON OF SHADOW IMPS", c.color_pair(2))
    w.addstr(1, 25, "SELECT A CHARACTER TO PLAY WITH", c.color_pair(1))
    w.addstr(2, 37, "0.2.0", c.color_pair(4))
    w.addstr(3, 2, "CLASSES (FUNGAL):", c.color_pair(4))
    w.addstr(5, 2, "1 - FUNGAL BARBARIAN", c.color_pair(2))
    w.addstr(7, 2, "2 - FUNGAL DUELIST", c.color_pair(2))
    w.addstr(9, 2, "3 - FUNGAL ROGUE", c.color_pair(2))
    w.addstr(11, 2, "4 - FUNGAL ARCHER", c.color_pair(2))
    w.refresh()
    while True:
        q = w.getkey()
        match q:
            case "1":
                p["strength"] = 10
                p["dexterity"] = 8
                p["playertype"] = "FUNGAL BARBARIAN"
                break
            case "2":
                p["strength"] = 9
                p["dexterity"] = 9
                p["playertype"] = "FUNGAL DUELIST"
                break
            case "3":
                p["strength"] = 8
                p["dexterity"] = 10
                p["playertype"] = "FUNGAL ROGUE"
                break
            case "4":
                p["strength"] = 7
                p["dexterity"] = 11
                p["playertype"] = "FUNGAL ARCHER"
                p["BP"].append(get_item(1)[:2] + [25] + get_item(1)[3:])
                break
            case _:
                if q in {"PADENTER","\n", ",", "\x1b"}:
                    return False
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
                p["e_attack"] = get_item(27)
                p["BP"] = [(get_item(3)[:2] + [50] + get_item(3)[3:]), get_item(7)]
                break
            case "2":
                p["strength"] = 10
                p["dexterity"] = 8
                p["playertype"] = "DWARF MINER"
                p["e_attack"] = get_item(27)
                p["BP"] = [(get_item(3)[:2] + [100] + get_item(3)[3:]), get_item(7)]
                break
            case "3":
                p["strength"] = 9
                p["dexterity"] = 9
                p["playertype"] = "DWARF SCOUT"
                p["e_attack"] = get_item(26)
                p["BP"] = [(get_item(3)[:2] + [50] + get_item(3)[3:]), get_item(7)]
                break
            case _:
                if q in {"PADENTER","\n", ",", "\x1b"}:
                    return False
    p["maxhp"], p["hp"] = 30, 30
    p["hpchange"] = 3
    p["basedefend"] = 30
    p["reg_time"] = 10
    p["reg_1/"] = 9
    p["gold"] = 50
    p["e_hand"] = get_item(59)
    p["e_armor"] = get_item(17)
    item = change_item(13)
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

def kobold(w, c, p):
    w.clear()
    w.addstr(0, 30, "DUNGEON OF SHADOW IMPS", c.color_pair(2))
    w.addstr(1, 25, "SELECT A CHARACTER TO PLAY WITH", c.color_pair(1))
    w.addstr(2, 37, "0.2.0", c.color_pair(4))
    w.addstr(3, 2, "CLASSES (KOBOLD):", c.color_pair(4))
    w.addstr(5, 2, "1 - KOBOLD BEASTMAN", c.color_pair(7))
    w.addstr(7, 2, "2 - KOBOLD SEEKER", c.color_pair(7))
    w.addstr(9, 2, "3 - KOBOLD HUNTER", c.color_pair(7))
    w.refresh()
    while True:
        q = w.getkey()
        match q:
            case "1":
                p["strength"] = 10
                p["dexterity"] = 8
                p["playertype"] = "KOBOLD BEASTMAN"
                break
            case "2":
                p["strength"] = 9
                p["dexterity"] = 9
                p["playertype"] = "KOBOLD SEEKER"
                break
            case "3":
                p["strength"] = 8
                p["dexterity"] = 10
                p["playertype"] = "KOBOLD HUNTER"
                break
            case _:
                if q in {"PADENTER","\n", ",", "\x1b"}:
                    return False
    p["basedefend"] = 40
    p["reg_time"] = 8
    p["reg_1/"] = 10
    p["maxeat"] = 3000
    p["gold"] = 150
    p["e_armor"] = get_item(17)
    item = change_item(11)
    item[-2] = True
    item[0] = ['TREASURE MAPPING', 2, 3]
    return True