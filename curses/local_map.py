from random import randint, choice
from time import time, ctime

from local_scripts import zero3
from local_enemies_class import enemies_class_add


def map_init_str(m, p, items, type_of):
    with open("maps/"+type_of+".cfg", "r") as rm: # readmap -PR-
        p["echo"] = "?!"
        rm = rm.read().split("\n")
        while rm[-1] == "":
            rm.pop(-1)
        ty, tx = rm.pop(0).split(" ")
        m["sy"], m["sx"] = int(ty), int(tx)
        ty, tx = rm.pop(0).split(" ")
        if type_of[:3] == "sur":
            m["r"] = [["^" for _ in range(m["sx"])] for _ in range(m["sy"])]
        else:
            m["r"] = [["#" for _ in range(m["sx"])] for _ in range(m["sy"])]
        m["v"] = [[" " for _ in range(m["sx"])] for _ in range(m["sy"])]
        l = 0
        for y in range(m["sy"]-2):
            t = rm[y].split(";")
            for x in range(m["sx"]-2):
                m["r"][y+1][x+1] = t[x]
    return(int(ty), int(tx))



def locate_a_room(m, pokoje, hm, minhm, max_room_size, min_room_size, space, are_all = True):
    proby = 0 #tries done -PR-
    while len(pokoje) < minhm or proby < hm:
        sy, sx = randint(min_room_size, max_room_size)/2, randint(min_room_size, max_room_size)/2
        y, x = randint(1, m["sy"]-3 -2*sy), randint(1, m["sx"]-3 -2*sx) # one was out of the map -2→-3 -PR-
        can, proby = True, proby + 1
        for i in pokoje:
            if ((abs((i[0]+i[2])-(y+sy)) < i[2]+sy+space and
                 abs((i[1]+i[3])-(x+sx)) < i[3]+sx+space)):
            # if ((abs((i[0]+i[2])-(y+sy))<i[2]+sy+1 and
            #      abs((i[1]+i[3])-(x+sx))<i[3]+sx+1) or
            #     (abs((i[0]+i[2])-(y+sy))==i[2]+sy+2 and
            #      abs((i[1]+i[3])-(x+sx))<i[3]+sx+2) or
            #     (abs((i[0]+i[2])-(y+sy))<i[2]+sy+2 and
            #      abs((i[1]+i[3])-(x+sx))==i[3]+sx+2)):
                can = False
        if can:
            pokoje.append([y, x, sy, sx])
            continue
    if are_all:
        for i in range(len(pokoje)):
            pokoje[i][2] = int(2*pokoje[i][2])
            pokoje[i][3] = int(2*pokoje[i][3])


def map_init(m, p, items, type_of = 0, stairs = 3):
    with open("log.txt", "a") as txt:
        txt.write(ctime(time()) + " creating map with properties: " + str(type_of)+" "+str(type(type_of))+"\n")
    if type(type_of) == int:
        return map_init_int(m, p, items, type_of, stairs)
    else:
        return map_init_str(m, p, items, type_of)


