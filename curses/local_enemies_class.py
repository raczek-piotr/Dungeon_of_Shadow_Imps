from random import randint, choice
from local_scripts import zero3, dire, shot
from local_translator import translate
from local_scripts import is_boss_killed


enemies_likes_light = [
    ["m",3,2,2,1,7,"drop","min_lw_to_give_xp",1,4,"MICE", 0],
    ["m",3,2,2,1,7,"drop","min_lw_to_give_xp",1,4,"MICE", 0],
    ["f",3,1,1,1,7,"drop","min_lw_to_give_xp",1,4,"FLY", 0],
    ["f",3,1,1,1,7,"drop","min_lw_to_give_xp",1,4,"FLY", 0],

    ["a",3,2,3,1,7,"drop","min_lw_to_give_xp",3,10,"ANT THE ACID FROWER", 1],
    ["a",3,2,3,1,7,"drop","min_lw_to_give_xp",3,10,"ANT THE ACID FROWER", 1],

    ["b",8,3,8,1,7,"drop","min_lw_to_give_xp",5,20,"BAT", 0],
    ["S",6,4,4,4,4,"drop","min_lw_to_give_xp",5,20,"SNAKE", 0],
    ]
enemies_half_light = [
    ["r",4,1,4,1,7,"drop","min_lw_to_give_xp",1,4,"RAT", 0],
    ["m",3,2,2,1,7,"drop","min_lw_to_give_xp",1,4,"MICE", 0],
    ["f",3,1,1,1,7,"drop","min_lw_to_give_xp",1,4,"FLY", 0],

    ["f",3,1,1,1,7,"drop","min_lw_to_give_xp",3,10,"FLY", 0], # special fly -PR-
    ["c",6,1,2,1,7,"drop","min_lw_to_give_xp",3,10,"CENTIPEDE", 0],
    ["a",3,2,3,1,7,"drop","min_lw_to_give_xp",3,10,"ANT THE ACID FROWER", 1],

    ["b",8,3,8,1,7,"drop","min_lw_to_give_xp",5,20,"BAT", 0],
    ["S",6,4,4,4,4,"drop","min_lw_to_give_xp",5,20,"SNAKE", 0],
    ]
enemies_not_light = [
    ["r",4,1,4,1,7,"drop","min_lw_to_give_xp",1,4,"RAT", 0],
    ["r",4,1,4,1,7,"drop","min_lw_to_give_xp",1,4,"RAT", 0],

    ["c",6,1,2,1,7,"drop","min_lw_to_give_xp",3,10,"CENTIPEDE", 0],
    ["c",6,1,2,1,7,"drop","min_lw_to_give_xp",3,10,"CENTIPEDE", 0],
    ["c",6,1,2,1,7,"drop","min_lw_to_give_xp",3,10,"CENTIPEDE", 0],

    ["b",8,3,8,1,7,"drop","min_lw_to_give_xp",5,20,"BAT", 0],
    ["S",6,4,4,4,4,"drop","min_lw_to_give_xp",5,20,"SNAKE", 0],
    ]

all_enemies = [enemies_likes_light, enemies_half_light, enemies_not_light, enemies_half_light]


def enemies_class_clear():
    global c, a, tlist, exlist, heads, elist # c - class, exlist - tlist + heads -PR-
    tlist = {".",","," ","]","}",")","$","~","-","*","!","?","<",">"}
    exlist = tlist.copy() # = tlist + heads -PR-
    heads = set()
    c, a = [], []
    elist = [] # tmp list for enemies -PR-

