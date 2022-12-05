def test_room(m, p1):
    w, k = p1[0], p1[1]
    q = []
    if m["r"][w][k][0] == "_":
        q.append([w, k])
        m["r"][w][k] = m["r"][w][k][1:]
    if m["r"][w-1][k][0] == "_":
        q.append([w-1, k])
        m["r"][w-1][k] = m["r"][w-1][k][1:]
    if m["r"][w+1][k][0] == "_":
        q.append([w+1, k])
        m["r"][w+1][k] = m["r"][w+1][k][1:]
    if m["r"][w][k-1][0] == "_":
        q.append([w, k-1])
        m["r"][w][k-1] = m["r"][w][k-1][1:]
    if m["r"][w][k+1][0] == "_":
        q.append([w, k+1])
        m["r"][w][k+1] = m["r"][w][k+1][1:]

    if m["r"][w-1][k-1][0] == "_":
        q.append([w-1, k-1])
        m["r"][w-1][k-1] = m["r"][w-1][k-1][1:]
    if m["r"][w+1][k-1][0] == "_":
        q.append([w+1, k-1])
        m["r"][w+1][k-1] = m["r"][w+1][k-1][1:]
    if m["r"][w-1][k+1][0] == "_":
        q.append([w-1, k+1])
        m["r"][w-1][k+1] = m["r"][w-1][k+1][1:]
    if m["r"][w+1][k+1][0] == "_":
        q.append([w+1, k+1])
        m["r"][w+1][k+1] = m["r"][w+1][k+1][1:]
    while q != []:
        p1 = q.pop(0)
        w, k = p1[0], p1[1]
        if m["r"][w-1][k][0] == "_":
            q.append([w-1, k])
            m["r"][w-1][k] = m["r"][w-1][k][1:]
        if m["r"][w+1][k][0] == "_":
            q.append([w+1, k])
            m["r"][w+1][k] = m["r"][w+1][k][1:]
        if m["r"][w][k-1][0] == "_":
            q.append([w, k-1])
            m["r"][w][k-1] = m["r"][w][k-1][1:]
        if m["r"][w][k+1][0] == "_":
            q.append([w, k+1])
            m["r"][w][k+1] = m["r"][w][k+1][1:]

        if m["r"][w-1][k-1][0] == "_":
            q.append([w-1, k-1])
            m["r"][w-1][k-1] = m["r"][w-1][k-1][1:]
        if m["r"][w+1][k-1][0] == "_":
            q.append([w+1, k-1])
            m["r"][w+1][k-1] = m["r"][w+1][k-1][1:]
        if m["r"][w-1][k+1][0] == "_":
            q.append([w-1, k+1])
            m["r"][w-1][k+1] = m["r"][w-1][k+1][1:]
        if m["r"][w+1][k+1][0] == "_":
            q.append([w+1, k+1])
            m["r"][w+1][k+1] = m["r"][w+1][k+1][1:]

        for i in range(w-1, w+2):
            for j in range(k-1, k+2):
                m["v"][i][j] = m["r"][i][j]
