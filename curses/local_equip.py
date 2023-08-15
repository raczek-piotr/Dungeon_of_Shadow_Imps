def get_equip_values(p):
    if p["e_attack"][1] == "]": # alwayes True -PR-
        p["attack"] = p["e_attack"][2][0]
        p["attack_damage"] = p["e_attack"][2][1]
        p["attack_acc"] = p["e_attack"][2][3]
        p["attack_hits"] = p["e_attack"][2][2]
        tv = p["e_attack"][2][-2] - p["strength"]
        ta = p["e_attack"][2][-1] - p["dexterity"]
        if tv > 0:
            p["attack"] = (2*p["attack"])//(1+tv)
            p["attack_damage"] = (2*p["attack_damage"])//(1+tv)
        if ta > 0:
            p["attack_acc"] = (2*p["attack_acc"])//(1+ta)
            p["attack_hits"] = (2*p["attack_hits"])//(1+ta)
    else:
        p["attack"], p["attack_attacks"], p["attack_acc"], p["attack_hits"] = 1,0,0,0

    if p["e_hand"][1] == "}":
        p["bow"] = p["e_hand"][2][0]
        p["bow_damage"] = p["e_hand"][2][1]
        p["bow_acc"] = p["e_hand"][2][3]
        p["bow_hits"] = p["e_hand"][2][2]
        tv = p["e_hand"][2][-2] - p["strength"]
        ta = p["e_hand"][2][-1] - p["dexterity"]
        if tv > 0:
            p["bow"] //= (1+tv)
            p["bow_damage"] //= (1+tv)
        if ta > 0:
            p["bow_acc"] //= (1+ta)
            p["bow_hits"] //= (1+ta)
    else:
        p["bow"], p["bow_attacks"], p["bow_acc"], p["bow_hits"] = 1,0,0,0

    if p["e_armor"][1] == ")":
        p["armor"] = p["e_armor"][2][0]
        p["defend"] = p["basedefend"]
        t = p["e_armor"][2][1] - p["lw"]
        if t > 0:
            p["armor"] = (2*p["armor"])//(2+t)
        if t > 0:
            p["defend"] -= 10*t
    else:
        p["armor"] = 0

    if p["e_shield"][1] == ")":
        p["shield"] = p["e_shield"][2][0]
        t = p["e_shield"][2][1] - p["lw"]
        if t > 0:
            p["shield"] -= t
            if p["shield"] < 0:
                p["shield"] = 0
    else:
        p["shield"] = 0
    p["armor"] += p["shield"]

    to_delate = []
    p["arrows_id"] = -1
    #for i in range(len(p["BP"])):
    #    if (#p["BP"][i][1] not in {"]",")","}"} and
    #        p["BP"][i][2] < 1):
    #        to_delate.append(i)
    #    elif p["BP"][i][1] == "ARROW":
    #        p["arrows_id"] = i
    for i in to_delate[::-1]:
        p["BP"].pop(i)

def merge(p): # polacz (PL) -PR-
    i = 0
    while i < len(p["BP"]):
        j = 1
        while j < len(p["BP"]):
            if i == j:
                j += 1
                continue
            if p["BP"][i][1] == "-" and p["BP"][i][0] == p["BP"][j][0]:
                t1 = p["BP"].pop(j)
                p["BP"][i][2] += t1[2]
            else:
                j += 1
        i += 1