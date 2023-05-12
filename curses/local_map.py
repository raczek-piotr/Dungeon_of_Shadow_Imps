from random import randint, choice

from local_scripts import zero3
from local_item_class import item_class_init
from local_enemies_class import enemies_class_init
from local_regular_map import regular_map_init


def map_init_str(m, p, items, enemies, type_of_map):
    with open("maps/"+type_of_map+".map", "r") as rm: # readmap -PR-
        p["echo"] = "?!"
        rm = rm.read().split("\n")
        while rm[-1] == "":
            rm.pop(-1)
        ty, tx = rm.pop(0).split(" ")
        m["sy"], m["sx"] = int(ty), int(tx)
        ty, tx = rm.pop(0).split(" ")
        if type_of_map[:3] == "sur":
            m["r"] = [["^" for _ in range(m["sx"])] for _ in range(m["sy"])]
        else:
            m["r"] = [["#" for _ in range(m["sx"])] for _ in range(m["sy"])]
        m["v"] = [[" " for _ in range(m["sx"])] for _ in range(m["sy"])]
        m["o"] = [[" " for _ in range(m["sx"])] for _ in range(m["sy"])]
        l = 0
        for y in range(m["sy"]-2):
            t = rm[y].split(";")
            for x in range(m["sx"]-2):
                m["r"][y+1][x+1] = t[x]
                if m["r"][y+1][x+1] == "_":
                    m["r"][y+1][x+1] += "."
                elif m["r"][y+1][x+1][0] == "_":
                    if m["r"][y+1][x+1][1] == "i":
                        l -= 1
                        it = rm[l].split(" ")
                        e, it = it[0], item_class_init(it[0], randint(int(it[1]), int(it[2])))
                        m["r"][y+1][x+1] = t[x][0]+e+zero3(it)+t[x][2:]
                    elif m["r"][y+1][x+1][1] == "w":
                        l -= 1
                        it = rm[l].split("|")
                        e = it[-1].split(";")
                        for i in range(len(e)):
                            if e[i][0] == '"':
                                e[i] = e[i][1:]
                            else:
                                e[i] = int(e[i])
                        e, it = it[0], item_class_init(it[0], {"item": it[1], "type": ("" if it[2] == ";" else it[2]), "values": e, "ident": (True if it[3] == "t" else False), "grouping": (True if it[4] == "t" else False)})
                        m["r"][y+1][x+1] = t[x][0]+e+zero3(it)+t[x][2:]
                elif m["r"][y+1][x+1][0] == "e":
                    l -= 1
                    e = rm[l].split(" ")
                    it = enemies_class_init(e[0], y+1, x+1, int(e[1]), int(e[2]),int(e[3]), int(e[4]), int(e[5]), (True if e[6] == "t" else False), [])
                    m["r"][y+1][x+1] = e[0]+zero3(it)+t[x][1:]
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


def map_init(m, p, items, enemies, type_of_map = 0, stairs = 3):
    if type(type_of_map) == type(0):
        return map_init_int(m, p, items, enemies, type_of_map, stairs)
    else:
        return map_init_str(m, p, items, enemies, type_of_map)


