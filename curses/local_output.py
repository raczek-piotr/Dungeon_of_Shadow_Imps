import curses as c
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
            return " attack by:"
        case _:
            return ""


def output(w, m, p):
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
    q = """    j = ""
    for y in range(23):
        ty = p["y"] + y - 11
        if ty >= 0 and ty < m["sy"]:
            i = ""
            for x in range(53):
                tx = p["x"] + x - 26
                if tx >= 0 and tx < m["sx"]:
                    #try: # for testing m["m"] and move enemies -PR-
                    #    i += m["m"][ty][tx][0]
                    #except:
                        i += m["o"][ty][tx][0]
                else:
                    i += " "
            w.addstr(y, 0, i + "| " + playerdata(y, p))
        w.addstr(y, 53, "| " + playerdata(y, p))"""
    #c.init_pair(1, c.COLOR_RED, c.COLOR_WHITE)
    c.init_pair(1, 231, 16)
    c.init_pair(2, 46, 16)
    c.init_pair(3, 5, 16)
    c.init_pair(4, 136, 16)
    c.init_pair(5, 245, 16)#148 :) -PR-
    for y in range(23):
        ty = p["y"] + y - 11
        if ty >= 0 and ty < m["sy"]:
            t = m["o"][ty]
            for x in range(53):
                tx = p["x"] + x - 26
                if tx >= 0 and tx < m["sx"]:
                    if t[tx] == "":
                        t[tx] = "!"
                    i = t[tx][0]
                    if i in {"]","}",")","~","$","*","-","?"}:
                        w.addstr(y, x, i, c.color_pair(2))
                    elif i == "#":
                        w.addstr(y, x, i, c.color_pair(5))
                    elif i in {"<",">","+",",",":"}:
                        w.addstr(y, x, i, c.color_pair(4))
                    elif i.upper() != i.lower():
                        w.addstr(y, x, i, c.color_pair(3))
                    else:
                        w.addstr(y, x, i, c.color_pair(1))
        w.addstr(y, 53, "|", c.color_pair(4))
        w.addstr(y, 55, playerdata(y, p), c.color_pair(1))
        w.addstr(22, 67, p["wasattackby"], c.color_pair(3))
        w.addstr(0, 55, "=----------------------=", c.color_pair(4))
        w.addstr(2, 55, "=----------------------=", c.color_pair(4))
        w.addstr(10, 55, "=----------------------=", c.color_pair(4))
        if p["starving"]:
            w.addstr(12, 55, "S", c.color_pair(3))
        if not p["torch"]:
            w.addstr(13, 55, "L", c.color_pair(3))
        w.addstr(14, 55, "=----------------------=", c.color_pair(4))
        w.addstr(21, 55, "=----------------------=", c.color_pair(4))
