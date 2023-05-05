from random import randint
from local_zero3 import zero3
from local_translator import translate

def enemies_class_clear():
    global c, a, mhr, tlist, exlist # c - class, mhr - max hear range -PR-
    tlist = {".",","," ","]","}",")","$","~","-","*","!","?","<",">"}
    exlist = tlist.copy()
    c, a, mhr = [], [], 1

def enemies_class_init(head, y, x, hp = 8, attack = 2, xp = 1, time_sleep = 1, hear_range = 5, ranged = False, carring = []):
    global c, a, mhr, exlist
    if ranged:
        a.append({"head": head, "y": y, "x": x, "mhp": hp, "hp": hp, "attack": attack, "xp": xp,
            "time_sleep": time_sleep, "hear_range": hear_range, "carring": carring})
        it = len(a)+500
    else:
        c.append({"head": head, "y": y, "x": x, "mhp": hp, "hp": hp, "attack": attack, "xp": xp,
            "time_sleep": time_sleep, "hear_range": hear_range, "carring": carring})
        it = len(c)
    if mhr < hear_range-1:
        mhr = hear_range-1
    if head not in exlist:
        exlist.add(head)
    return(it-1)  # return id -PR-

def enemies_class_update(m, p, yx):
    global c, a, mhr, tlist, exlist
    m["m"] = [[-1 for _ in range(m["sx"])] for _ in range(m["sy"])]
    w, k = yx[0], yx[1] # row kolumn -PR-
    q = [[w, k, -1]]
    while q != []:
        p1 = q.pop(0)
        if p1[2] <= mhr:
            w, k = p1[0], p1[1]
            if (m["r"][w][k][0] in exlist) and m["m"][w][k] == -1:
                q.append([w, k, p1[2] + 1])
                m["m"][w][k] = p1[2] + 1
            if (m["r"][w-1][k][0] in exlist) and m["m"][w-1][k] == -1:
                q.append([w-1, k, p1[2] + 1])
                m["m"][w-1][k] = p1[2] + 1
            if (m["r"][w+1][k][0] in exlist) and m["m"][w+1][k] == -1:
                q.append([w+1, k, p1[2] + 1])
                m["m"][w+1][k] = p1[2] + 1
            if (m["r"][w][k-1][0] in exlist) and m["m"][w][k-1] == -1:
                q.append([w, k-1, p1[2] + 1])
                m["m"][w][k-1] = p1[2] + 1
            if (m["r"][w][k+1][0] in exlist) and m["m"][w][k+1] == -1:
                q.append([w, k+1, p1[2] + 1])
                m["m"][w][k+1] = p1[2] + 1

            if (m["r"][w-1][k-1][0] in exlist) and m["m"][w-1][k-1] == -1:
                q.append([w-1, k-1, p1[2] + 1])
                m["m"][w-1][k-1] = p1[2] + 1
            if (m["r"][w+1][k-1][0] in exlist) and m["m"][w+1][k-1] == -1:
                q.append([w+1, k-1, p1[2] + 1])
                m["m"][w+1][k-1] = p1[2] + 1
            if (m["r"][w-1][k+1][0] in exlist) and m["m"][w-1][k+1] == -1:
                q.append([w-1, k+1, p1[2] + 1])
                m["m"][w-1][k+1] = p1[2] + 1
            if (m["r"][w+1][k+1][0] in exlist) and m["m"][w+1][k+1] == -1:
                q.append([w+1, k+1, p1[2] + 1])
                m["m"][w+1][k+1] = p1[2] + 1

    t = []
    for it in range(len(c)):
        q = c[it]
        if q["head"]+zero3(it) == m["r"][q["y"]][q["x"]][:4] and m["m"][q["y"]][c[it]["x"]] < q["hear_range"]: # q["hp"] > 0 he won't be on the map! -PR-
            if q["time_sleep"] == 0:
                if m["m"][q["y"]][q["x"]] == 0:
                    enemies_class_attack(p, q["head"], q["attack"])
                else:
                    t.append(it)
            else:
                q["time_sleep"] -= 1
    while t != []:
        it = t.pop(randint(0, len(t)-1)) # it = id
        q = c[it]
        t_mmap = [[m["m"][q["y"]-1][q["x"]-1], q["y"]-1, q["x"]-1],
                  [m["m"][q["y"]-1][q["x"]], q["y"]-1, q["x"]],
                  [m["m"][q["y"]-1][q["x"]+1], q["y"]-1, q["x"]+1],
                  [m["m"][q["y"]][q["x"]-1], q["y"], q["x"]-1],
                  #[m["m"][q["y"]][q["x"]], q["y"], q["x"]], # stay -PR-
                  [m["m"][q["y"]][q["x"]+1], q["y"], q["x"]+1],
                  [m["m"][q["y"]+1][q["x"]-1], q["y"]+1, q["x"]-1],
                  [m["m"][q["y"]+1][q["x"]], q["y"]+1, q["x"]],
                  [m["m"][q["y"]+1][q["x"]+1], q["y"]+1, q["x"]+1],
                  ]
        p_min = m["m"][q["y"]][q["x"]]
        direction = [m["m"][q["y"]][q["x"]], q["y"], q["x"]] # stay -PR-

        while t_mmap != []:
            i = t_mmap.pop(randint(0, len(t_mmap)-1))
            if i[0] >= 0 and i[0] <= p_min:
                p_min = i[0]
                direction = i
        m["r"][q["y"]][q["x"]] = m["r"][q["y"]][q["x"]][4:]
        #if m["r"][q["y"]][q["x"]] == "":
        #    m["r"][q["y"]][q["x"]] = " "
        #    print("CUT OFF WORNING, I DON'T KNOW WHY")
        if m["v"][q["y"]][q["x"]][0] != " ":
            m["v"][q["y"]][q["x"]] = m["r"][q["y"]][q["x"]]
        if m["r"][direction[1]][direction[2]][0] in tlist: # move an enemie? -PR-
            q["y"], q["x"] = direction[1:]
        m["r"][q["y"]][q["x"]] = q["head"]+zero3(it)+m["r"][q["y"]][q["x"]]
        if m["r"][q["y"]][q["x"]][-1] != " ":
            m["v"][q["y"]][q["x"]] = m["r"][q["y"]][q["x"]]



    for y in range(len(m["m"])): # time for archers -PR-
        for x in range(len(m["m"][0])):
            if m["m"][y][x] != -1:
                m["m"][y][x] = -2
    q = [] # it isn't needed -PR-
    for i in [[1,1],[1,0],[1,-1],[0,1],[0,-1],[-1,1],[-1,0],[-1,-1]]:
        w, k = yx[0]+i[0], yx[1]+i[1]
        while m["m"][w][k] == -2:
            q.append([w, k, 0])
            m["m"][w][k] = 0
            w, k = w +i[0], k +i[1]
    while q != []:
        p1 = q.pop(0)
        if p1[2] <= mhr:
            w, k = p1[0], p1[1]
            if (m["r"][w][k][0] in exlist) and m["m"][w][k] == -2:
                q.append([w, k, p1[2] + 1])
                m["m"][w][k] = p1[2] + 1
            if (m["r"][w-1][k][0] in exlist) and m["m"][w-1][k] == -2:
                q.append([w-1, k, p1[2] + 1])
                m["m"][w-1][k] = p1[2] + 1
            if (m["r"][w+1][k][0] in exlist) and m["m"][w+1][k] == -2:
                q.append([w+1, k, p1[2] + 1])
                m["m"][w+1][k] = p1[2] + 1
            if (m["r"][w][k-1][0] in exlist) and m["m"][w][k-1] == -2:
                q.append([w, k-1, p1[2] + 1])
                m["m"][w][k-1] = p1[2] + 1
            if (m["r"][w][k+1][0] in exlist) and m["m"][w][k+1] == -2:
                q.append([w, k+1, p1[2] + 1])
                m["m"][w][k+1] = p1[2] + 1

            if (m["r"][w-1][k-1][0] in exlist) and m["m"][w-1][k-1] == -2:
                q.append([w-1, k-1, p1[2] + 1])
                m["m"][w-1][k-1] = p1[2] + 1
            if (m["r"][w+1][k-1][0] in exlist) and m["m"][w+1][k-1] == -2:
                q.append([w+1, k-1, p1[2] + 1])
                m["m"][w+1][k-1] = p1[2] + 1
            if (m["r"][w-1][k+1][0] in exlist) and m["m"][w-1][k+1] == -2:
                q.append([w-1, k+1, p1[2] + 1])
                m["m"][w-1][k+1] = p1[2] + 1
            if (m["r"][w+1][k+1][0] in exlist) and m["m"][w+1][k+1] == -2:
                q.append([w+1, k+1, p1[2] + 1])
                m["m"][w+1][k+1] = p1[2] + 1

    t = []
    for it in range(len(a)):
        q = a[it]
        if q["head"]+zero3(it+500) == m["r"][q["y"]][q["x"]][:4] and m["m"][q["y"]][q["x"]] < q["hear_range"]:
            if q["time_sleep"] == 0:
                if m["m"][q["y"]][q["x"]] == 0:
                    if enemies_class_shot(m["r"], [q["y"], q["x"]], [p["y"], p["x"]], q["hear_range"]):
                        enemies_class_attack(p, q["head"], q["attack"])
                else:
                    t.append(it)
            else:
                q["time_sleep"] -= 1
    while t != []:
        it = t.pop(randint(0, len(t)-1))
        q = a[it]
        t_mmap = [[m["m"][q["y"]-1][q["x"]-1], q["y"]-1, q["x"]-1],
                  [m["m"][q["y"]-1][q["x"]], q["y"]-1, q["x"]],
                  [m["m"][q["y"]-1][q["x"]+1], q["y"]-1, q["x"]+1],
                  [m["m"][q["y"]][q["x"]-1], q["y"], q["x"]-1],
                  #[m["m"][q["y"]][q["x"]], q["y"], q["x"]], # stay -PR-
                  [m["m"][q["y"]][q["x"]+1], q["y"], q["x"]+1],
                  [m["m"][q["y"]+1][q["x"]-1], q["y"]+1, q["x"]-1],
                  [m["m"][q["y"]+1][q["x"]], q["y"]+1, q["x"]],
                  [m["m"][q["y"]+1][q["x"]+1], q["y"]+1, q["x"]+1],
                  ]
        p_min = m["m"][q["y"]][q["x"]]
        direction = [m["m"][q["y"]][q["x"]], q["y"], q["x"]] # stay -PR-

        while t_mmap != []:
            i = t_mmap.pop(randint(0, len(t_mmap)-1))
            if i[0] >= 0 and i[0] <= p_min:
                p_min = i[0]
                direction = i
        m["r"][q["y"]][q["x"]] = m["r"][q["y"]][q["x"]][4:]
        #if m["r"][q["y"]][q["x"]] == "":
        #    m["r"][q["y"]][q["x"]] = " "
        #    print("CUT OFF WORNING, I DON'T KNOW WHY")
        if m["v"][q["y"]][q["x"]][0] != " ":
            m["v"][q["y"]][q["x"]] = m["r"][q["y"]][q["x"]]
        if m["r"][direction[1]][direction[2]][0] in tlist: # move an enemie? -PR-
            q["y"], q["x"] = direction[1:]
        m["r"][q["y"]][q["x"]] = q["head"]+zero3(it+500)+m["r"][q["y"]][q["x"]]
        if m["r"][q["y"]][q["x"]][-1] != " ":
            m["v"][q["y"]][q["x"]] = m["r"][q["y"]][q["x"]]
    #for y in range(len(m["m"])):
    #    for x in range(len(m["m"][0])):
    #        m["m"][y][x] = str(m["m"][y][x])[0]

