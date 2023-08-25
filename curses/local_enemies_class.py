from random import randint, choice
from local_scripts import zero3, dire, shot
from local_translator import translate
from local_scripts import is_boss_killed


def flag(f, n):
    return f%(2*n)//n
# flags
# 1 - is a shooter
# 2 - poison (armor penetration)
# 4 - random movement 50% (always)
# 8 - when not sleeping and there is no player in range, then random movement (seeks player)
e = [
    ["r",4,2,3,1,5,"drop",5,1,5,"RAT", 8], #0
    ["m",3,2,2,1,5,"drop",5,1,5,"MICE", 0], #1
    ["f",1,2,1,0,3,"drop",5,1,5,"FLY", 10], #2
    ["u",10,3,11,0,7,"drop",10,6,10,"URCHIN", 9], #3
    ["w",7,3,4,5,7,"drop",10,6,10,"WORM", 0], #4
    ["c",5,4,4,2,4,"drop",10,6,10,"CENTIPEDE", 0], #5
    ["S",12,9,10,3,5,"drop",15,11,15,"SNAKE", 14], #6
    ["b",10,7,5,0,7,"drop",15,11,15,"BAT", 12], #7
    ["F",3,5,5,1,3,"drop",15,11,15,"POISON DART FROG", 2], #8
    ["t",11,6,14,0,7,"drop",20,16,20,"THIEF", 0], #9
    ["a",7,3,10,1,5,"drop",20,16,20,"ANT (the acid shooter)", 3], #10
    ]
enemies_light = [e[1],e[1],e[1],e[1],e[2],e[3],e[5],e[6],e[8],e[8],e[9],e[10]]
enemies_dark = [e[0],e[0],e[0],e[3],e[4],e[7],e[7],e[7],e[8],e[9],e[10]]
#enemies_half = enemies_light+enemies_dark
#enemies_light = enemies_light+enemies_light
#enemies_dark = enemies_dark+enemies_dark
del e # e is used in functions leater, but data isn't deleted -PR-

enemies_part1 = [enemies_light,
                 enemies_light,
                 enemies_dark,
                 enemies_light]
enemies_part2 = [enemies_light,
                 enemies_dark,
                 enemies_dark,
                 enemies_dark]


def enemies_class_clear():
    global c, a, tlist, exlist, heads, elist # c - class, exlist - tlist + heads -PR-
    tlist = {".",","," ","]","}",")","$","~","-","*","!","?","<",">","="}
    exlist = tlist.copy() # = tlist + heads -PR-
    heads = set()
    c, a = [], []
    elist = [] # tmp list for enemies -PR-

def enemies_class_add(x, y, type_of, lw): #carring is not used now -PR-
    #global enemies_likes_light, enemies_half_light, enemies_not_light
    if lw == 0:
        lw = 1
    global c, a, exlist, heads, elist
    if elist == []:
        for e in enemies_part1[type_of%4]:
            if e[8] <= lw and e[9] >= lw:
                for _ in range(2):#randint(2,2)):
                    elist.append(e)
        for e in enemies_part2[type_of%4]:
            if e[8] <= lw and e[9] >= lw:
                for _ in range(2):#randint(2,2)):
                    elist.append(e)
    if elist == []:
        print(enemies_part1[type_of%4][0][8:10])
        while True:
            pass

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

    for it in range(len(c)):
        q = c[it]
        updete_enemie(m, p, q, it)

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

    for it in range(len(a)):
        q = a[it]
        updete_enemie(m, p, q, it, 500)

def updete_enemie(m, p, q, it, plus_it = 0):
    if q[0]+zero3(it+plus_it) == m["r"][q[9]][q[8]][:4]: # could be updated -PR-
        if q[4] == 0: # wake up -PR-
            if flag(q[11], 4) and randint(0,1): # flag 4? -PR-
                randmove(m, p, q, it, plus_it)
                return#break#continue
            if m["m"][q[9]][q[8]] < q[5] and m["m"][q[9]][q[8]] >= 0: # could hear?
                if m["m"][q[9]][q[8]] == 0:
                    if enemies_class_shot(m["r"], [q[9], q[8]], [p["y"], p["x"]], q[5]):
                        enemies_class_attack(p, q[0], q[2], flag(q[11], 2))
                else:
                    move_enemie(m, p, q, it, plus_it)
            else:# flag(q[11], 8): # not sleeping and can't hear the player, flag 8 -PR-
                randmove(m, p, q, it, plus_it)
        elif m["m"][q[9]][q[8]] < q[5] and m["m"][q[9]][q[8]] >= 0: # is sleeping, but would it wake up? -PR-
            q[4] -= 1
    return # formal -PR-