def enemies_class_add(x, y, type_of, lw): #carring is not used now -PR-
    #global enemies_likes_light, enemies_half_light, enemies_not_light
    enemies = all_enemies[type_of%4]
    global c, a, exlist, heads, elist
    if elist == []:
        for e in enemies:
            if e[8] <= lw and e[9] >= lw:
                for _ in range(randint(1,4)):
                    elist.append(e)

    e = elist.pop(randint(0,len(elist)-1)).copy() # enemie -PR-
    e[8], e[9] = x, y
    if e[11]%2 == 1:
        q, it = a, len(a)+500
    else:
        q, it = c, len(c)
    head = e[0]
    if head not in exlist:
        exlist.add(head), heads.add(head)
    q.append(e)
    return head+zero3(it), elist != [] # return id -PR-

def enemies_class_update(m, p, yx):
    global c, a, tlist, exlist
    q = 0
    while q != 0:
        q -= 1
    m["m"] = [[-1 for _ in range(m["sx"])] for _ in range(m["sy"])]
    w, k = yx[0], yx[1] # row kolumn -PR-
    q = [[w, k, -1]]
    while q != []:
        p1 = q.pop(0)
        if p1[2] <= 7:
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
        if q[0]+zero3(it) == m["r"][q[9]][q[8]][:4] and m["m"][q[9]][q[8]] < q[5]: # q[1] > 0 he won't be on the map! -PR-
            if q[4] == 0:
                if m["m"][q[9]][q[8]] == 0:
                    enemies_class_attack(p, q[0], q[2])
                else:
                    t.append(it)
            else:
                q[4] -= 1
    while t != []:
        it = t.pop(randint(0, len(t)-1)) # it = id
        q = c[it]
        t_mmap = [[m["m"][q[9]-1][q[8]-1], q[9]-1, q[8]-1],
                  [m["m"][q[9]-1][q[8]], q[9]-1, q[8]],
                  [m["m"][q[9]-1][q[8]+1], q[9]-1, q[8]+1],
                  [m["m"][q[9]][q[8]-1], q[9], q[8]-1],
                  #[m["m"][q[9]][q[8]], q[9], q[8]], # stay -PR-
                  [m["m"][q[9]][q[8]+1], q[9], q[8]+1],
                  [m["m"][q[9]+1][q[8]-1], q[9]+1, q[8]-1],
                  [m["m"][q[9]+1][q[8]], q[9]+1, q[8]],
                  [m["m"][q[9]+1][q[8]+1], q[9]+1, q[8]+1],
                  ]
        move_enemie(m, p, t_mmap, q, it)

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
        if p1[2] <= 7:
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
        if q[0]+zero3(it+500) == m["r"][q[9]][q[8]][:4] and m["m"][q[9]][q[8]] < q[5]:
            if q[4] == 0:
                if m["m"][q[9]][q[8]] == 0:
                    if enemies_class_shot(m["r"], [q[9], q[8]], [p["y"], p["x"]], q[5]):
                        enemies_class_attack(p, q[0], q[2])
                else:
                    t.append(it)
            else:
                q[4] -= 1
    while t != []:
        it = t.pop(randint(0, len(t)-1))
        q = a[it]
        t_mmap = [[m["m"][q[9]-1][q[8]-1], q[9]-1, q[8]-1],
                  [m["m"][q[9]-1][q[8]], q[9]-1, q[8]],
                  [m["m"][q[9]-1][q[8]+1], q[9]-1, q[8]+1],
                  [m["m"][q[9]][q[8]-1], q[9], q[8]-1],
                  #[m["m"][q[9]][q[8]], q[9], q[8]], # stay -PR-
                  [m["m"][q[9]][q[8]+1], q[9], q[8]+1],
                  [m["m"][q[9]+1][q[8]-1], q[9]+1, q[8]-1],
                  [m["m"][q[9]+1][q[8]], q[9]+1, q[8]],
                  [m["m"][q[9]+1][q[8]+1], q[9]+1, q[8]+1],
                  ]
        move_enemie(m, p, t_mmap, q, it, 500)

