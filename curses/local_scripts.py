def dire(e, p):
    dire = [0, 0] # direction -PR-
    if p[0] < e[0]:
        dire[0] = 1
    elif p[0] > e[0]:
        dire[0] = -1
    if p[1] < e[1]:
        dire[1] = 1
    elif p[1] > e[1]:
        dire[1] = -1
    return dire

def shot(rmap, p, dire, tlist, hr = 7): # hr - hear_range -PR-
    ty, tx = p
    r = 0
    while rmap[ty][tx][0] in tlist and r < hr:
        ty, tx, r = ty+dire[0], tx+dire[1], r+1
    return [ty, tx]

def zero3(i):
    i = str(i)
    while len(i) < 3:
        i = "0" + i
    return i

def is_boss_killed(m, p, head): #Boss is killed (if)-PR-
    if head == "B":
        p["strength"] += 1
        p["dexterity"] += 1
        rmap, vmap = m["r"], m["v"]
        for y in range(len(rmap)):
            for x in range(len(rmap[0])):
                if rmap[y][x][0] == "=":
                    rmap[y][x] = rmap[y][x][1:]
                    if vmap[y][x][0] == "=":
                        vmap[y][x] = rmap[y][x]
                else:
                    if len(rmap[y][x]) > 1 and rmap[y][x][1] == "=":
                        rmap[y][x] = rmap[y][x][0] + rmap[y][x][2:]