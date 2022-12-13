from local_translator import translate


def item(item, arg=9, moreinfo=False):
    if arg == 9:
        i = item
    else:
        try:
            i = item[arg]
        except:
            return ("")
    if i["type"] in ["]", "}", ")"]:
        if i["ident"]:
            r = (translate(i["item"][:-2]) + i["item"][-2:] + str(i["values"][0]) + i["type"])
        else:
            r = (translate(i["item"][:-2]) + i["item"][-2:] + "?" + i["type"])
        if moreinfo:
            r += "  "+str(i["values"][1])+"-"+translate("TIER")
            if i["values"][2] > moreinfo:
                r += ", "+translate("YOU NEED")+" "+str(i["values"][2] - moreinfo)+" "+translate("MORE STRENGTH TO EQUIP IT")
                # POTRZEBUJESZ o 3 SIŁY WIĘCEJ, ABY GO WYPOSAŻYĆ -PR-
            else:
                r += ", "+translate("YOU CAN EQUIP IT")
        return r
    elif i["type"] == "|":
        if i["ident"]:
            return (translate(i["values"][0][:-2]) + i["values"][0][-2:] + ("+" if i["values"][1] >= 0 else "") + str(i["values"][1]) + i["type"])
        else:
            return (translate(i["item"][:-2]) + i["item"][-2:] + ("+" if i["values"][1] >= 0 else "") + str(i["values"][1]) + i["type"])
    elif not i["grouping"]: # no identifity for (normal) items -PR-
        #if i["ident"]:
        return (i["item"]  + str(i["values"][0]))
        #else:
        #    return (i["item"] + str(i["values"][0]))
    else:
        return (str(i["values"][0]) + "x " + translate((i["values"][1] if i["values"][0] > 1 else i["item"]), i["values"][0]))
        #return (str(i["values"][0]) + "x " + i["item"] + " " + (i["type"] if i["ident"] else "?"))


def playerdata(y, p):
    match y:
        case 1:
            return " "+p["playertype"]
        case 3:
            return " mana: " + str(p["mana"]) + "/" + str(p["maxmana"])
        case 4:
            return " hp: " + str(p["hp"]) + "/" + str(p["maxhp"])
        case 5:
            return " xp: " + str(p["xp"])
        case 6:
            return " lw: " + str(p["lw"])
        case 7:
            return " depth: " + str(p["depth"])
        case 8:
            return " strength: " + str(p["strength"])
        case 9:
            return " gold: " + str(p["gold"])
        case 11:
            return " attack: " + str(p["attack"])
        case 12:
            return "    bow: " + str(p["bow"])
        case 13:
            return "  armor: " + str(p["armor"])
        case 15:
            return " " + item(p["BP"], 0)
        case 16:
            return " " + item(p["BP"], 1)
        case 17:
            return " " + item(p["BP"], 2)
        case 18:
            return " " + item(p["BP"], 3)
        case 19:
            return " " + item(p["BP"], 4)
        case 20:
            return " " + item(p["BP"], 5)
        case 22:
            return " attack by: " + p["wasattackby"]
        case _:
            return "=----------------------="


def output(m, p):
    if p["torch"] == 1:
        for y in range(-1, 2):  # In the future I will make it better !!!
            for x in range(-1, 2):
                i = [(p["y"] + y) % m["sy"], (p["x"] + x) % m["sx"]]
                if m["r"][i[0]][i[1]][0] == "_":
                    m["r"][i[0]][i[1]] = m["r"][i[0]][i[1]][1:]
                m["v"][i[0]][i[1]] = m["r"][i[0]][i[1]]
    for y in range(m["sy"]):
        m["o"][y] = m["v"][y].copy()
    #     for x in range(m["sx"]):
    #         m["o"][y][x] = m["v"][y][x]
    m["o"][p["y"]][p["x"]] = "@"
    if p["torch"] == 1:
        for y in range(-1, 2):
            for x in range(-1, 2):
                i = [(p["y"] + y) % m["sy"], (p["x"] + x) % m["sx"]]
                if m["o"][i[0]][i[1]] == " ":
                    m["o"][i[0]][i[1]] = "."
    j = ""
    for y in range(23):
        ty = p["y"] + y - 11
        if ty >= 0 and ty < m["sy"]:
            i = ""
            for x in range(53):
                tx = p["x"] + x - 26
                if tx >= 0 and tx < m["sx"]:
                    try: # for testing m["m"] and move enemies -PR-
                        i += m["m"][ty][tx][0]
                    except:
                        i += m["o"][ty][tx][0]
                else:
                    i += " "
        else:
            i = "                                                     "
        j += i + "| " + playerdata(y, p) + "\n"
    return j
