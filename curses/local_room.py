darktiles = {" ","#","^","+"}

def test_room(m, p, view = 0):
    q = [[p[0], p[1], 0]]
    m["m"] = [[True for _ in range(m["sx"])] for _ in range(m["sy"])]
    while q != []:
        p = q.pop(0)
        d = p[2]
        w, k, d = p[0], p[1], d+1
        if d != view:
            #if m["r"][w][k][-1] not in darktiles:
            #    q.append([w, k, d])
            if m["r"][w-1][k][-1] not in darktiles:
                if m["m"][w-1][k]:
                    m["m"][w-1][k] = False
                    q.append([w-1, k, d])
            if m["r"][w+1][k][-1] not in darktiles:
                if m["m"][w+1][k]:
                    m["m"][w+1][k] = False
                    q.append([w+1, k, d])
            if m["r"][w][k-1][-1] not in darktiles:
                if m["m"][w][k-1]:
                    m["m"][w][k-1] = False
                    q.append([w, k-1, d])
            if m["r"][w][k+1][-1] not in darktiles:
                if m["m"][w][k+1]:
                    m["m"][w][k+1] = False
                    q.append([w, k+1, d])

            if m["r"][w-1][k-1][-1] not in darktiles:
                if m["m"][w-1][k-1]:
                    m["m"][w-1][k-1] = False
                    q.append([w-1, k-1, d])
            if m["r"][w+1][k-1][-1] not in darktiles:
                if m["m"][w+1][k-1]:
                    m["m"][w+1][k-1] = False
                    q.append([w+1, k-1, d])
            if m["r"][w-1][k+1][-1] not in darktiles:
                if m["m"][w-1][k+1]:
                    m["m"][w-1][k+1] = False
                    q.append([w-1, k+1, d])
            if m["r"][w+1][k+1][-1] not in darktiles:
                if m["m"][w+1][k+1]:
                    m["m"][w+1][k+1] = False
                    q.append([w+1, k+1, d])

        for i in range(w-1, w+2):
            for j in range(k-1, k+2):
                m["v"][i][j] = m["r"][i][j]
