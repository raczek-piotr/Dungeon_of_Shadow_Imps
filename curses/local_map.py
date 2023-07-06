from random import randint, choice

from local_scripts import zero3
from local_enemies_class import enemies_class_add
from local_boss_map import boss_map_init


def map_init_str(m, p, items, type_of):
    with open("maps/"+type_of+".map", "r") as rm: # readmap -PR-
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
                    elif m["r"][y+1][x+1][0] == "@": # for the future -PR-
                        pass
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


def map_init(m, p, items, type_of = 0, stairs = 3):
    if type(type_of) == type(0):
        return map_init_int(m, p, items, type_of, stairs) if type_of < 100 else boss_map_init(m, p, items, type_of, stairs)
    else:
        return map_init_str(m, p, items, type_of)


def map_init_int(m, p, items, type_of, stairs):
    pokoje = []
    m["sy"], m["sx"] = 33, 33
    m["r"] = [["#" for _ in range(m["sx"])] for _ in range(m["sy"])]
    m["v"] = [[" " for _ in range(m["sx"])] for _ in range(m["sy"])]
    m["o"] = m["v"].copy()

    match type_of:
        case 1:
            hm = 5
            minhm = 4
            pokoje = []
            tryes = 0
            sizey, sizex = 16, 16 # 0 makes self -PR-
            m["sy"], m["sx"] = 2*sizey+1, 2*sizex+1
            m["r"] = [["#" for _ in range(m["sx"])] for _ in range(m["sy"])]
            m["v"] = [[" " for _ in range(m["sx"])] for _ in range(m["sy"])]
            m["o"] = m["v"].copy()
            while len(pokoje) < minhm or tryes < hm:
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
            
            hm = 10
            minhm = 8 # should be space on the map -PR-
            Spokoje = []
            tryes = 0
            while len(Spokoje) < minhm or tryes < hm:
                sy, sx = 1+2*randint(0,4), 1+2*randint(0,5)
                y, x = 1+2*randint(0, sizey - sy), 1+2*randint(0, sizex - sx)
                can, tryes = True, tryes + 1
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

            hm = len(pokoje)
            for it in range(hm):
                for y in range(pokoje[it][0]-1, pokoje[it][0] + pokoje[it][2] +1):
                    for x in range(pokoje[it][1]-1, pokoje[it][1] + pokoje[it][3] +1):
                        m["r"][y][x] = "|"
            Spokoje.extend(pokoje)
            for it in range(len(Spokoje)):
                RegularConnect(m, Spokoje[it-1].copy(), Spokoje[it].copy())

            #for it in range(hm):
            #    RegularConnect(m, pokoje[it-1].copy(), pokoje[it].copy())
            for it in range(hm):
                for y in range(pokoje[it][0], pokoje[it][0] + pokoje[it][2]):
                    for x in range(pokoje[it][1], pokoje[it][1] + pokoje[it][3]):
                        m["r"][y][x] = "_."
            for it in range(hm):
                for y in range(pokoje[it][0]-1, pokoje[it][0] + pokoje[it][2] +1):
                    for x in range(pokoje[it][1]-1, pokoje[it][1] + pokoje[it][3] +1):
                        if m["r"][y][x] == "|":
                            m["r"][y][x] = "#"
            if stairs > 1:
                m["r"][pokoje[-2][0]+pokoje[-2][2]//2][pokoje[-2][1]+pokoje[-2][3]//2] = "_>."
            if stairs % 2 == 1:
                m["r"][pokoje[-3][0]+pokoje[-3][2]//2][pokoje[-3][1]+pokoje[-3][3]//2] = "_<."

            pokoje = Spokoje
            l_pokoje = len(pokoje)-1
            i = randint(0, l_pokoje)
            j = [pokoje[i][0]+randint(0, pokoje[i][2]-1), pokoje[i][1]+randint(0, pokoje[i][3]-1)]
            for k in items:
                while m["r"][j[0]][j[1]] not in {"_.", " "}:
                    i = randint(0, l_pokoje)
                    j = [pokoje[i][0]+randint(0, pokoje[i][2]-1), pokoje[i][1]+randint(0, pokoje[i][3]-1)]
                if m["r"][j[0]][j[1]] == " ":
                    m["r"][j[0]][j[1]] = k+" "
                else:
                    m["r"][j[0]][j[1]] = "_"+k+"."
            pokoje[0] = pokoje[-1] # for good place player to start -PR-
        case 2:
            locate_a_room(m, pokoje, 25, 10, 3, 3, 1, True)
            locate_a_room(m, pokoje, 15, 0, 1, 1, 0)
            for i in range(len(pokoje)):
                j = pokoje[i]
                for y in range(j[0], j[0]+j[2]):
                    for x in range(j[1], j[1]+j[3]):
                        m["r"][y][x] = " "
            pokojen = pokoje.copy()
            pokojeok = [pokojen.pop(0)]
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
                #middle = [(p1[0]+p2[0])//2, (p1[1]+p2[1])//2]
                Connect(m, p2, [m["sx"]//2, m["sy"]//2])
                Connect(m, p1, [m["sx"]//2, m["sy"]//2], True)
                pokojeok.append(pokojen.pop(n_minodl))
            if stairs > 1:
                m["r"][pokoje[-1][0]+pokoje[-1][2]//2][pokoje[-1][1]+pokoje[-1][3]//2] = "> "
                m["r"][pokoje[-3][0]+pokoje[-3][2]//2][pokoje[-3][1]+pokoje[-3][3]//2] = "> "
            if stairs % 2 == 1:
                m["r"][pokoje[-2][0]+pokoje[-2][2]//2][pokoje[-2][1]+pokoje[-2][3]//2] = "< "
                m["r"][pokoje[-4][0]+pokoje[-4][2]//2][pokoje[-4][1]+pokoje[-4][3]//2] = "< "
            l_pokoje = len(pokoje)-1 # like l_pokoje -= 1 -PR-
            i = randint(3, l_pokoje) #ran=3 -PR-
            j = [pokoje[i][0]+randint(0, pokoje[i][2]-1), pokoje[i][1]+randint(0, pokoje[i][3]-1)]
            for k in items:
                while m["r"][j[0]][j[1]] != " ":
                    i = randint(3, l_pokoje) #ran=3 -PR-
                    j = [pokoje[i][0]+randint(0, pokoje[i][2]-1), pokoje[i][1]+randint(0, pokoje[i][3]-1)]
                m["r"][j[0]][j[1]] = k+" "
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
                if i == ran: #rest of rooms have no light
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
                        elif m["r"][y][x] == "+":
                            m["r"][y][x] = ":."
                        else:
                            if randint(0, 7) == 0:
                                m["r"][y][x] = "_:."
            l_pokoje -= 1
            i = randint(1, l_pokoje) # (1→ran) less items in rooms with lihgt
            j = [pokoje[i][0]+randint(0, pokoje[i][2]-1), pokoje[i][1]+randint(0, pokoje[i][3]-1)]
            for k in items:
                while m["r"][j[0]][j[1]] != " ":
                    i = randint(1, l_pokoje)
                    j = [pokoje[i][0]+randint(0, pokoje[i][2]-1), pokoje[i][1]+randint(0, pokoje[i][3]-1)]
                m["r"][j[0]][j[1]] = k+" "
            if stairs > 1:
                m["r"][pokoje[-1][0]+pokoje[-1][2]//2][pokoje[-1][1]+pokoje[-1][3]//2] = "> "
                m["r"][pokoje[-3][0]+pokoje[-3][2]//2][pokoje[-3][1]+pokoje[-3][3]//2] = "> "
            if stairs % 2 == 1:
                m["r"][pokoje[-2][0]+pokoje[-2][2]//2][pokoje[-2][1]+pokoje[-2][3]//2] = "< "
                m["r"][pokoje[-4][0]+pokoje[-4][2]//2][pokoje[-4][1]+pokoje[-4][3]//2] = "< "
            m["r"][pokoje[0][0]+pokoje[0][2]//2][pokoje[0][1]+pokoje[0][3]//2] = "_."

        case _: # 0 -PR-
            hm = 25
            minhm = 9 # 5 -PR-
            pokoje = []
            tryes = 0
            sizey, sizex = 17, 26
            m["sy"], m["sx"] = 2*sizey+1, 2*sizex+1
            m["r"] = [["#" for _ in range(m["sx"])] for _ in range(m["sy"])]
            m["v"] = [[" " for _ in range(m["sx"])] for _ in range(m["sy"])]
            m["o"] = [[" " for _ in range(m["sx"])] for _ in range(m["sy"])]
            while len(pokoje) < minhm or tryes < hm:
                sy, sx = 1+2*randint(1,2), 1+2*randint(1,3)
                y, x = 1+2*randint(0, sizey - sy), 1+2*randint(0, sizex - sx) if tryes != 0 else 1 #on left boarder
                can, tryes = True, tryes + 1
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
                        m["r"][y][x] = "_."
            for it in range(hm):
                for y in range(pokoje[it][0]-1, pokoje[it][0] + pokoje[it][2] +1):
                    for x in range(pokoje[it][1]-1, pokoje[it][1] + pokoje[it][3] +1):
                        if m["r"][y][x] == "|":
                            m["r"][y][x] = "#"
            if stairs > 1:
                m["r"][pokoje[-2][0]+pokoje[-2][2]//2][pokoje[-2][1]+pokoje[-2][3]//2] = "_>."
            if stairs % 2 == 1:
                m["r"][pokoje[-3][0]+pokoje[-3][2]//2][pokoje[-3][1]+pokoje[-3][3]//2] = "_<."
            l_pokoje = hm-2
            i = randint(0, l_pokoje)
            j = [pokoje[i][0]+randint(0, pokoje[i][2]-1), pokoje[i][1]+randint(0, pokoje[i][3]-1)]
            for k in items:
                while m["r"][j[0]][j[1]] != "_.":
                    i = randint(0, l_pokoje)
                    j = [pokoje[i][0]+randint(0, pokoje[i][2]-1), pokoje[i][1]+randint(0, pokoje[i][3]-1)]
                m["r"][j[0]][j[1]] = "_"+k+"."

    more = True # here are added enemies on "battle field" :) -PR-
    while more:
        i = randint(1, l_pokoje) # (1→ran) player with nonething in start_room -PR-
        j = [pokoje[i][0]+randint(0, pokoje[i][2]-1), pokoje[i][1]+randint(0, pokoje[i][3]-1)]
        while m["r"][j[0]][j[1]] != "_." and m["r"][j[0]][j[1]] != " ":
            i = randint(1, l_pokoje)
            j = [pokoje[i][0]+randint(0, pokoje[i][2]-1), pokoje[i][1]+randint(0, pokoje[i][3]-1)]
        e_id, more = enemies_class_add(j[1], j[0], type_of, p["depth"])
        if m["r"][j[0]][j[1]] != " ":
            m["r"][j[0]][j[1]] = "_"+e_id+"."
        else:
            m["r"][j[0]][j[1]] = e_id+" "
    return(pokoje[0][0]+pokoje[0][2]//2, pokoje[0][1]+pokoje[0][3]//2)
        #rmap[i[0]+randint(1-sy, sy-1)][i[1]+randint(1-sx, sx-1)] = item

def RegularConnect(m, p_end, p_start):
    p_end[0], p_end[1] = p_end[0] + 2 * randint(0,p_end[2]//2), p_end[1] + 2 * randint(0,p_end[3]//2)
    p_start[0], p_start[1] = p_start[0] + 2 * randint(0,p_start[2]//2), p_start[1] + 2 * randint(0,p_start[3]//2)
    direction = randint(0, 1)
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
            if m["r"][k][p_start[1]] == "|" or m["r"][k][p_start[1]] == "+":
                m["r"][k][p_start[1]] = "+"
            elif m["r"][k][p_start[0]] != "_.":
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
            if m["r"][p_start[0]][k] == "|" or m["r"][p_start[0]][k] == "+":
                m["r"][p_start[0]][k] = "+"
            elif m["r"][p_start[0]][k] != "_.":
                m["r"][p_start[0]][k] = " "
            p_start[1] = 2*k-p_start[1]
            m["r"][p_start[0]][p_start[1]] = " "
        if p_start[0] == p_end[0] and p_start[1] == p_end[1]:
            goal = False
        if randint(0, 99) < 20:
            direction = (direction+1) % 2

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
                m["r"][p_start[0]][p_start[1]] = "+"
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
                m["r"][p_start[0]][p_start[1]] = "+"
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
