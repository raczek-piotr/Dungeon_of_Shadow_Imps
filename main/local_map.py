from random import randint, choice

from local_zero3 import zero3
from local_item_class import item_class_init

#def galwana(x, sx):
#    return((x+9) % sx-9)

def locate_a_room(m, pokoje, hm, minhm, max_room_size, min_room_size, space, are_all = True):
    proby = 0
    while len(pokoje) < minhm or proby < hm:
        sy, sx = randint(min_room_size, max_room_size)/2, randint(min_room_size, max_room_size)/2
        y, x = randint(1, m["sy"]-2 - 2 * sy), randint(1, m["sx"]-2 - 2 * sx)
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

def map_init(m, p, items, type_of_map = 0):
    pokoje = []
    m["sy"], m["sx"] = 32, 32
    m["r"] = [["#" for _ in range(m["sx"])] for _ in range(m["sy"])]
    m["v"] = [[" " for _ in range(m["sx"])] for _ in range(m["sy"])]
    m["o"] = [[" " for _ in range(m["sx"])] for _ in range(m["sy"])]
    special_map = False

    match type_of_map:
        case 0:
            min_room_size = 3
            max_room_size = 5
            hm = randint(15, 35) # how many?
            minhm = 8
            space = 3
            locate_a_room(m, pokoje, hm, minhm, max_room_size, min_room_size, space)
            for i in range(len(pokoje)):
                j = pokoje[i]
                for y in range(j[0]-1, j[0]+j[2]+1):
                    for x in range(j[1]-1, j[1]+j[3]+1):
                        m["r"][y][x] = "|"
                for y in range(j[0], j[0]+j[2]):
                    for x in range(j[1], j[1]+j[3]):
                        m["r"][y][x] = "_."
            pokojen = []
            for i in pokoje:
                pokojen.append(i)
            pokojeok = [pokojen.pop(1)]
            while pokojen != []:
                # if type_of_map != 0:
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
                middle2 = [(p1[0]+p2[0])//2, (p1[1]+p2[1])//2]
                if m["r"][middle2[0]][middle2[1]][0] != "#":
                    middle2[0] -= 1
                    middle2[1] -= 1
                #while m["r"][middle2[0]][middle2[1]][0] != "#":
                #    middle2[0] += randint(-1,1)
                #    middle2[1] += randint(-1,1)
                #    if ((middle2[0] > p1[0] and
                #         middle2[0] > p2[0]) or
                #        (middle2[0] < p1[0] and
                #         middle2[0] < p2[0])):
                #        middle2[0] = (p1[0]+p2[0])//2
                #    if ((middle2[1] > p1[1] and
                #         middle2[1] > p2[1]) or
                #        (middle2[1] < p1[1] and
                #         middle2[1] < p2[1])):
                #        middle2[1] = (p1[1]+p2[1])//2
                middle1 = [middle2[0], middle2[1]]
                ConnectNormal(m, p2, middle2)
                ConnectNormal(m, p1, middle1, True)
                pokojeok.append(pokojen.pop(n_minodl))
            for i in range(m["sy"]):
                for j in range(m["sx"]):
                    if m["r"][i][j] == "|":
                        m["r"][i][j] = "#"
            i = randint(1, len(pokoje)-2)
            for k in items:
                while m["r"][pokoje[i][0]+randint(0, pokoje[i][2]-1)][pokoje[i][1]+randint(0, pokoje[i][3]-1)] != "_.":
                    i = randint(1, len(pokoje)-2)
                m["r"][pokoje[i][0]+randint(0, pokoje[i][2]-1)][pokoje[i][1]+randint(0, pokoje[i][3]-1)] = "_"+k+"."
            if p["depth"] % 5 == 0:
                m["r"][pokoje[-1][0]+pokoje[-1][2]//2][pokoje[-1][1]+pokoje[-1][3]//2] = "_=>"
            else:
                m["r"][pokoje[-1][0]+pokoje[-1][2]//2][pokoje[-1][1]+pokoje[-1][3]//2] = "_>"

        case 1:
            m["r"] = [[choice(["#","#","#",":",":"]) for _ in range(m["sx"])] for _ in range(m["sy"])]
            for i in range(m["sx"]):
                m["r"][0][i] = "#"
                m["r"][-1][i] = "#"
            for i in range(m["sy"]):
                m["r"][i][0] = "#"
                m["r"][i][-1] = "#"
            locate_a_room(m, pokoje, 4, 2, 5, 3, 3, False)
            ran = len(pokoje)
            locate_a_room(m, pokoje, 16, 8, 3, 3, 1)
            l_pokoje = len(pokoje)
            for i in range(ran):
                j = pokoje[i]
                for y in range(j[0]-1, j[0]+j[2]+1):
                    for x in range(j[1]-1, j[1]+j[3]+1):
                        m["r"][y][x] = "|"
            flor = "_."
            for i in range(l_pokoje):
                j = pokoje[i]
                if i == ran:
                    flor = " "
                for y in range(j[0], j[0]+j[2]):
                    for x in range(j[1], j[1]+j[3]):
                        m["r"][y][x] = flor
            pokojen = []
            for i in pokoje:
                pokojen.append(i)
            pokojeok = [pokojen.pop(1)]
            while pokojen != []:
                # if type_of_map != 0:
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
                middle2 = [(p1[0]+p2[0])//2, (p1[1]+p2[1])//2]
                if m["r"][middle2[0]][middle2[1]][0] != "#":
                    middle2[0] -= 1
                    middle2[1] -= 1
                middle1 = [middle2[0], middle2[1]]
                ConnectCave(m, p2, middle2)
                ConnectCave(m, p1, middle1, True)
                pokojeok.append(pokojen.pop(n_minodl))
            for i in range(ran):
                j = pokoje[i]
                for y in range(j[0]-1, j[0]+j[2]+1):
                    for x in range(j[1]-1, j[1]+j[3]+1):
                        if m["r"][y][x] == "|":
                            m["r"][y][x] = "#"
            l_pokoje -= 1
            i = randint(ran, l_pokoje)
            for k in items:
                while m["r"][pokoje[i][0]+randint(0, pokoje[i][2]-1)][pokoje[i][1]+randint(0, pokoje[i][3]-1)] != " ":
                    i = randint(ran, l_pokoje)
                m["r"][pokoje[i][0]+randint(0, pokoje[i][2]-1)][pokoje[i][1]+randint(0, pokoje[i][3]-1)] = k+" "
            if p["depth"] % 5 == 0:
                m["r"][pokoje[1][0]+pokoje[1][2]//2][pokoje[1][1]+pokoje[1][3]//2] = "_=>"
            else:
                m["r"][pokoje[1][0]+pokoje[1][2]//2][pokoje[1][1]+pokoje[1][3]//2] = "_>"
        case _:
            min_room_size = 2
            max_room_size = 2
            # hm = randint(20, 30) # how many?
            # minhm = 10
            space = 0
            locate_a_room(m, pokoje, 4, 2, 3, 3, 3, False)
            locate_a_room(m, pokoje, 16, 8, 1, 1, 1)
            for i in range(len(pokoje)):
                j = pokoje[i]
                for y in range(j[0], j[0]+j[2]):
                    for x in range(j[1], j[1]+j[3]):
                        m["r"][y][x] = " "
            pokojen = []
            for i in pokoje:
                pokojen.append(i)
            pokojeok = [pokojen.pop(1)]
            while pokojen != []:
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
                        if odl > modl and odl < 20:
                            modl = odl
                            o_modl = id_o
                    if modl > minodl:
                        minodl = modl
                        n_minodl = id_n
                        o_minodl = o_modl
                p2 = pokojeok[o_minodl]
                p1 = pokojen[n_minodl]
                p2 = [p2[0]+p2[2]//2, p2[1]+p2[3]//2]
                p1 = [p1[0]+p1[2]//2, p1[1]+p1[3]//2]
                middle2 = [(p1[0]+p2[0])//2, (p1[1]+p2[1])//2]
                middle1 = [middle2[0], middle2[1]]
                ConnectCave(m, p2, middle2)
                ConnectCave(m, p1, middle1, True)
                pokojeok.append(pokojen.pop(n_minodl))
            i = randint(1, len(pokoje)-2)
            for k in items:
                while m["r"][pokoje[i][0]+randint(0, pokoje[i][2]-1)][pokoje[i][1]+randint(0, pokoje[i][3]-1)] != " ":
                    i = randint(1, len(pokoje)-2)
                m["r"][pokoje[i][0]+randint(0, pokoje[i][2]-1)][pokoje[i][1]+randint(0, pokoje[i][3]-1)] = k+" "
            if p["depth"] % 5 == 0:
                m["r"][pokoje[-1][0]+pokoje[-1][2]//2][pokoje[-1][1]+pokoje[-1][3]//2] = "=>"
            else:
                m["r"][pokoje[-1][0]+pokoje[-1][2]//2][pokoje[-1][1]+pokoje[-1][3]//2] = ">"

    return(pokoje[0][0]+pokoje[0][2]//2, pokoje[0][1]+pokoje[0][3]//2)
        #rmap[i[0]+randint(1-sy, sy-1)][i[1]+randint(1-sx, sx-1)] = item

def ConnectNormal(m, p_end, p_start, clear = False):
    direction = randint(0, 1)
    goal = True
    while goal:
        if direction == 0:
            if p_start[0] < p_end[0]:
                k = (p_start[0]+1) % m["sy"]
            elif p_start[0] > p_end[0]:
                k = (p_start[0]-1 )% m["sy"]
            else:
                k = p_start[0]
                direction += 1
            if m["r"][p_start[0]][p_start[1]] == "|" or m["r"][p_start[0]][p_start[1]] == " " or m["r"][p_start[0]+1][p_start[1]] == " " or m["r"][p_start[0]-1][p_start[1]] == " " or m["r"][p_start[0]][p_start[1]+1] == " " or m["r"][p_start[0]-1][p_start[1]] == " ":
                goal = False
            if m["r"][p_start[0]][p_start[1]] == "|":
                m["r"][p_start[0]][p_start[1]] = "+"
            elif m["r"][p_start[0]][p_start[1]] == "#":
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
            if m["r"][p_start[0]][p_start[1]] == "|" or m["r"][p_start[0]][p_start[1]] == " " or m["r"][p_start[0]+1][p_start[1]] == " " or m["r"][p_start[0]-1][p_start[1]] == " " or m["r"][p_start[0]][p_start[1]+1] == " " or m["r"][p_start[0]-1][p_start[1]] == " ":
                goal = False
            if m["r"][p_start[0]][p_start[1]] == "|":
                m["r"][p_start[0]][p_start[1]] = "+"
            elif m["r"][p_start[0]][p_start[1]] == "#":
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

def ConnectCave(m, p_end, p_start, clear = False):
    direction = randint(0, 1)
    goal = True
    while goal:
        if direction == 0:
            if p_start[0] < p_end[0]:
                k = (p_start[0]+1) % m["sy"]
            elif p_start[0] > p_end[0]:
                k = (p_start[0]-1 )% m["sy"]
            else:
                k = p_start[0]
                direction += 1
            #if m["r"][p_start[0]][p_start[1]] == "|":# or m["r"][p_start[0]][p_start[1]] == " " or m["r"][p_start[0]+1][p_start[1]] == " " or m["r"][p_start[0]-1][p_start[1]] == " " or m["r"][p_start[0]][p_start[1]+1] == " " or m["r"][p_start[0]-1][p_start[1]] == " ":
            #    goal = False
            if m["r"][p_start[0]][p_start[1]] == "|":
                m["r"][p_start[0]][p_start[1]] = "_."
            elif m["r"][p_start[0]][p_start[1]] in ["#"]:#,":"]:
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
            #if m["r"][p_start[0]][p_start[1]] == "|":# or m["r"][p_start[0]][p_start[1]] == " " or m["r"][p_start[0]+1][p_start[1]] == " " or m["r"][p_start[0]-1][p_start[1]] == " " or m["r"][p_start[0]][p_start[1]+1] == " " or m["r"][p_start[0]-1][p_start[1]] == " ":
            #    goal = False
            if m["r"][p_start[0]][p_start[1]] == "|":
                m["r"][p_start[0]][p_start[1]] = "_."
            elif m["r"][p_start[0]][p_start[1]] in ["#"]:#,":"]:
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

def open_doors(rmap, vmap):
    for y in range(len(rmap)):
        for x in range(len(rmap[0])):
            if rmap[y][x][0] == "=":
                rmap[y][x] = rmap[y][x][1:]
                if vmap[y][x][0] == "=":
                    vmap[y][x] = rmap[y][x]
            else:
                if len(rmap[y][x]) > 1 and rmap[y][x][1] == "=":
                    rmap[y][x] = rmap[y][x][0] + rmap[y][x][2:]
