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
