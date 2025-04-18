from random import randint, choice
from time import time, ctime

from local_scripts import zero3
from local_iostream import write2log
from local_enemies_class import enemies_class_add




def locate_a_room(m, pokoje, hm, max_room_size, min_room_size, space):
    # do hm rooms -PR-
    while len(pokoje) < hm:
        sy, sx = randint(min_room_size, max_room_size)/2, randint(min_room_size, max_room_size)/2
        y, x = randint(1, m["sy"]-3 -2*sy), randint(1, m["sx"]-3 -2*sx)
        can = True
        for i in pokoje:
            if ((abs((i[0]+i[2])-(y+sy)) <= i[2]+sy+space and
                 abs((i[1]+i[3])-(x+sx)) <= i[3]+sx+space)):
                can = False
        if can:
            pokoje.append([y, x, sy, sx])

    # change format -PR-
    for i in range(len(pokoje)):
        pokoje[i][2] = int(2*pokoje[i][2])
        pokoje[i][3] = int(2*pokoje[i][3])


def deep_map(m, p, items, type_of, stairs):

    pokoje = []
    m["sy"], m["sx"] = 50, 50
    sizey, sizex = m["sy"]//2, m["sx"]//2
    m["r"] = [["#" for _ in range(m["sx"])] for _ in range(m["sy"])]
    m["v"] = [[" " for _ in range(m["sx"])] for _ in range(m["sy"])]
               

    hm = 13
    locate_a_room(m, pokoje, hm, 9, 3, 0)

    for x in range(m["sx"]): # divine halo -PR-
        rx = x**2 + (m["sx"]-x-1)**2 # for optymalization, remember the value -PR-
        for y in range(m["sy"]):
            r = rx + y**2 + (m["sy"]-y-1)**2
            if r < 2510:
                m["r"][y][x] = "  "

    # make lava river and divine -PR-
    for _ in range(3):
        RandomTileConnect(m, "& ")
    for it in range(hm): # mark "door" options -PR-
        for y in range(pokoje[it][0]-1, pokoje[it][0] + pokoje[it][2]+1):
            for x in range(pokoje[it][1]-1, pokoje[it][1] + pokoje[it][3]+1):
                if m["r"][y][x] == "#":
                    m["r"][y][x] = "|"
    for it in range(hm): # then make rooms -PR-
        for y in range(pokoje[it][0], pokoje[it][0] + pokoje[it][2]):
            for x in range(pokoje[it][1], pokoje[it][1] + pokoje[it][3]):
                if m["r"][y][x] in {"& ", "  "}:
                    m["r"][y][x] = "\""
                else:
                    m["r"][y][x] = "."
    for it in range(hm): # and then connect the rooms -PR-
        Connect(m, pokoje[it-1].copy(), pokoje[it].copy())
    for it in range(hm): # after connected, make doors -PR-
        for y in range(pokoje[it][0]-1, pokoje[it][0] + pokoje[it][2]+1):
            for x in range(pokoje[it][1]-1, pokoje[it][1] + pokoje[it][3]+1):
                if m["r"][y][x] == "|":
                    m["r"][y][x] = "#"

    for x in range(m["sx"]): # hill with lava halo -PR-
        rx = x**2 + (m["sx"]-x-1)**2 # for optymalization, remember the value -PR-
        for y in range(m["sy"]):
            r = rx + y**2 + (m["sy"]-y-1)**2
            if r < 2410:
                m["r"][y][x] = "&"
            elif r < 2440:
                m["r"][y][x] = "^ "

    if stairs > 1:
        m["r"][pokoje[-2][0]+pokoje[-2][2]//2][pokoje[-2][1]+pokoje[-2][3]//2] = ">"
    if stairs % 2 == 1:
        m["r"][pokoje[-3][0]+pokoje[-3][2]//2][pokoje[-3][1]+pokoje[-3][3]//2] = "<"



    pokoje[0], pokoje[-1] = pokoje[-1], pokoje[0] # for good place player to start -PR-




    more = True # here are added enemies on "battle field" :) -PR-
    l_pokoje = len(pokoje)-1
    for k in items:
        i = randint(1, l_pokoje) # (1→ran) player with nonething else in start_room -PR-
        j = [pokoje[i][0]+randint(0, pokoje[i][2]-1), pokoje[i][1]+randint(0, pokoje[i][3]-1)]
        while m["r"][j[0]][j[1]] not in {" ",".","=","%"}:
            i = randint(1, l_pokoje)
            j = [pokoje[i][0]+randint(0, pokoje[i][2]-1), pokoje[i][1]+randint(0, pokoje[i][3]-1)]
        m["r"][j[0]][j[1]] = k+m["r"][j[0]][j[1]]
    while more:
        i = randint(1, l_pokoje) # (1→ran) player with nonething else in start_room -PR-
        j = [pokoje[i][0]+randint(0, pokoje[i][2]-1), pokoje[i][1]+randint(0, pokoje[i][3]-1)]
        while m["r"][j[0]][j[1]] not in {" ",".","=","%","*","~","]","}",")","?","!"}:
            i = randint(1, l_pokoje)
            j = [pokoje[i][0]+randint(0, pokoje[i][2]-1), pokoje[i][1]+randint(0, pokoje[i][3]-1)]
        e_id, more = enemies_class_add(j[1], j[0], type_of, p["depth"])
        m["r"][j[0]][j[1]] = e_id+m["r"][j[0]][j[1]]
    i = randint(1, l_pokoje)
    j = [pokoje[i][0]+randint(0, pokoje[i][2]-1), pokoje[i][1]+randint(0, pokoje[i][3]-1)]

    return(pokoje[0][0]+pokoje[0][2]//2, pokoje[0][1]+pokoje[0][3]//2)






def Connect(m, p_end, p_start):
    if m["r"][p_start[0]][p_start[1]] == "#":
        m["r"][p_start[0]][p_start[1]] = " "
    elif m["r"][p_start[0]][p_start[1]] == "|":
        m["r"][p_start[0]][p_start[1]] = "."
    elif m["r"][p_start[0]][p_start[1]] in {"& ", "  "}:
        m["r"][p_start[0]][p_start[1]] = "\" "

    direction = randint(0, 1)
    goal = True # Do we have a goal? Or it is "done"?
    while goal:
        if direction == 0:
            if p_start[0] < p_end[0]:
                k = (p_start[0]+1) % m["sy"]
            elif p_start[0] > p_end[0]:
                k = (p_start[0]-1)% m["sy"]
            else:
                k = p_start[0]
                direction += 1
            if m["r"][p_start[0]][p_start[1]] == "#":
                m["r"][p_start[0]][p_start[1]] = " "
            elif m["r"][p_start[0]][p_start[1]] == "|":
                m["r"][p_start[0]][p_start[1]] = "."
            elif m["r"][p_start[0]][p_start[1]] in {"& ", "  "}:
                m["r"][p_start[0]][p_start[1]] = "\" "
            p_start[0] = k
        else:
            if p_start[1] < p_end[1]:
                k = (p_start[1]+1) % m["sx"]
            elif p_start[1] > p_end[1]:
                k = (p_start[1]-1) % m["sx"]
            else:
                k = p_start[1]
                direction -= 1
            if m["r"][p_start[0]][p_start[1]] == "#":
                m["r"][p_start[0]][p_start[1]] = " "
            elif m["r"][p_start[0]][p_start[1]] == "|":
                m["r"][p_start[0]][p_start[1]] = "."
            elif m["r"][p_start[0]][p_start[1]] in {"& ", "  "}:
                m["r"][p_start[0]][p_start[1]] = "\" "
            p_start[1] = k
        if p_start[0] == p_end[0] and p_start[1] == p_end[1]:
            goal = False
        if randint(0, 99) < 20:
            direction = (direction+1) % 2


def RandomTileConnect(m, tile):
    p_end = [m["sy"], m["sx"]]
    p_start = [m["sy"], m["sx"]]
    direction = randint(0, 1)
    p_end[direction], p_start[direction] = randint(1, p_end[direction]-2), randint(1, p_start[direction]-2)
    direction = (direction+1)%2
    p_end[direction], p_start[direction] = p_end[direction]-2, 1
    if randint(0,1):
        p_start, p_end = p_end, p_start
    m["r"][p_start[0]][p_start[1]] = tile
    goal = True # We have the goal -PR-
    while goal:
        if direction == 0:
            if p_start[0] < p_end[0]:
                k = p_start[0]+1
            elif p_start[0] > p_end[0]:
                k = p_start[0]-1
            else:
                k = p_start[0]
                direction += 1
            m["r"][k][p_start[1]] = tile
            p_start[0] = k
        else:
            if p_start[1] < p_end[1]:
                k = p_start[1]+1
            elif p_start[1] > p_end[1]:
                k = p_start[1]-1
            else:
                k = p_start[1]
                direction -= 1
            m["r"][p_start[0]][k] = tile
            p_start[1] = k
        if p_start[0] == p_end[0] and p_start[1] == p_end[1]:
            goal = False
        if randint(0, 99) < 20:
            direction = (direction+1) % 2