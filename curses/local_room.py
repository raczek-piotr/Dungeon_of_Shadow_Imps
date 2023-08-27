darktiles = {" ","#","^","+"}

def test_room(m, p):
    q = [[p[0], p[1], 1]]
    m["m"] = [[True for _ in range(m["sx"])] for _ in range(m["sy"])]
    while q != []:
        p = q.pop(0)
        d = p[2]
        if d < 50:
            w, k, d = p[0], p[1], d+1
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
