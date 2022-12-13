def get_equip_values(p):
    if p["e_attack"]["type"] == "]":
        p["attack"] = p["e_attack"]["values"][0]
    else:
        p["attact"] = 1
    if p["e_hand"]["type"] == "}":
        p["bow"] = p["e_hand"]["values"][0]
    else:
        p["bow"] = 1
    if p["e_armor"]["type"] == ")":
        p["armor"] = p["e_armor"]["values"][0]
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