def move_enemie(m, p, t_mmap, q, it, plus_it = 0):
    p_min = m["m"][q[9]][q[8]]
    direction = [m["m"][q[9]][q[8]], q[9], q[8]] # stay -PR-
    while t_mmap != []:
        i = t_mmap.pop(randint(0, len(t_mmap)-1))
        if i[0] >= 0 and i[0] <= p_min:
            p_min = i[0]
            direction = i
    m["r"][q[9]][q[8]] = m["r"][q[9]][q[8]][4:]
    #if m["r"][q[9]][q[8]] == "":
    #    m["r"][q[9]][q[8]] = " "
    if m["v"][q[9]][q[8]][0] != " ": # if viewmap is unseen -PR-
        m["v"][q[9]][q[8]] = m["r"][q[9]][q[8]]
    if m["r"][direction[1]][direction[2]][0] in tlist: # move an enemie? -PR-
        if m["r"][direction[1]][direction[2]] != "  ": # divine -PR-
            q[9], q[8] = direction[1:]
        else:
            q[1] = 0
    m["r"][q[9]][q[8]] = q[0]+zero3(it+plus_it)+m["r"][q[9]][q[8]]
    if m["r"][q[9]][q[8]][-1] != " ":
        m["v"][q[9]][q[8]] = m["r"][q[9]][q[8]]
    if q[1] == 0: # no xp for the player who did NOT kill him -PR-
        is_boss_killed(m, p, q[0]) # but It was a Boss?
        m["r"][q[9]][q[8]] = m["r"][q[9]][q[8]][4:]
        if m["v"][q[9]][q[8]][0] == q[0]:
            m["v"][q[9]][q[8]] = m["r"][q[9]][q[8]]

# enemies attacks player

def enemies_class_shot(rmap, e, p, hear_range):#  = 7): in shot -PR-
    global tlist
    d = dire(e, p)
    p = shot(rmap, p, d, tlist, (hear_range if hear_range <= 7 else 7))
    return p == e

def enemies_class_attack(p, head, value):
    if randint(0, 99) < p["armor_acc"]:
        value += randint(-value//2, value//2)-p["armor"]
        if value < 0:
            value = 0
        p["hp"] -= value
        p["wasattackby"] += head

# player attack enemies

def enemies_class_is_shoted(m, p, dire, value):
    global tlist, heads
    tx = p["y"], p["x"] # it is NOT x'pos -PR-
    ty, tx = shot(m["r"], tx, dire, tlist)
    p["BP"][p["arrows_id"]]["values"][0] -= 1
    if m["r"][ty][tx][0] in heads:
        it = int(m["r"][ty][tx][1:4])
        enemies_class_is_attacked(m, p, it, value, True)
        return ()
    p["echo"] = translate("YOU SHOT SOMEWERE")

def enemies_class_is_attacked(m, p, it, value, ranged = False):
    if it >= 500:
        q = a[it-500]
    else:
        q = c[it]
    at_value = 0
    acc = (p["bow_acc"] if ranged else p["attack_acc"])
    attacks = (p["bow_attacks"] if ranged else p["attack_attacks"])
    if q[4] != 0:
        at_value = value * attacks
        acc = 100
        q[4] = 0
    for _ in range(attacks):
        at_value += (randint(0, 99) < acc) * (value + randint(-value//2, value//2))
    if at_value != 0:
        q[1] -= at_value
        q[4], q[5] = 0, 7 # fast wake up -PR- and alarmed
        p["echo"] = translate("YOU HIT A")+" "+translate(q[10])
        if q[1] <= 0:
            m["r"][q[9]][q[8]] = m["r"][q[9]][q[8]][4:]
            if m["v"][q[9]][q[8]][0] == q[0]:
                m["v"][q[9]][q[8]] = m["r"][q[9]][q[8]]
            p["xp"] += q[3]
            p["echo"] = translate("YOU KILL A")+" "+translate(q[10])
            is_boss_killed(m, p, q[0])
    else:
        p["echo"] = translate("YOU MISS A")+" "+translate(q[10])
