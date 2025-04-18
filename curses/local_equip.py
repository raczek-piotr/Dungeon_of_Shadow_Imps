def get_equip_values(p):
    if p["e_attack"][1] == "]": # alwayes True -PR-
        p["attack"] = p["e_attack"][2][0]
        p["attack_damage"] = p["e_attack"][2][1]
        p["attack_acc"] = p["e_attack"][2][3]
        p["attack_hits"] = p["e_attack"][2][2]
        tv = p["e_attack"][2][-2] - p["strength"]
        ta = p["e_attack"][2][-1] - p["dexterity"]
        if tv > 0:
            p["attack"] = (p["attack"])//(1+tv)
        if ta > 0:
            p["attack_acc"] = (p["attack_acc"])//(1+ta)
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
            p["bow"] = (p["bow"])//(1+tv)
        if ta > 0:
            p["bow_acc"] = (p["bow_acc"])//(2+ta) #rogue with short bow is op with 1 -PR-
        p["magic_list"] = False
        p["hand_name"] = str(p["bow"])+"D"+str(p["bow_damage"])+" "+(str(p["bow_hits"])+"H"+str(p["bow_acc"])+"%")
    elif p["e_hand"][1] == "??":
        p["bow"] = False
        p["bow_damage"] = 0
        p["bow_acc"] = 0
        p["bow_hits"] = 0
        p["magic_list"] = p["e_hand"][2]
        p["hand_name"] = p["e_hand"][0][0]
    else:
        p["bow"], p["bow_attacks"], p["bow_acc"], p["bow_hits"] = 0,0,0,0
        p["hand_name"] = "0D0 0H0%"

    if p["e_armor"][1] == ")":
        p["armor"] = p["e_armor"][2][0]
        p["defend"] = p["basedefend"]
        t = p["e_armor"][2][1] - p["lw"]
        if t > 0:
            p["armor"] = (2*p["armor"])//(2+t)
            p["defend"] -= 10*t
    else:
        p["armor"] = 0

def merge(p): # polacz (PL) -PR-
    i = 0
    while i < len(p["BP"]): #marge only "-"
        j = 1
        while j < len(p["BP"]):
            if i == j:
                j += 1
                continue
            if p["BP"][i][1] in {"-"} and p["BP"][i][0] == p["BP"][j][0]:
                t1 = p["BP"].pop(j)
                p["BP"][i][2] += t1[2]
            else:
                j += 1
        i += 1