def map_init_int(m, p, items, enemies, type_of_map, stairs):
    print(type_of_map)
    pokoje = []
    m["sy"], m["sx"] = 32, 32
    m["r"] = [["#" for _ in range(m["sx"])] for _ in range(m["sy"])]
    m["v"] = [[" " for _ in range(m["sx"])] for _ in range(m["sy"])]
    m["o"] = [[" " for _ in range(m["sx"])] for _ in range(m["sy"])]

    match type_of_map:
        case 1:
            m["r"] = [["#" for _ in range(m["sx"])] for _ in range(m["sy"])]
            locate_a_room(m, pokoje, 3, 3, 5, 3, 1, False)
            ran = len(pokoje) #first rooms with no light
            locate_a_room(m, pokoje, 20, 5, 3, 3, 1)
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
            pokojen = [] #no -PR-
            for i in pokoje:
                pokojen.append(i)
            pokojeok = [pokojen.pop(1)] #ok -PR-
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
                Connect(m, p2, middle2)
                Connect(m, p1, middle1, True)
                pokojeok.append(pokojen.pop(n_minodl))
            for i in range(ran):
                j = pokoje[i]
                for y in range(j[0]-1, j[0]+j[2]+1):
                    for x in range(j[1]-1, j[1]+j[3]+1):
                        if m["r"][y][x] == "|":
                            m["r"][y][x] = "#"
            l_pokoje = l_pokoje-1
            i = randint(1, l_pokoje) # (1→ran) less items in rooms with lihgt
            j = [pokoje[i][0]+randint(0, pokoje[i][2]-1), pokoje[i][1]+randint(0, pokoje[i][3]-1)]
            for k in items:
                while m["r"][j[0]][j[1]] != " ":
                    i = randint(1, l_pokoje)
                    j = [pokoje[i][0]+randint(0, pokoje[i][2]-1), pokoje[i][1]+randint(0, pokoje[i][3]-1)]
                m["r"][j[0]][j[1]] = k+" "
            if stairs > 1:
                m["r"][pokoje[-1][0]+pokoje[-1][2]//2][pokoje[-1][1]+pokoje[-1][3]//2] = "> "
            if stairs % 2 == 1:
                m["r"][pokoje[-2][0]+pokoje[-2][2]//2][pokoje[-2][1]+pokoje[-2][3]//2] = "< "
            for k in enemies:
                i = randint(1, l_pokoje) # (1→ran) less monsters in rooms with lihgt
                j = [pokoje[i][0]+randint(0, pokoje[i][2]-1), pokoje[i][1]+randint(0, pokoje[i][3]-1)]
                while m["r"][j[0]][j[1]] != "_." and m["r"][j[0]][j[1]] != " ":
                    i = randint(1, l_pokoje)
                    j = [pokoje[i][0]+randint(0, pokoje[i][2]-1), pokoje[i][1]+randint(0, pokoje[i][3]-1)]
                if m["r"][j[0]][j[1]] != " ":
                    e_id = enemies_class_init(k[0], j[0], j[1], k[1], k[2], k[3], k[4], k[5], k[6], k[7])
                    m["r"][j[0]][j[1]] = "_"+k[0]+zero3(e_id)+"."
                else:
                    e_id = enemies_class_init(k[0], j[0], j[1], k[1], k[2], k[3], k[4], k[5], k[6], k[7])
                    m["r"][j[0]][j[1]] = k[0]+zero3(e_id)+" "
        case 2:
            locate_a_room(m, pokoje, 3, 3, 1, 1, 1)
            #ran = len(pokoje) #len(special_rooms) (<>@) -PR-
            locate_a_room(m, pokoje, 20, 10, 3, 3, 1, True)
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
                Connect(m, p2, middle2)
                Connect(m, p1, middle1, True)
                pokojeok.append(pokojen.pop(n_minodl))
            if stairs > 1:
                m["r"][pokoje[1][0]+pokoje[1][2]//2][pokoje[1][1]+pokoje[-1][3]//2] = "> "
            if stairs % 2 == 1:
                m["r"][pokoje[2][0]+pokoje[2][2]//2][pokoje[2][1]+pokoje[-2][3]//2] = "< "
            l_pokoje = len(pokoje)-1 #-3
            i = randint(3, l_pokoje) #ran=3 -PR-
            j = [pokoje[i][0]+randint(0, pokoje[i][2]-1), pokoje[i][1]+randint(0, pokoje[i][3]-1)]
            for k in items:
                while m["r"][j[0]][j[1]] != " ":
                    i = randint(3, l_pokoje) #ran=3 -PR-
                    j = [pokoje[i][0]+randint(0, pokoje[i][2]-1), pokoje[i][1]+randint(0, pokoje[i][3]-1)]
                m["r"][j[0]][j[1]] = k+" "
            for k in enemies:
                i = randint(3, l_pokoje) #ran=3 -PR-
                j = [pokoje[i][0]+randint(0, pokoje[i][2]-1), pokoje[i][1]+randint(0, pokoje[i][3]-1)]
                while m["r"][j[0]][j[1]] != " ":
                    i = randint(3, l_pokoje) #ran=3 -PR-
                    j = [pokoje[i][0]+randint(0, pokoje[i][2]-1), pokoje[i][1]+randint(0, pokoje[i][3]-1)]
                e_id = enemies_class_init(k[0], j[0], j[1], k[1], k[2], k[3], k[4], k[5], k[6], k[7])
                m["r"][j[0]][j[1]] = k[0]+zero3(e_id)+" "
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
                Connect(m, p2, middle2)
                Connect(m, p1, middle1, True)
                pokojeok.append(pokojen.pop(n_minodl))
            for i in range(ran):
                j = pokoje[i]
                for y in range(j[0]-1, j[0]+j[2]+1):
                    for x in range(j[1]-1, j[1]+j[3]+1):
                        if m["r"][y][x] == "|":
                            m["r"][y][x] = "#"
                        else:
                            if randint(0, 7) == 0:
                                m["r"][y][x] = "_:."
            l_pokoje = l_pokoje-1
            i = randint(1, l_pokoje) # (1→ran) less items in rooms with lihgt
            j = [pokoje[i][0]+randint(0, pokoje[i][2]-1), pokoje[i][1]+randint(0, pokoje[i][3]-1)]
            for k in items:
                while m["r"][j[0]][j[1]] != " ":
                    i = randint(1, l_pokoje)
                    j = [pokoje[i][0]+randint(0, pokoje[i][2]-1), pokoje[i][1]+randint(0, pokoje[i][3]-1)]
                m["r"][j[0]][j[1]] = k+" "
            for k in enemies:
                i = randint(1, l_pokoje) # (1→ran) less monsters in rooms with lihgt
                j = [pokoje[i][0]+randint(0, pokoje[i][2]-1), pokoje[i][1]+randint(0, pokoje[i][3]-1)]
                while m["r"][j[0]][j[1]] != "_." and m["r"][j[0]][j[1]] != " ":
                    i = randint(1, l_pokoje)
                    j = [pokoje[i][0]+randint(0, pokoje[i][2]-1), pokoje[i][1]+randint(0, pokoje[i][3]-1)]
                if m["r"][j[0]][j[1]] != " ":
                    e_id = enemies_class_init(k[0], j[0], j[1], k[1], k[2], k[3], k[4], k[5], k[6], k[7])
                    m["r"][j[0]][j[1]] = "_"+k[0]+zero3(e_id)+"."
                else:
                    e_id = enemies_class_init(k[0], j[0], j[1], k[1], k[2], k[3], k[4], k[5], k[6], k[7])
                    m["r"][j[0]][j[1]] = k[0]+zero3(e_id)+" "
            if stairs > 1:
                m["r"][pokoje[-1][0]+pokoje[-1][2]//2][pokoje[-1][1]+pokoje[-1][3]//2] = "> "
            if stairs % 2 == 1:
                m["r"][pokoje[-2][0]+pokoje[-2][2]//2][pokoje[-2][1]+pokoje[-2][3]//2] = "< "
            m["r"][pokoje[0][0]+pokoje[0][2]//2][pokoje[0][1]+pokoje[0][3]//2] = "_."

        case _:
            return regular_map_init(m, p, items, enemies, type_of_map, stairs)

    return(pokoje[0][0]+pokoje[0][2]//2, pokoje[0][1]+pokoje[0][3]//2)
        #rmap[i[0]+randint(1-sy, sy-1)][i[1]+randint(1-sx, sx-1)] = item

def Connect(m, p_end, p_start, clear = False):
    direction = randint(0, 1)
    goal = True # Do we have a goal? Or it is "done"?
    while goal:
        if direction == 0:
            if p_start[0] < p_end[0]:
                k = (p_start[0]+1) % m["sy"]
            elif p_start[0] > p_end[0]:
                k = (p_start[0]-1 )% m["sy"]
            else:
                k = p_start[0]
                direction += 1
            if m["r"][p_start[0]][p_start[1]] == "|":
                m["r"][p_start[0]][p_start[1]] = "_."
            elif m["r"][p_start[0]][p_start[1]] == "#":#{"#",":"}:
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
                m["r"][p_start[0]][p_start[1]] = "_."
            elif m["r"][p_start[0]][p_start[1]] == "#":#{"#",":"}:
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

def open_doors(rmap, vmap): #Boss is killed -PR-
    for y in range(len(rmap)):
        for x in range(len(rmap[0])):
            if rmap[y][x][0] == "=":
                rmap[y][x] = rmap[y][x][1:]
                if vmap[y][x][0] == "=":
                    vmap[y][x] = rmap[y][x]
            else:
                if len(rmap[y][x]) > 1 and rmap[y][x][1] == "=":
                    rmap[y][x] = rmap[y][x][0] + rmap[y][x][2:]

