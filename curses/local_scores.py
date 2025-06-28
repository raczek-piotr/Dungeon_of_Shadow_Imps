from consts import path

def scoreboard_print(w, c):
    try:
        with open(path + "scores.txt", 'r'):
            pass
    except:
        with open(path + "scores.txt", 'w') as  scores_txt:
            scores_txt.write("5001|CLASSIC|DWARWISH STEELCLAD|7245|28|27|-|[]|True\n625|CLASSIC|FUDISH ARCHER|2214|8|8|-|[]|True\n")
    with open(path + "scores.txt", 'r') as scores_txt:
        scores = scores_txt.read().split("\n")

    while scores[-1] == "": # empty lines -PR-
        scores.pop(-1)
    for t in range(len(scores)):
        scores[t] = scores[t].split("|")
    scores = sorted(scores, key = lambda key: int(key[0]))
    orgscores = scores.copy()

    w.clear()
    w.addstr(0, 16, "dosi Scoreboard", c.color_pair(1))
    w.addstr(1, 3, "Win? Score:    Turns:    Lw: Depth: PlayerType:         NickName:", c.color_pair(4))
    scores = scores[:-22:-1]
    for t in range(len(scores)):
        w.addstr(t+2, 1, str(t+1)+".", c.color_pair(2))
        w.addstr(t+2, 4, scores[t][6], c.color_pair(5))
        w.addstr(t+2, 8, scores[t][0], c.color_pair(1))
        w.addstr(t+2, 18, scores[t][3], c.color_pair(5))
        w.addstr(t+2, 28, scores[t][4], c.color_pair(1))
        w.addstr(t+2, 33, scores[t][5], c.color_pair(1))
        w.addstr(t+2, 39, scores[t][2], c.color_pair(5))
        w.addstr(t+2, 59, scores[t][1][:20], c.color_pair(1))
    w.getkey()

    scores = orgscores
    scores2 = []
    for t in range(len(scores)-1 ,-1,-1):
        if scores[t][8] != "True":
            scores2.append(scores.pop(t))
            
    w.clear()
    w.addstr(0, 8, "Classic dosi Scoreboard", c.color_pair(7))
    w.addstr(1, 3, "Win? Score:    Turns:    Lw: Depth: PlayerType:         NickName:", c.color_pair(4))
    scores = scores[:-22:-1]
    for t in range(len(scores)):
        w.addstr(t+2, 1, str(t+1)+".", c.color_pair(2))
        w.addstr(t+2, 4, scores[t][6], c.color_pair(5))
        w.addstr(t+2, 8, scores[t][0], c.color_pair(1))
        w.addstr(t+2, 18, scores[t][3], c.color_pair(5))
        w.addstr(t+2, 28, scores[t][4], c.color_pair(1))
        w.addstr(t+2, 33, scores[t][5], c.color_pair(1))
        w.addstr(t+2, 39, scores[t][2], c.color_pair(5))
        w.addstr(t+2, 59, scores[t][1][:20], c.color_pair(1))
    w.getkey()

    scores = scores2
    w.clear()
    w.addstr(0, 10, "Magic dosi Scoreboard", c.color_pair(2))
    w.addstr(1, 3, "Win? Score:    Turns:    Lw: Depth: PlayerType:         NickName:", c.color_pair(4))
    scores = scores[:22]
    for t in range(len(scores)):
        w.addstr(t+2, 1, str(t+1)+".", c.color_pair(2))
        w.addstr(t+2, 4, scores[t][6], c.color_pair(5))
        w.addstr(t+2, 8, scores[t][0], c.color_pair(1))
        w.addstr(t+2, 18, scores[t][3], c.color_pair(5))
        w.addstr(t+2, 28, scores[t][4], c.color_pair(1))
        w.addstr(t+2, 33, scores[t][5], c.color_pair(1))
        w.addstr(t+2, 39, scores[t][2], c.color_pair(5))
        w.addstr(t+2, 59, scores[t][1][:20], c.color_pair(1))
    w.getkey()


def scoreboard_append(w, c, p, wins = False):
    if wins:
        win = "+"
    else:
        win = "-"
    try:
        with open(path + "scores.txt", 'r'):
            pass
    except:
        with open(path + "scores.txt", 'w') as  scores_txt:
            scores_txt.write("505|DEFAULT|DWARF MINER|2343|7|7|-|[]\n")

    if p["classicgame"]:
        points = p["xp"]+(p["attack"]*(p["attack_damage"]+1)*p["attack_acc"]*p["attack_hits"])//5+(p["bow"]*(p["bow_damage"]+1)*p["bow_acc"]*p["bow_hits"])//10+10*(p["lw"]+p["depth"]+p["armor"])-80
    else:
        points = p["xp"]+(p["attack"]*(p["attack_damage"]+1)*p["attack_acc"]*p["attack_hits"])//5+10*(p["lw"]+p["depth"]+p["armor"]+p["inteligence"])-22
    c.curs_set(2)
    q = ""
    nick = ""
    while q not in {"PADENTER","\n", ",", "\x1b"}:
        if q in {"KEY_BACKSPACE", ""}:
            nick = nick[:-1]
        elif len(nick) >= 20 or q in {"|", "KEY_LEFT", "KEY_RIGHT", "KEY_UP", "KEY_DOWN"}:
            c.beep()
        else:
            nick += q
        w.clear()
        w.addstr(2, 31, "NICKNAME: (max: 20)", c.color_pair(4))
        w.addstr(3, 31, nick, c.color_pair(1))
        q = w.getkey()
    c.curs_set(0)
    with open(path + "scores.txt", 'a') as scores_txt:
        scores_txt.write(str(points)+"|"+nick+"|"+p["playertype"]+"|"+str(p["time"])+"|"+str(p["lw"])+"|"+str(p["depth"])+"|"+win+"|"+str(p["BP"])+"|"+str(p["classicgame"])+"\n")

    scoreboard_print(w, c)

    return points