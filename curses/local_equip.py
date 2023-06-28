def get_equip_values(p):
    if p["e_attack"]["type"] == "]":
        p["attack"] = p["e_attack"]["values"][0]
        p["attack_acc"] = p["e_attack"]["values"][1]
        p["attack_attacks"] = p["e_attack"]["values"][4]
    else:
        p["attact"] = 1
    if p["e_hand"]["type"] == "}":
        p["bow"] = p["e_hand"]["values"][0]
        p["bow_acc"] = p["e_hand"]["values"][1]
        p["bow_attacks"] = p["e_hand"]["values"][4]
    else:
        p["bow"] = 1
    if p["e_armor"]["type"] == ")":
        p["armor"] = p["e_armor"]["values"][0]
        p["armor_acc"] = p["e_armor"]["values"][1]
    else:
        p["armor"] = 0
    to_delate = []
    p["arrows_id"] = -1
    for i in range(len(p["BP"])):
        if p["BP"][i]["type"] == "" and p["BP"][i]["values"][0] < 1:
            to_delate.append(i)
        elif p["BP"][i]["item"] == "ARROW":
            p["arrows_id"] = i
    for i in to_delate[::-1]:
        p["BP"].pop(i)

BP_mask = []

def f_BP_mask():
    return BP_mask

def update_BP_mask(p): # is local_input
    global BP_mask
    BP_mask = []
    for i in p["BP"]:
        if i["grouping"]:
            BP_mask.append(i["item"])

def merge(p): # polacz (PL) -PR-
    i = 0
    while i < len(p["BP"]):
        j = 1
        while j < len(p["BP"]):
            if i == j:
                j += 1
                continue
            if p["BP"][i]["grouping"] and p["BP"][i]["item"] + " " + p["BP"][i]["type"] == p["BP"][j]["item"] + " " + p["BP"][j]["type"]:
                t1 = p["BP"].pop(j)
                p["BP"][i]["values"][0] += t1["values"][0]
            else:
                j += 1
        i += 1