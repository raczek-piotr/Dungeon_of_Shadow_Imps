from random import randint, choice
#from time import sleep
from local_scripts import zero3  # or "*" -PR-
from local_map import map_init
from local_enemies_class import enemies_class_clear
from local_character import character

from local_equip import get_equip_values
from local_translator import translate
from local_item_class import get_item, randitem


def menager(w, c, command = "#R", m = {}, p = {}): # #E - end game #R - try to reload or start, #S - save, #U - go up, #D - go down -PR-
    match command[:2]:
        case "#E":
            scoreboard_append(w, c, p)
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
            c.init_pair(6, 57, 16)
            c.init_pair(7, 196, 16)
            character(w, c, p)
            get_equip_values(p)
            scoreboard_print(w, c)
            w.clear()
            w.addstr(5, 5, "The angel of the LORD came back a second time and touched YOU and said:", c.color_pair(5))
            w.addstr(6, 13, '"Get up and eat, for the journey is too much for you."', c.color_pair(1))
            w.addstr(23, 65, "~ 1 KINGS 19:7", c.color_pair(5))
            w.getkey()
            prepare_map(m, p)
            return m, p, path

def prepare_map(m, p):
    h = p["camp"][p["id_camp"]][p["depth"]].copy()
    while h == "next": # not used -PR-
        p["id_camp"] += 1
        h = p["camp"][p["id_camp"]][p["depth"]].copy()
    if h[0] == "?":
        h[0] = p["type"]
        i = randint(-1, 1)
        if p["type"] + i in {0,1,2}:
            p["type"] += i
    enemies_class_clear()
    ilist, xp = [], 0
    if type(h[0]) == int:
        p["normal_level"] = True # "needs" are enable/disable -PR-
        ilist = randitem(h[0]+5, 8, 58)+randitem(2, 0, 4)# + arrows -PR-
        for _ in range(randint(0,3+p["type"])):
            ilist.append("$"+zero3(randint(3,5+5*p["type"])))
    #else:
    #    p["normal_level"] = False 
    p["y"], p["x"] = map_init(m, p, ilist, h[0], h[1])

def start_data():
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
        "needxp": 30,
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
        "e_attack": get_item(23),
        "e_hand": get_item(50),
        "e_armor": get_item(16),
        "blessing": 0,
        "fury": 0,
        "y": 0,
        "x": 0,
        "dy": 0, # direction y -PR-
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
            #for testing only{"item": "MAGIC MAPPING", "type": "!", "values": [20, "MAGIC MAPPING"], "cost": 40, "grouping": True},
            ],
        "time": 0,
        "moved": True,
        "id_camp": 0,
        "type": 1, # type of dungeon -PR-
        "camp": [[["surface",0],["?",3],["?",3],["?",3],["?",3],["?",3],["?",3],["?",3],["?",3],["?",3],["fudit_village",3],[7,3],[7,3],["?",3],["?",3],["?",3],["?",3],["?",3],["?",3],["?",3],["?",3],["surface",3]],
                ]
        }
    return m, p, path

def scoreboard_print(w, c):
    try:
        with open("scores.txt", 'r'):
            pass
    except:
        with open("scores.txt", 'w') as  scores_txt:
            scores_txt.write("0|FUEL|A FUEL|0|0|0|L|[]\n")
    with open("scores.txt", 'r') as scores_txt:
        scores = scores_txt.read().split("\n")

    while scores[-1] == "": # empty lines -PR-
        scores.pop(-1)
    for t in range(len(scores)):
        scores[t] = scores[t].split("|")
    scores = sorted(scores, key = lambda key: int(key[0]))

    w.clear()
    w.addstr(0, 3, "Win? Score:    Turns:    Lw: Depth: PlayerType:         NickName:          ", c.color_pair(4))
    scores = scores[:-23:-1]
    for t in range(len(scores)):
        w.addstr(t+1, 1, str(t)+".", c.color_pair(2))
        w.addstr(t+1, 4, scores[t][6], c.color_pair(5))
        w.addstr(t+1, 8, scores[t][0], c.color_pair(1))
        w.addstr(t+1, 18, scores[t][3], c.color_pair(5))
        w.addstr(t+1, 28, scores[t][4], c.color_pair(1))
        w.addstr(t+1, 33, scores[t][5], c.color_pair(1))
        w.addstr(t+1, 39, scores[t][2], c.color_pair(5))
        w.addstr(t+1, 59, scores[t][1][:20], c.color_pair(1))
    w.getkey()


def scoreboard_append(w, c, p):
    try:
        with open("scores.txt", 'r'):
            pass
    except:
        with open("scores.txt", 'w') as  scores_txt:
            scores_txt.write("0|FUEL|A FUEL|0|0|0|L|[]\n")

    points = p["xp"]+(p["attack"]*(p["attack_damage"]+1)*p["attack_acc"]*p["attack_hits"])//5+(p["bow"]*(p["bow_damage"]+1)*p["bow_acc"]*p["bow_hits"])//10+10*(p["lw"]+p["depth"]+p["armor"])-80
    c.curs_set(2)
    q = ""
    nick = ""
    while q not in {"PADENTER","\n", ",", "\x1b"}:
        if q == "KEY_BACKSPACE":
            nick = nick[:-1]
        elif len(nick) >= 20 or q == "|":
            c.beep()
        else:
            nick += q
        w.clear()
        w.addstr(2, 31, "NICKNAME: (max: 20)", c.color_pair(4))
        w.addstr(3, 31, nick, c.color_pair(1))
        q = w.getkey()
    c.curs_set(0)
    with open("scores.txt", 'a') as scores_txt:
        scores_txt.write(str(points)+"|"+nick+"|"+p["playertype"]+"|"+str(p["time"])+"|"+str(p["lw"])+"|"+str(p["depth"])+"|L|"+str(p["BP"])+"\n")

    with open("scores.txt", 'r') as scores_txt:
        scores = scores_txt.read().split("\n")
    while scores[-1] == "": # empty lines -PR-
        scores.pop(-1)

    for t in range(len(scores)):
        scores[t] = scores[t].split("|")
    scores = sorted(scores, key = lambda key: int(key[0]))

    w.clear()
    w.addstr(0, 3, "Win? Score:    Turns:    Lw: Depth: PlayerType:         NickName:          ", c.color_pair(4))
    scores = scores[:-23:-1]
    for t in range(len(scores)):
        w.addstr(t+1, 1, str(t)+".", c.color_pair(2))
        w.addstr(t+1, 4, scores[t][6], c.color_pair(5))
        w.addstr(t+1, 8, scores[t][0], c.color_pair(1))
        w.addstr(t+1, 18, scores[t][3], c.color_pair(5))
        w.addstr(t+1, 28, scores[t][4], c.color_pair(1))
        w.addstr(t+1, 33, scores[t][5], c.color_pair(1))
        w.addstr(t+1, 39, scores[t][2], c.color_pair(5))
        w.addstr(t+1, 59, scores[t][1][:20], c.color_pair(1))
    w.getkey()
