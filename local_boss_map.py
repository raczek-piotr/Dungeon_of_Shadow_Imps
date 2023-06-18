from random import randint, choice

from local_scripts import zero3
from local_item_class import item_class_init
from local_enemies_class import enemies_class_init


def boss_map_init(m, p, items, enemies, type_of_map, stairs): #enemies → list of list -PR-    pokoje = []
    sizey, sizex = 12, 20
    pokoje = []
    m["sy"], m["sx"] = 2*sizey+1, 2*sizex+1
    m["r"] = [["#" for _ in range(m["sx"])] for _ in range(m["sy"])]
    m["v"] = [[" " for _ in range(m["sx"])] for _ in range(m["sy"])]
    m["o"] = [[" " for _ in range(m["sx"])] for _ in range(m["sy"])]

    # the boss room -PR-
    sy, sx = 7, 7
    y, x = 1+2*randint(0, sizey - sy), 1+2*randint(0, sizex - sx)
    pokoje.append([y, x, sy, sx, ["7x7", "B"]])

    qq = '''
    hm = 3 # royal big rooms -PR-
    minhm = 3
    tryes = 0
    while len(pokoje) < minhm and tryes < hm:
        sy, sx = 11, 17
        y, x = 1+2*randint(0, sizey - sy), 1+2*randint(0, sizex - sx)
        can, tryes = True, tryes + 1
        for i in pokoje:
            if ((abs((i[0]+i[2])-(y+sy)) < i[2]+sy and
                 abs((i[1]+i[3])-(x+sx)) < i[3]+sx)):
                can = False
        if can:
            pokoje.append([y, x, sy, sx])
            continue

    hm = 15 # regular rooms -PR-
    minhm = 10
    tryes = 0
    while len(pokoje) < minhm and tryes < hm:
        sy, sx = 1+2*randint(1,2), 1+2*randint(1,3)
        y, x = 1+2*randint(0, sizey - sy), 1+2*randint(0, sizex - sx)
        can, tryes = True, tryes + 1
        for i in pokoje:
            if ((abs((i[0]+i[2])-(y+sy)) < i[2]+sy and
                 abs((i[1]+i[3])-(x+sx)) < i[3]+sx)):
                can = False
        if can:
            pokoje.append([y, x, sy, sx])
            continue
    hm = len(pokoje)
'''

    # big rooms -PR-
    tryes = 0
    while tryes < 10:
        sy, sx = 1+2*randint(3,3), 1+2*randint(2,3)
        y, x = 1+2*randint(0, sizey - sy), 1+2*randint(0, sizex - sx)
        can, tryes = True, tryes + 1
        for i in pokoje:
            if ((abs((i[0]+i[2])-(y+sy)) < i[2]+sy and
                 abs((i[1]+i[3])-(x+sx)) < i[3]+sx)):
                can = False
        if can:
            xy = str(sx)+"x"+str(sy)
            with open("maps/"+xy+"/"+xy+".cfg", "r") as txt:
                cfg = txt.read().split("\n")
            while cfg[-1] == "":
                cfg.pop(-1)
            print("can")
            t = choice([chr(z+65) for z in range(len(cfg))])

            pokoje.append([y, x, sy, sx, [xy, t]])

    # small rooms -PR-
    tryes = 0
    while tryes < 25 or len(pokoje) < 3:
        sy, sx = 3,5
        y, x = 1+2*randint(0, sizey - sy), 1+2*randint(0, sizex - sx)
        can, tryes = True, tryes + 1
        for i in pokoje:
            if ((abs((i[0]+i[2])-(y+sy)) < i[2]+sy and
                 abs((i[1]+i[3])-(x+sx)) < i[3]+sx)):
                can = False
        if can:
            xy = "5x3"
            with open("maps/"+xy+"/"+xy+".cfg", "r") as txt:
                cfg = txt.read().split("\n")
            while cfg[-1] == "":
                cfg.pop(-1)
            print("can")
            t = choice([chr(z+65) for z in range(len(cfg))])

            pokoje.append([y, x, sy, sx, [xy, t]])

    hm = len(pokoje)
    MaskMaker(m, pokoje, hm)

    #for it in range(hm):
    #    for y in range(pokoje[it][0]-1, pokoje[it][0] + pokoje[it][2] +1):
    #        for x in range(pokoje[it][1]-1, pokoje[it][1] + pokoje[it][3] +1):
    #            m["r"][y][x] = "|"
    Spokoje = sorted(pokoje.copy(), key = lambda p: p[1]) #Sort+pokoje -PR-
    for it in range(len(pokoje)):
        RegularConnect(m, Spokoje[it-1].copy(), Spokoje[it].copy())
    #for it in range(hm):
    #    for y in range(pokoje[it][0], pokoje[it][0] + pokoje[it][2]):
    #        for x in range(pokoje[it][1], pokoje[it][1] + pokoje[it][3]):
    #            m["r"][y][x] = "_."
    #for it in range(hm):
    #    for y in range(pokoje[it][0]-1, pokoje[it][0] + pokoje[it][2] +1):
    #        for x in range(pokoje[it][1]-1, pokoje[it][1] + pokoje[it][3] +1):
    #            if m["r"][y][x] == "|":
    #                m["r"][y][x] = "#"
    ContMaker(m, pokoje, hm)
    for it in range(hm):
        for y in range(pokoje[it][0]-1, pokoje[it][0] + pokoje[it][2] +1):
            for x in range(pokoje[it][1]-1, pokoje[it][1] + pokoje[it][3] +1):
                if m["r"][y][x] == "|":
                    m["r"][y][x] = "#"
    #for it in range(3):
     #   for y in range(pokoje[it][0]+2, pokoje[it][0]+8+6, 6):
    #        for x in range(pokoje[it][1]+2, pokoje[it][1]+17+3, 3):
    #            m["r"][y][x] = "#"

    qq = '''l_pokoje = hm-2
    i = randint(1, l_pokoje)
    j = [pokoje[i][0]+randint(0, pokoje[i][2]-1), pokoje[i][1]+randint(0, pokoje[i][3]-1)]
    for k in items:
        while m["r"][j[0]][j[1]] != "_.":
            i = randint(1, l_pokoje)
            j = [pokoje[i][0]+randint(0, pokoje[i][2]-1), pokoje[i][1]+randint(0, pokoje[i][3]-1)]
        m["r"][j[0]][j[1]] = "_"+k+"."
    print("itemd")
    for k in enemies:
        i = randint(1, l_pokoje)
        j = [pokoje[i][0]+randint(0, pokoje[i][2]-1), pokoje[i][1]+randint(0, pokoje[i][3]-1)]
        while m["r"][j[0]][j[1]] != "_.":
            i = randint(1, l_pokoje)
            j = [pokoje[i][0]+randint(0, pokoje[i][2]-1), pokoje[i][1]+randint(0, pokoje[i][3]-1)]
        e_id = enemies_class_init(k[0], j[0], j[1], k[1], k[2], k[3], k[4], k[5], k[6], k[7])
        m["r"][j[0]][j[1]] = "_"+k[0]+zero3(e_id)+"."'''

    e_id = enemies_class_init("B", pokoje[0][0]+pokoje[0][2]//2, pokoje[0][1]+pokoje[0][3]//2,
                              12, 5, 15, 1, 30, False, [])
    m["r"][pokoje[0][0]+pokoje[0][2]//2][pokoje[0][1]+pokoje[0][3]//2] = "B"+zero3(e_id)+" "
    print("enemid")

    if stairs > 1:
        m["r"][pokoje[-1][0]+pokoje[-1][2]//2][pokoje[-1][1]+pokoje[-1][3]//2] = "_=>."
    if stairs % 2 == 1:
        m["r"][pokoje[-2][0]+pokoje[-2][2]//2][pokoje[-2][1]+pokoje[-2][3]//2] = "_=<."

    return(pokoje[-1][0]+pokoje[-1][2]//2, pokoje[-1][1]+pokoje[-1][3]//2)

def MaskMaker(m, pokoje, hm):
    for it in range(hm):
        xy, t = pokoje[it][4]
        with open("maps/"+xy+"/"+t+"_mask.cfg", "r") as q:
            q = q.read().split("\n")
            while q[-1] == "":
                q.pop(-1)
            for y in range(len(q)):
                w = q[y].split(";")
                for x in range(len(w)):
                    e = w[x]
                    if e != "-":
                        m["r"][y+pokoje[it][0]-1][x+pokoje[it][1]-1] = e

def ContMaker(m, pokoje, hm): #ContentMaker → room -PR-
    for it in range(hm):
        xy, t = pokoje[it][4]
        with open("maps/"+xy+"/"+t+"_cont.cfg", "r") as q: #(cont)ent
            q = q.read().split("\n")
            while q[-1] == "":
                q.pop(-1)
            for y in range(len(q)):
                w = q[y].split(";")
                for x in range(len(w)):
                    e = w[x]
                    if e != "-":
                        m["r"][y+pokoje[it][0]][x+pokoje[it][1]] = e

def RegularConnect(m, p_end, p_start):
    #p_end[0], p_end[1] = p_end[0] + 2*p_end[2]//4, p_end[1] + 2*p_end[3]//4
    #p_start[0], p_start[1] = p_start[0] + 2*p_start[2]//4, p_start[1] + 2*p_start[3]//4
    direction = randint(0, 1)
    goal = True # I have the goal -PR-
    print(p_start, p_end)
    while goal:
        if direction == 0:
            if p_start[0] < p_end[0]:
                k = p_start[0]+1
            elif p_start[0] > p_end[0]:
                k = p_start[0]-1
            else:
                k = p_start[0]
                direction += 1
            if m["r"][k][p_start[1]] in {"+", "|"}:
                m["r"][k][p_start[1]] = "+"
            #elif m["r"][k][p_start[1]] == " ":
            #    goal = False
            else:
                m["r"][k][p_start[1]] = " "
            p_start[0] = 2*k-p_start[0]
            m["r"][p_start[0]][p_start[1]] = " "
        else:
            if p_start[1] < p_end[1]:
                k = p_start[1]+1
            elif p_start[1] > p_end[1]:
                k = p_start[1]-1
            else:
                k = p_start[1]
                direction -= 1
            if m["r"][p_start[0]][k] in {"+", "|"}:
                m["r"][p_start[0]][k] = "+"
            #elif m["r"][p_start[0]][k] == " ":
            #    goal = False
            else:
                m["r"][p_start[0]][k] = " "
            p_start[1] = 2*k-p_start[1]
            m["r"][p_start[0]][p_start[1]] = " "
        if p_start[0] == p_end[0] and p_start[1] == p_end[1]:
            goal = False
        if randint(0, 99) < 20:
            direction = (direction+1) % 2