def map_init_int(m, p, items, type_of, stairs):
    pokoje = []
    m["sy"], m["sx"] = 31, 31
    sizey, sizex = m["sy"]//2, m["sx"]//2
    m["r"] = [["#" for _ in range(m["sx"])] for _ in range(m["sy"])]
    m["v"] = [[" " for _ in range(m["sx"])] for _ in range(m["sy"])]
    match type_of:
        case 1:
            pokoje, hm = [], 0
            while hm < 16:
                sy, sx = randint(2,3), randint(2,4)
                y, x = randint(1, m["sy"] - sy -1), randint(1, m["sx"] - sx -1)
                can = True
                for i in pokoje:
                    if ((abs((i[0]+i[2])-(y+sy)) < i[2]+sy and
                         abs((i[1]+i[3])-(x+sx)) < i[3]+sx)):
                        can = False
                if can:
                    pokoje.append([y, x, sy, sx])
                    hm += 1
                    continue

            for i in range(len(pokoje)):
                j = pokoje[i]
                for y in range(j[0], j[0]+j[2]):
                    for x in range(j[1], j[1]+j[3]):
                        m["r"][y][x] = " "
            for pos in pokoje[:-1]:
                pos = [pos[0]+pos[2]//2, pos[1]+pos[3]//2]
                Connect(m, pos, [m["sx"]//2, m["sy"]//2])
            pos = pokoje[-1]
            pos = [pos[0]+pos[2]//2, pos[1]+pos[3]//2]
            Connect(m, pos, [m["sx"]//2, m["sy"]//2], True)
            if stairs > 1:
                m["r"][pokoje[-1][0]+pokoje[-1][2]//2][pokoje[-1][1]+pokoje[-1][3]//2] = "> "
                m["r"][pokoje[-3][0]+pokoje[-3][2]//2][pokoje[-3][1]+pokoje[-3][3]//2] = "> "
            if stairs % 2 == 1:
                m["r"][pokoje[-2][0]+pokoje[-2][2]//2][pokoje[-2][1]+pokoje[-2][3]//2] = "< "
                m["r"][pokoje[-4][0]+pokoje[-4][2]//2][pokoje[-4][1]+pokoje[-4][3]//2] = "< "
            RandomTileConnect(m, "= ")
            RandomTileConnect(m, "= ")

        case 2:
            minhm = 7 # should be space on the map… -PR-
            pokoje = []
            while len(pokoje) < minhm:
                sy, sx = 1+2*randint(1,2), 1+2*randint(1,2)
                y, x = 1+2*randint(0, sizey - sy), 1+2*randint(0, sizex - sx)
                can = True
                for i in pokoje:
                    if ((abs((i[0]+i[2])-(y+sy)) < i[2]+sy and
                         abs((i[1]+i[3])-(x+sx)) < i[3]+sx)):
                        can = False
                if can:
                    pokoje.append([y, x, sy, sx]) # one room in enother -PR-
                    continue

            hm = len(pokoje)
            for it in range(hm):
                for y in range(pokoje[it][0]-1, pokoje[it][0] + pokoje[it][2] +1):
                    for x in range(pokoje[it][1]-1, pokoje[it][1] + pokoje[it][3] +1):
                        m["r"][y][x] = "|"
            for it in range(hm):
                RegularConnect(m, pokoje[it-1].copy(), pokoje[it].copy())

            type_of_rooms = ["% ","% ","% ","% ","=" ".", ".","."] # one more -PR-
            for it in range(hm):
                i = type_of_rooms.pop()
                for y in range(pokoje[it][0], pokoje[it][0] + pokoje[it][2]):
                    for x in range(pokoje[it][1], pokoje[it][1] + pokoje[it][3]):
                        m["r"][y][x] = i
            for it in range(hm):
                for y in range(pokoje[it][0]-1, pokoje[it][0] + pokoje[it][2] +1):
                    for x in range(pokoje[it][1]-1, pokoje[it][1] + pokoje[it][3] +1):
                        if m["r"][y][x] == "|":
                            m["r"][y][x] = "#"
            if stairs > 1:
                m["r"][pokoje[-2][0]+pokoje[-2][2]//2][pokoje[-2][1]+pokoje[-2][3]//2] = "> "
            if stairs % 2 == 1:
                m["r"][pokoje[-3][0]+pokoje[-3][2]//2][pokoje[-3][1]+pokoje[-3][3]//2] = "< "
            pokoje[0], pokoje[-1] = pokoje[-1], pokoje[0] # for good place player to start -PR-

        case 3:
            m["r"] = [[choice(["#","#",": "]) for _ in range(m["sx"])] for _ in range(m["sy"])]
            for i in range(m["sx"]):
                m["r"][0][i] = "#"
                m["r"][-1][i] = "#"
            for i in range(m["sy"]):
                m["r"][i][0] = "#"
                m["r"][i][-1] = "#"
            locate_a_room(m, pokoje, 3, 3, 5, 3, 1, False)
            ran = 3 # len(pokoje) # always 3 -PR-
            locate_a_room(m, pokoje, 20, 8, 3, 3, 1)
            l_pokoje = len(pokoje)
            for i in range(ran):
                j = pokoje[i]
                for y in range(j[0]-1, j[0]+j[2]+1):
                    for x in range(j[1]-1, j[1]+j[3]+1):
                        m["r"][y][x] = "|"
            flor = "."
            for i in range(l_pokoje):
                j = pokoje[i]
                if i == ran: # rest of rooms have no light -PR-
                    flor = " "
                for y in range(j[0], j[0]+j[2]):
                    for x in range(j[1], j[1]+j[3]):
                        m["r"][y][x] = flor
            pokojen = pokoje.copy()
            pokojeok = [pokojen.pop(0)]
            while pokojen != []:
                # if type_of != 0:
                n_minodl = 0
                o_minodl = 0
                minodl = m["sy"]**2 + m["sx"]**2
                for id_n in range(len(pokojen)):
                    n = pokojen[id_n]
                    modl = m["sy"]**2 + m["sx"]**2
                    o_modl = -1
                    for id_o in range(len(pokojeok)):
                        o = pokojeok[id_o]
                        odl = (n[0]-n[2]/2-o[0]+o[2]/2)**2 + (n[1]-n[3]/2-o[1]+o[3]/2)**2
                        if odl < modl:
                            modl = odl
                            o_modl = id_o
                    if modl < minodl:
                        minodl = modl
                        n_minodl = id_n
                        o_minodl = o_modl
                p2 = pokojeok[o_minodl]
                p1 = pokojen[n_minodl]
                p2 = [p2[0]+p2[2]//2, p2[1]+p2[3]//2]
                p1 = [p1[0]+p1[2]//2, p1[1]+p1[3]//2]
                middle = [(p1[0]+p2[0])//2, (p1[1]+p2[1])//2]
                if m["r"][middle[0]][middle[1]][0] != "#":
                    middle[0] -= 1
                    middle[1] -= 1
                Connect(m, p2, middle.copy())
                Connect(m, p1, middle.copy(), True)
                pokojeok.append(pokojen.pop(n_minodl))
            for i in range(ran):
                j = pokoje[i]
                for y in range(j[0]-1, j[0]+j[2]+1):
                    for x in range(j[1]-1, j[1]+j[3]+1):
                        if m["r"][y][x] == "|":
                            m["r"][y][x] = "#"
                        elif m["r"][y][x] == "+ ":
                            m["r"][y][x] = ": "
                        else:
                            if randint(0, 7) == 0:
                                m["r"][y][x] = ":."
            if stairs > 1:
                m["r"][pokoje[-1][0]+pokoje[-1][2]//2][pokoje[-1][1]+pokoje[-1][3]//2] = "> "
                m["r"][pokoje[-3][0]+pokoje[-3][2]//2][pokoje[-3][1]+pokoje[-3][3]//2] = "> "
            if stairs % 2 == 1:
                m["r"][pokoje[-2][0]+pokoje[-2][2]//2][pokoje[-2][1]+pokoje[-2][3]//2] = "< "
                m["r"][pokoje[-4][0]+pokoje[-4][2]//2][pokoje[-4][1]+pokoje[-4][3]//2] = "< "
        case 8:
            hm = 7
            pokoje == []
            while len(pokoje) < hm:
                sy, sx = 1+2*randint(1,2), 1+2*randint(1,3)
                y, x = 1+2*randint(0, sizey - sy), 1+2*randint(0, sizex - sx)
                can = True
                for i in pokoje:
                    if ((abs((i[0]+i[2])-(y+sy)) < i[2]+sy and
                         abs((i[1]+i[3])-(x+sx)) < i[3]+sx)):
                        can = False
                if can:
                    pokoje.append([y, x, sy, sx])
                    continue

            hm = 3
            Spokoje = []
            while len(Spokoje) < hm:
                sy, sx = randint(2,3), randint(2,3)
                y, x = 1+2*randint(0, sizey - sy), 1+2*randint(0, sizex - sx)
                can = True
                for i in pokoje:
                    if ((abs((i[0]+i[2])-(y+sy)) < i[2]+sy and
                         abs((i[1]+i[3])-(x+sx)) < i[3]+sx)):
                        can = False
                if can:
                    Spokoje.append([y, x, sy, sx]) # one room in enother -PR-
                    continue
            hm = len(Spokoje)
            for it in range(hm):
                for y in range(Spokoje[it][0], Spokoje[it][0] + Spokoje[it][2]):
                    for x in range(Spokoje[it][1], Spokoje[it][1] + Spokoje[it][3]):
                        m["r"][y][x] = " "
            for it in range(hm):
                RegularConnect(m, Spokoje[it-1].copy(), Spokoje[it].copy())

            hm = len(pokoje)
            for it in range(hm):
                for y in range(pokoje[it][0]-1, pokoje[it][0] + pokoje[it][2] +1):
                    for x in range(pokoje[it][1]-1, pokoje[it][1] + pokoje[it][3] +1):
                        m["r"][y][x] = "|"
            for it in range(hm):
                RegularConnect(m, pokoje[it-1].copy(), pokoje[it].copy())
            RegularConnect(m, Spokoje[hm-it].copy(), pokoje[it].copy()) # connect the two "worlds" -PR-
            for it in range(hm):
                for y in range(pokoje[it][0], pokoje[it][0] + pokoje[it][2]):
                    for x in range(pokoje[it][1], pokoje[it][1] + pokoje[it][3]):
                        m["r"][y][x] = "."
            for it in range(hm):
                for y in range(pokoje[it][0]-1, pokoje[it][0] + pokoje[it][2] +1):
                    for x in range(pokoje[it][1]-1, pokoje[it][1] + pokoje[it][3] +1):
                        if m["r"][y][x] == "|":
                            m["r"][y][x] = "#"
            if stairs > 1:
                m["r"][pokoje[-2][0]+pokoje[-2][2]//2][pokoje[-2][1]+pokoje[-2][3]//2] = ">."
            if stairs % 2 == 1:
                m["r"][pokoje[-3][0]+pokoje[-3][2]//2][pokoje[-3][1]+pokoje[-3][3]//2] = "<."
            pokoje[0], pokoje[-1] = pokoje[-1], pokoje[0] # for good place player to start -PR-
            pokoje.extend(Spokoje)

        case _: # 0 -PR-
            hm = 9 # 5 -PR-
            pokoje = []
            sizey, sizex = 17, 26
            m["sy"], m["sx"] = 2*sizey+1, 2*sizex+1
            m["r"] = [["#" for _ in range(m["sx"])] for _ in range(m["sy"])]
            m["v"] = [[" " for _ in range(m["sx"])] for _ in range(m["sy"])]
            while len(pokoje) < hm:
                sy, sx = 1+2*randint(1,2), 1+2*randint(1,3)
                y, x = 1+2*randint(0, sizey - sy), 1+2*randint(0, sizex - sx) if hm != 0 else 1 #on left boarder
                can = True
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
                RegularConnect(m, pokoje[it-1].copy(), pokoje[it].copy())
            for it in range(hm):
                for y in range(pokoje[it][0], pokoje[it][0] + pokoje[it][2]):
                    for x in range(pokoje[it][1], pokoje[it][1] + pokoje[it][3]):
                        m["r"][y][x] = "."
            for it in range(hm):
                for y in range(pokoje[it][0]-1, pokoje[it][0] + pokoje[it][2] +1):
                    for x in range(pokoje[it][1]-1, pokoje[it][1] + pokoje[it][3] +1):
                        if m["r"][y][x] == "|":
                            m["r"][y][x] = "#"
            if stairs > 1:
                m["r"][pokoje[-2][0]+pokoje[-2][2]//2][pokoje[-2][1]+pokoje[-2][3]//2] = ">."
            if stairs % 2 == 1:
                m["r"][pokoje[-3][0]+pokoje[-3][2]//2][pokoje[-3][1]+pokoje[-3][3]//2] = "<."

    more = True # here are added enemies on "battle field" :) -PR-
    l_pokoje = len(pokoje)-1
    while more:
        i = randint(1, l_pokoje) # (1→ran) player with nonething else in start_room -PR-
        j = [pokoje[i][0]+randint(0, pokoje[i][2]-1), pokoje[i][1]+randint(0, pokoje[i][3]-1)]
        while m["r"][j[0]][j[1]] not in {" ",".","= ","% "}:
            i = randint(1, l_pokoje)
            j = [pokoje[i][0]+randint(0, pokoje[i][2]-1), pokoje[i][1]+randint(0, pokoje[i][3]-1)]
        e_id, more = enemies_class_add(j[1], j[0], type_of, p["depth"])
        m["r"][j[0]][j[1]] = e_id+m["r"][j[0]][j[1]]
    i = randint(1, l_pokoje) # (1→ran) less items in rooms with lihgt
    j = [pokoje[i][0]+randint(0, pokoje[i][2]-1), pokoje[i][1]+randint(0, pokoje[i][3]-1)]
    for k in items:
        while m["r"][j[0]][j[1]] not in {" ",".","= ","% "}:
            i = randint(1, l_pokoje)
            j = [pokoje[i][0]+randint(0, pokoje[i][2]-1), pokoje[i][1]+randint(0, pokoje[i][3]-1)]
        m["r"][j[0]][j[1]] = k+m["r"][j[0]][j[1]]
    return(pokoje[0][0]+pokoje[0][2]//2, pokoje[0][1]+pokoje[0][3]//2)

def RegularConnect(m, p_end, p_start):
    p_end[0], p_end[1] = p_end[0] + 2 * randint(0,p_end[2]//2), p_end[1] + 2 * randint(0,p_end[3]//2)
    p_start[0], p_start[1] = p_start[0] + 2 * randint(0,p_start[2]//2), p_start[1] + 2 * randint(0,p_start[3]//2)
    direction = randint(0, 1)
    goal = True # have the goal -PR-
    while goal:
        if direction == 0:
            if p_start[0] < p_end[0]:
                k = p_start[0]+1
            elif p_start[0] > p_end[0]:
                k = p_start[0]-1
            else:
                k = p_start[0]
                direction += 1
            if m["r"][k][p_start[1]] == "|" or m["r"][k][p_start[1]] == "+ ":
                m["r"][k][p_start[1]] = "+ "
            elif m["r"][k][p_start[0]] not in {".","= ","%"}:
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
            if m["r"][p_start[0]][k] == "|" or m["r"][p_start[0]][k] == "+ ":
                m["r"][p_start[0]][k] = "+ "
            elif m["r"][p_start[0]][k] not in {".","= ","%"}:
                m["r"][p_start[0]][k] = " "
            p_start[1] = 2*k-p_start[1]
            m["r"][p_start[0]][p_start[1]] = " "
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
    change = {" ","#","^","+","% ","."}
    goal = True # I have the goal -PR-
    while goal:
        if direction == 0:
            if p_start[0] < p_end[0]:
                k = p_start[0]+1
            elif p_start[0] > p_end[0]:
                k = p_start[0]-1
            else:
                k = p_start[0]
                direction += 1
            if m["r"][k][p_start[1]][0] in change:
                m["r"][k][p_start[1]] = tile
            elif len(m["r"][k][p_start[1]]) >= 4: #@000 + something? -PR-
                m["r"][k][p_start[1]] = m["r"][k][p_start[1]][:4]+tile
            elif m["r"][k][p_start[1]] == "$":
                m["r"][k][p_start[1]] = "$"+tile
            p_start[0] = k#2*k-p_start[0]
            #if m["r"][p_start[0]][p_start[1]] in {"#"," ","+",": ",":."}:
            #    m["r"][p_start[0]][p_start[1]] = "="
        else:
            if p_start[1] < p_end[1]:
                k = p_start[1]+1
            elif p_start[1] > p_end[1]:
                k = p_start[1]-1
            else:
                k = p_start[1]
                direction -= 1
            if m["r"][p_start[0]][k][0] in change:
                m["r"][p_start[0]][k] = tile
            elif len(m["r"][k][p_start[1]]) >= 4: #@000 + something? -PR-
                m["r"][p_start[0]][k] = m["r"][p_start[0]][k][:4]+tile
            elif m["r"][p_start[0]][k] == "$":
                m["r"][p_start[0]][k] = "$"+tile
            p_start[1] = k#2*k-p_start[1]
            #if m["r"][p_start[0]][p_start[1]] in {"#"," ","+",": ",":."}:
            #    m["r"][p_start[0]][p_start[1]] = "="
        if p_start[0] == p_end[0] and p_start[1] == p_end[1]:
            goal = False
        if randint(0, 99) < 20:
            direction = (direction+1) % 2

def Connect(m, p_end, p_start, clear = False):
    m["r"][p_start[0]][p_start[1]] = "d"
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
            if m["r"][p_start[0]][p_start[1]] == "|":
                m["r"][p_start[0]][p_start[1]] = "+ "
            elif m["r"][p_start[0]][p_start[1]] in {"#","  ","&"}:
                m["r"][p_start[0]][p_start[1]] = "d"
            p_start[0] = k
        else:
            if p_start[1] < p_end[1]:
                k = (p_start[1]+1) % m["sx"]
            elif p_start[1] > p_end[1]:
                k = (p_start[1]-1) % m["sx"]
            else:
                k = p_start[1]
                direction -= 1
            if m["r"][p_start[0]][p_start[1]] == "|":
                m["r"][p_start[0]][p_start[1]] = "+ "
            elif m["r"][p_start[0]][p_start[1]] in {"#","  ","&"}:
                m["r"][p_start[0]][p_start[1]] = "d"
            p_start[1] = k
        if p_start[0] == p_end[0] and p_start[1] == p_end[1]:
            goal = False
        if randint(0, 99) < 20:
            direction = (direction+1) % 2
    if clear:
        for i in range(m["sy"]):
            for j in range(m["sx"]):
                if m["r"][i][j] == "d":
                    m["r"][i][j] = " "
