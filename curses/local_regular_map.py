from random import randint, choice

from local_scripts import zero3
from local_item_class import item_class_init
from local_enemies_class import enemies_class_init


def regular_map_init(m, p, items, enemies, type_of_map, stairs):
    hm = 20
    minhm = 5 # 5 -PR-
    pokoje = []
    tryies = 0
    sizey, sizex = 12, 20
    m["sy"], m["sx"] = 25, 41
    m["r"] = [["#" for _ in range(m["sx"])] for _ in range(m["sy"])]
    m["v"] = [[" " for _ in range(m["sx"])] for _ in range(m["sy"])]
    m["o"] = [[" " for _ in range(m["sx"])] for _ in range(m["sy"])]
    while len(pokoje) < minhm and tryies < hm:
        sy, sx = 1+2*randint(1,2), 1+2*randint(1,3)
        y, x = 1+2*randint(0, sizey - sy), 1+2*randint(0, sizex - sx)
        can, tryies = True, tryies + 1
        for i in pokoje:
            if ((abs((i[0]+i[2])-(y+sy)) < i[2]+sy and
                 abs((i[1]+i[3])-(x+sx)) < i[3]+sx)):
                can = False
        if can:
            pokoje.append([y, x, sy, sx])
            continue

    hm = len(pokoje)
    for it in range(hm):
        for y in range(pokoje[it][0]-1, pokoje[it][0] + pokoje[it][2] +1):
            for x in range(pokoje[it][1]-1, pokoje[it][1] + pokoje[it][3] +1):
                m["r"][y][x] = "|"
    for it in range(hm):
        Connect(m, pokoje[it-1].copy(), pokoje[it].copy())
    for it in range(hm):
        for y in range(pokoje[it][0], pokoje[it][0] + pokoje[it][2]):
            for x in range(pokoje[it][1], pokoje[it][1] + pokoje[it][3]):
                m["r"][y][x] = "_."
    for it in range(hm):
        for y in range(pokoje[it][0]-1, pokoje[it][0] + pokoje[it][2] +1):
            for x in range(pokoje[it][1]-1, pokoje[it][1] + pokoje[it][3] +1):
                if m["r"][y][x] == "|":
                    m["r"][y][x] = "#"
    l_pokoje = hm-2
    i = randint(1, l_pokoje)
    j = [pokoje[i][0]+randint(0, pokoje[i][2]-1), pokoje[i][1]+randint(0, pokoje[i][3]-1)]
    for k in items:
        while m["r"][j[0]][j[1]] != "_.":
            i = randint(1, l_pokoje)
            j = [pokoje[i][0]+randint(0, pokoje[i][2]-1), pokoje[i][1]+randint(0, pokoje[i][3]-1)]
        m["r"][j[0]][j[1]] = "_"+k+"."
    for k in enemies:
        i = randint(1, l_pokoje)
        j = [pokoje[i][0]+randint(0, pokoje[i][2]-1), pokoje[i][1]+randint(0, pokoje[i][3]-1)]
        while m["r"][j[0]][j[1]] != "_.":
            i = randint(1, l_pokoje)
            j = [pokoje[i][0]+randint(0, pokoje[i][2]-1), pokoje[i][1]+randint(0, pokoje[i][3]-1)]
        e_id = enemies_class_init(k[0], j[0], j[1], k[1], k[2], k[3], k[4], k[5], k[6], k[7])
        m["r"][j[0]][j[1]] = "_"+k[0]+zero3(e_id)+"."
    if stairs > 1:
        m["r"][pokoje[-1][0]+pokoje[-1][2]//2][pokoje[-1][1]+pokoje[-1][3]//2] = "_>."
    if stairs % 2 == 1:
        m["r"][pokoje[-2][0]+pokoje[-2][2]//2][pokoje[-2][1]+pokoje[-2][3]//2] = "_<."

    return(pokoje[0][0]+pokoje[0][2]//2, pokoje[0][1]+pokoje[0][3]//2)

def Connect(m, p_end, p_start):
    p_end[0], p_end[1] = p_end[0] + 2 * randint(0,p_end[2]//2), p_end[1] + 2 * randint(0,p_end[3]//2)
    p_start[0], p_start[1] = p_start[0] + 2 * randint(0,p_start[2]//2), p_start[1] + 2 * randint(0,p_start[3]//2)
    direction = randint(0, 1)
    goal = True
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
        
    