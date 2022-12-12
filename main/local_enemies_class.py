from random import randint
from local_zero3 import zero3

def enemies_class_clear():
    global c, a, mhr, tlist, exlist # c - class, mhr - max hear range -PR-
    tlist = [".",","," ","]","}",")","$","~","-","!","?","<",">"]
    exlist = tlist.copy()
    c, a, mhr = [], [], 1

def enemies_class_init(head, y, x, hp = 8, attack = 2, xp = 1, time_sleep = 1, hear_range = 5, ranged = False, carring = []):
    global c, a, mhr, exlist
    if ranged:
        a.append({"head": head, "y": y, "x": x, "mhp": hp, "hp": hp, "attack": attack, "xp": xp,
            "time_sleep": time_sleep, "hear_range": hear_range, "carring": carring})
    else:
        c.append({"head": head, "y": y, "x": x, "mhp": hp, "hp": hp, "attack": attack, "xp": xp,
            "time_sleep": time_sleep, "hear_range": hear_range, "carring": carring})
    if mhr < hear_range-1:
        mhr = hear_range-1
    if head not in exlist:
        exlist.append(head)
    return(len(c)-1)  # return id -PR-

def enemies_class_update(m, p):
    global c, a, mhr, tlist, exlist
    m["m"] = [[-1 for _ in range(m["sy"])] for _ in range(m["sx"])]
    w, k = p[0], p[1] # row kolumn -PR-
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
    for i in range(len(c)):
        if c[i]["hp"] > 0 and c[i]["head"] == m["r"][c[i]["y"]][c[i]["x"]][0] and m["m"][c[i]["y"]][c[i]["x"]] < c[i]["hear_range"]:
            if c[i]["time_sleep"] == 0:
                if m["m"][c[i]["y"]][c[i]["x"]] == 0:
                    pass
                else:
                    t.append(i)
            else:
                c[i]["time_sleep"] -= 1
    while t != []:
        id = t.pop(randint(0, len(t)-1))
        t_mmap = [[m["m"][c[id]["y"]-1][c[id]["x"]-1], c[id]["y"]-1, c[id]["x"]-1],
                  [m["m"][c[id]["y"]-1][c[id]["x"]], c[id]["y"]-1, c[id]["x"]],
                  [m["m"][c[id]["y"]-1][c[id]["x"]+1], c[id]["y"]-1, c[id]["x"]+1],
                  [m["m"][c[id]["y"]][c[id]["x"]-1], c[id]["y"], c[id]["x"]-1],
                  #[m["m"][c[id]["y"]][c[id]["x"]], c[id]["y"], c[id]["x"]], # stay -PR-
                  [m["m"][c[id]["y"]][c[id]["x"]+1], c[id]["y"], c[id]["x"]+1],
                  [m["m"][c[id]["y"]+1][c[id]["x"]-1], c[id]["y"]+1, c[id]["x"]-1],
                  [m["m"][c[id]["y"]+1][c[id]["x"]], c[id]["y"]+1, c[id]["x"]],
                  [m["m"][c[id]["y"]+1][c[id]["x"]+1], c[id]["y"]+1, c[id]["x"]+1],
                  ]
        p_min = m["m"][c[id]["y"]][c[id]["x"]]
        direction = [m["m"][c[id]["y"]][c[id]["x"]], c[id]["y"], c[id]["x"]] # stay -PR-

        while t_mmap != []:
            i = t_mmap.pop(randint(0, len(t_mmap)-1))
            if i[0] >= 0 and i[0] <= p_min:
                p_min = i[0]
                direction = i
        m["r"][c[id]["y"]][c[id]["x"]] = m["r"][c[id]["y"]][c[id]["x"]][4:]
        m["v"][c[id]["y"]][c[id]["x"]] = m["r"][c[id]["y"]][c[id]["x"]]
        if m["r"][c[id]["y"]][c[id]["x"]] == "":
            m["r"][c[id]["y"]][c[id]["x"]] = " "
            print(1+"CUT OFF ERROR")
        if m["r"][direction[1]][direction[2]] in tlist: # move an enemie? -PR-
            c[id]["y"], c[id]["x"] = direction[1:]
        m["r"][c[id]["y"]][c[id]["x"]] = c[id]["head"]+zero3(id)+m["r"][c[id]["y"]][c[id]["x"]]
        if m["r"][c[id]["y"]][c[id]["x"]][-1] != " ":
            m["v"][c[id]["y"]][c[id]["x"]] = m["r"][c[id]["y"]][c[id]["x"]]



    print("run1")
    for y in range(len(m["m"])): # time for archers -PR-
        for x in range(len(m["m"][0])):
            if m["m"][y][x] != -1:
                m["m"][y][x] = -2
    w, k = p[0], p[1]
    print("run2")
    q = [] # it isn't needed -PR-
    for i in [[1,1],[1,0],[1,-1],[0,1],[0,-1],[-1,1],[-1,0],[-1,-1]]:
        w, k = p[0]+i[0], p[1]+i[1]
        while m["m"][w][k] == -2:
            q.append([w, k, 0])
            m["m"][w][k] = 0
            w, k = w +i[0], k +i[1]
    print("run3")
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
    print("run4")

    t = []
    for i in range(len(a)):
        if a[i]["hp"] > 0 and a[i]["head"] == m["r"][a[i]["y"]][a[i]["x"]][0] and m["m"][a[i]["y"]][a[i]["x"]] < a[i]["hear_range"]:
            if a[i]["time_sleep"] == 0:
                if m["m"][a[i]["y"]][a[i]["x"]] == 0:
                    pass
                else:
                    t.append(i)
            else:
                a[i]["time_sleep"] -= 1
    while t != []:
        id = t.pop(randint(0, len(t)-1))
        t_mmap = [[m["m"][a[id]["y"]-1][a[id]["x"]-1], a[id]["y"]-1, a[id]["x"]-1],
                  [m["m"][a[id]["y"]-1][a[id]["x"]], a[id]["y"]-1, a[id]["x"]],
                  [m["m"][a[id]["y"]-1][a[id]["x"]+1], a[id]["y"]-1, a[id]["x"]+1],
                  [m["m"][a[id]["y"]][a[id]["x"]-1], a[id]["y"], a[id]["x"]-1],
                  #[m["m"][a[id]["y"]][a[id]["x"]], a[id]["y"], a[id]["x"]], # stay -PR-
                  [m["m"][a[id]["y"]][a[id]["x"]+1], a[id]["y"], a[id]["x"]+1],
                  [m["m"][a[id]["y"]+1][a[id]["x"]-1], a[id]["y"]+1, a[id]["x"]-1],
                  [m["m"][a[id]["y"]+1][a[id]["x"]], a[id]["y"]+1, a[id]["x"]],
                  [m["m"][a[id]["y"]+1][a[id]["x"]+1], a[id]["y"]+1, a[id]["x"]+1],
                  ]
        p_min = m["m"][a[id]["y"]][a[id]["x"]]
        direction = [m["m"][a[id]["y"]][a[id]["x"]], a[id]["y"], a[id]["x"]] # stay -PR-

        while t_mmap != []:
            i = t_mmap.pop(randint(0, len(t_mmap)-1))
            if i[0] >= 0 and i[0] <= p_min:
                p_min = i[0]
                direction = i
        m["r"][a[id]["y"]][a[id]["x"]] = m["r"][a[id]["y"]][a[id]["x"]][4:]
        m["v"][a[id]["y"]][a[id]["x"]] = m["r"][a[id]["y"]][a[id]["x"]]
        if m["r"][a[id]["y"]][a[id]["x"]] == "":
            m["r"][a[id]["y"]][a[id]["x"]] = " "
            print(1+"CUT OFF ERROR")
        print(direction)
        if m["r"][direction[1]][direction[2]] in tlist: # move an enemie? -PR-
            a[id]["y"], a[id]["x"] = direction[1:]
        m["r"][a[id]["y"]][a[id]["x"]] = a[id]["head"]+zero3(id)+m["r"][a[id]["y"]][a[id]["x"]]
        if m["r"][a[id]["y"]][a[id]["x"]][-1] != " ":
            m["v"][a[id]["y"]][a[id]["x"]] = m["r"][a[id]["y"]][a[id]["x"]]
    #for y in range(len(m["m"])):
    #    for x in range(len(m["m"][0])):
    #        m["m"][y][x] = str(m["m"][y][x])[0]

#def enemies_class_get(i): #all from 1 enemie -PR-
#    global c
#    return(c[i])