# enemies attacks player

def enemies_class_shot(rmap, e, p, hear_range):
    dire = [0, 0] # direction -PR-
    if p[0] < e[0]:
        dire[0] = 1
    elif p[0] > e[0]:
        dire[0] = -1
    if p[1] < e[1]:
        dire[1] = 1
    elif p[1] > e[1]:
        dire[1] = -1
    if abs(p[0] - e[0]) + abs(p[1] - e[1]) <= hear_range:
        return True
    elif p[0]+dire[0] == e[0] and p[1]+dire[1] == e[1]:
        return True
    return False

def enemies_class_attack(p,head, value):
    if randint(0, 99) < p["armor_acc"]:
        value += randint(-value//2, value//2)-p["armor"]
        if value < 0:
            value = 0
        p["hp"] -= value
        p["wasattackby"] += head

# player attack enemies

def enemies_class_is_shoted(m, p, dire, value):
    ty, tx = p["y"], p["x"]
    r = 0
    while m["r"][ty][tx][0] in tlist:
        ty, tx, r = ty+dire[0], tx+dire[1], r+1
    p["BP"][p["arrows_id"]]["values"][0] -= 1
    if r < 8 and m["r"][ty][tx][0] in exlist:
        it = int(m["r"][ty][tx][1:4])
        enemies_class_is_attacked(m, p, it, value, True)
        return ()
    p["echo"] = translate("YOU SHOT SOMEWERE")

def enemies_class_is_attacked(m, p, it, value, ranged = False):
    if randint(0, 99) < (p["bow_acc"] if ranged else p["attack_acc"]):
        for _ in range((p["bow_attacks"] if ranged else p["attack_attacks"])):
            value += randint(-value//2, value//2)
        if it >= 500:
            q = a[it-500]
        else:
            q = c[it]
        q["hp"] -= value
        if ranged:
            p["echo"] = translate("YOU HIT IT") +" |"+str(value)+"|"+(str(q["hp"]) if q["hp"] > 0 else "die")+"|"
        else:
            p["echo"] = translate("YOU HIT IT") +" |"+str(value)+"|"+(str(q["hp"]) if q["hp"] > 0 else "die")+"|"
        if q["hp"] <= 0:
            m["r"][q["y"]][q["x"]] = m["r"][q["y"]][q["x"]][4:]
            if m["v"][q["y"]][q["x"]][0] == q["head"]:
                m["v"][q["y"]][q["x"]] = m["r"][q["y"]][q["x"]]
            p["xp"] += q["xp"]
    else:
        p["echo"] = translate("YOU MISS IT")