def randmove(m, p, q, it, plus_it):
    direction = [randint(-1,1)+q[9], randint(-1,1)+q[8]]
    if p["x"] == direction[0] and p["y"] == direction[1]:
        return # do not move -PR-

    m["r"][q[9]][q[8]] = m["r"][q[9]][q[8]][4:] # the same -PR-
    #if m["r"][q[9]][q[8]] == "":
    #    m["r"][q[9]][q[8]] = " "
    if m["v"][q[9]][q[8]][0] != " ": # if viewmap is seen -PR-
        m["v"][q[9]][q[8]] = m["r"][q[9]][q[8]]
    if m["r"][direction[0]][direction[1]][0] in tlist: # move an enemie? -PR-
        if m["r"][direction[0]][direction[1]] != "  ": # divine -PR-
            q[9], q[8] = direction
        #else: # on the randmove, enemies don't fall, because they are cautious -PR-
        #    q[1] = 0
    m["r"][q[9]][q[8]] = q[0]+zero3(it+plus_it)+m["r"][q[9]][q[8]]
    if m["r"][q[9]][q[8]][-1] != " ":
        m["v"][q[9]][q[8]] = m["r"][q[9]][q[8]]
    if q[1] == 0: # no xp for the player who did NOT kill him -PR-
        is_boss_killed(m, p, q[0]) # but if it was a Boss?
        m["r"][q[9]][q[8]] = m["r"][q[9]][q[8]][4:]
        if m["v"][q[9]][q[8]][0] == q[0]:
            m["v"][q[9]][q[8]] = m["r"][q[9]][q[8]]

def move_enemie(m, p, q, it, plus_it):
    t_mmap = [[m["m"][q[9]-1][q[8]-1], q[9]-1, q[8]-1], [m["m"][q[9]-1][q[8]], q[9]-1, q[8]], [m["m"][q[9]-1][q[8]+1], q[9]-1, q[8]+1], [m["m"][q[9]][q[8]-1], q[9], q[8]-1], [m["m"][q[9]][q[8]+1], q[9], q[8]+1], [m["m"][q[9]+1][q[8]-1], q[9]+1, q[8]-1], [m["m"][q[9]+1][q[8]], q[9]+1, q[8]], [m["m"][q[9]+1][q[8]+1], q[9]+1, q[8]+1],
              ]
    p_min = m["m"][q[9]][q[8]]
    direction = [m["m"][q[9]][q[8]], q[9], q[8]] # stay -PR-
    while t_mmap != []:
        i = t_mmap.pop(randint(0, len(t_mmap)-1))
        if i[0] >= 0 and i[0] <= p_min:
            p_min = i[0]
            direction = i
    m["r"][q[9]][q[8]] = m["r"][q[9]][q[8]][4:] # the same -PR-
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
        is_boss_killed(m, p, q[0]) # but if it was a Boss?
        m["r"][q[9]][q[8]] = m["r"][q[9]][q[8]][4:]
        if m["v"][q[9]][q[8]][0] == q[0]:
            m["v"][q[9]][q[8]] = m["r"][q[9]][q[8]]

# enemies attacks player

def enemies_class_shot(rmap, e, p, hear_range):#  = 7): in shot -PR-
    global tlist
    d = dire(e, p)
    p = shot(rmap, p, d, tlist, (hear_range if hear_range <= 7 else 7))
    return p == e

def enemies_class_attack(p, head, value, ap):
    if randint(0, 99) >= p["defend"]:
        value += randint(-value//2, value//2)
        if not ap: # standard attack -PR-
            value -= p["armor"]
            if value < 0:
                value = 0
        p["hp"] -= value
        p["wasattackby"] += head

# player attack enemies
def roll (a,b):
    q = 0
    for _ in range(a):
        q += randint(1,b)
    return q


def enemies_class_is_shoted(m, p, dire, value):
    global tlist, heads
    tx = p["y"], p["x"] # it is NOT x'pos -PR-
    ty, tx = shot(m["r"], tx, dire, tlist)
    for ammo_id in range(len(p["BP"])):
        ammo = p["BP"][ammo_id]
        if ammo[0][0] == p["e_hand"][0][2]:
            ammo[2] -= 1
            if ammo[2] == 0:
                p["BP"].pop(ammo_id)
            if m["r"][ty][tx][0] in heads:
                it = int(m["r"][ty][tx][1:4])
                enemies_class_is_attacked(m, p, it, value, True)
                return #()
            p["echo"] = translate("YOU SHOT SOMEWERE")
            return #()
    p["echo"] = translate("NO AMMO")
    return #()

def enemies_class_is_attacked(m, p, it, value, ranged = False): # value - sleep of an enemie
    if it >= 500:
        q = a[it-500]
    else:
        q = c[it]
    at_value = 0
    acc = (p["bow_acc"] if ranged else p["attack_acc"])
    hits = (p["bow_hits"] if ranged else p["attack_hits"])
    if p["blessing"]:
        hits *= 2
    rolls = (p["bow"] if ranged else p["attack"])
    damage = (p["bow_damage"] if ranged else p["attack_damage"])
    if q[4] != 0:
        at_value += value * damage #free wake up hit
        acc = 100
        q[4] = 0
    for _ in range(hits):
        at_value += (randint(0, 99) < acc) * (roll(rolls, damage))
    if at_value != 0:
        if p["fury"]:
            at_value *= 2
        q[1] -= at_value
        q[4], q[5] = 0, 7 # fast wake up -PR- and alarmed
        p["echo"] = translate("YOU HIT A")+" "+translate(q[10])
        if q[1] <= 0:
            m["r"][q[9]][q[8]] = m["r"][q[9]][q[8]][4:]
            if m["v"][q[9]][q[8]][0] == q[0]:
                m["v"][q[9]][q[8]] = m["r"][q[9]][q[8]]
            p["xp"] += q[3] * (q[7] >= p["lw"])
            p["echo"] = translate("YOU KILL A")+" "+translate(q[10])
            is_boss_killed(m, p, q[0])
    else:
        p["echo"] = translate("YOU MISS A")+" "+translate(q[10])
