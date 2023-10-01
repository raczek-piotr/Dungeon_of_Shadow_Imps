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