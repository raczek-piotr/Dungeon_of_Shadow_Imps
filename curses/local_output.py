#import curses as c
from local_translator import translate
spacer = "=----------------------="

def item(item, arg=9, p=False): #if moreinfo != False then moreinfo = p -PR-
    if arg >= 9:
        i = item
    else:
        try:
            i = item[arg]
        except:
            return ("")
    match i[1]:
        case "]":
            r = translate(i[0][0])+" "+str(i[2][0])+"D"+str(i[2][1])+" "+(str(i[2][2])+"H"+str(i[2][3])+"%")
            
            if p:
                i = i[2][-2]-p["strength"], i[2][-1]-p["dexterity"]
                i = i[0] if i[0] > 0 else 0, i[1] if i[1] > 0 else 0
                if i[0] > 0 or i[1] > 0:
                    r += " "+translate("YOU NEED")+" "+str(i[0])+"|"+str(i[1])+" "+translate("MORE")
            return r
        case "}":
            r = translate(i[0][0])+" "+str(i[2][0])+"D"+str(i[2][1])+" "+(str(i[2][2])+"H"+str(i[2][3])+"%")
            
            if p:
                i = i[2][-2]-p["strength"], i[2][-1]-p["dexterity"]
                i = i[0] if i[0] > 0 else 0, i[1] if i[1] > 0 else 0
                if i[0] > 0 or i[1] > 0:
                    r += " "+translate("YOU NEED")+" "+str(i[0])+"|"+str(i[1])+" "+translate("MORE")
            return r
                        # POTRZEBUJESZ o 3 SIŁY WIĘCEJ, ABY GO WYPOSAŻYĆ -PR-
        case ")":
            r = translate(i[0][0])+" "+str(i[2][0])
            if p:
                i = i[2][-1]-p["lw"] # new i, and i ≠ i -PR-
                if i > 0 :
                    r += " "+translate("YOU NEED")+" "+str(i)+" LW(S) "+translate("MORE")
                        # POTRZEBUJESZ o 3 SIŁY WIĘCEJ, ABY GO WYPOSAŻYĆ -PR-
            return r
        case "-":
            r = translate(i[0][0] if (i[2] == 1 and arg != 10) else i[0][1])
            if arg != 10:
                r = str(i[2])+"x "+r
            return r
        case _:
            return translate(i[0][0])


def playerdata(y, p):
    match y:
        #case 1:
        #    return p["playertype"]
        case 3:
            return "hp: " + str(p["hp"]) + "/" + str(p["maxhp"])
        case 4:
            return "xp: " + str(p["xp"]) + "/" + str(p["needxp"])
        case 5:
            return "lw: " + str(p["lw"])
        case 6:
            return "depth: " + str(p["depth"])
        case 7:
            if p["inteligence"] > 0:
                return "str|dex|int"
            return "str|dex"
        case 8:
            if p["inteligence"] > 0:
                return " "*(3-len(str(p["strength"])))+str(p["strength"])+"|"+" "*(3-len(str(p["dexterity"])))+str(p["dexterity"])+"|"+" "*(3-len(str(p["inteligence"])))+str(p["inteligence"])
            return " "*(3-len(str(p["strength"])))+str(p["strength"])+"|"+str(p["dexterity"])
        case 9:
            return "gold: " + str(p["gold"])
        case 11:
            return " attack: " + str(p["attack"])+"D"+str(p["attack_damage"])+" "+(str(p["attack_hits"])+"H"+str(p["attack_acc"])+"%")
        case 12:
            if p["magic_list"]:
                return "  " + p["hand_name"]
            return "  range: " + p["hand_name"]
        case 13:
            return "  armor: " + str(p["armor"])#+"+"+str(p["shield"])
        case 15:
            return item(p["BP"], 0)
        case 16:
            return item(p["BP"], 1)
        case 17:
            return item(p["BP"], 2)
        case 18:
            return item(p["BP"], 3)
        case 19:
            return item(p["BP"], 4)
        case 20:
            return item(p["BP"], 5)
        case 22:
            return "attack by:"
        case _:
            return ""


def output(w, c, m, p):
    if p["torch"]:
        for y in range(-1, 2):
            for x in range(-1, 2):
                i = [(p["y"] + y) % m["sy"], (p["x"] + x) % m["sx"]]
                m["v"][i[0]][i[1]] = m["r"][i[0]][i[1]]

    for y in range(23):
        ty = p["y"] + y - 11
        if ty >= 0 and ty < m["sy"]:
            t = m["v"][ty]
            for x in range(53):
                tx = p["x"] + x - 26
                if tx >= 0 and tx < m["sx"]:
                    i = t[tx][0]
                    if i in {"@","]","}",")","~","$","*","-","?","!","%","~"}:
                        col = 2
                    elif i == "#":
                        col = 8
                    elif i == "=":
                        col = 6
                    elif i == "&":
                        col = 7
                    elif i in {"<",">","+",",",":"}:
                        col = 4
                    elif i.upper() != i.lower():
                        col = 3
                    else:
                        col = 1
                    w.addstr(y, x, i, c.color_pair(col))
        w.addstr(y, 53, "|", c.color_pair(4))
        w.addstr(y, 56, playerdata(y, p), c.color_pair(1))
    w.addstr(1, 56, p["playertype"], c.color_pair(p["color"]))
    if p["torch"]:
        for y in range(-1, 2):
            ty = (p["y"] + y) % m["sy"]
            for x in range(-1, 2):
                i = [ty, (p["x"] + x) % m["sx"]]
                if m["v"][i[0]][i[1]] == " ":
                    w.addstr(11+y, 26+x, ".", c.color_pair(1))
    w.addstr(22, 67, p["wasattackby"], c.color_pair(3))
    w.addstr(0, 55, spacer, c.color_pair(4))
    w.addstr(2, 55, spacer, c.color_pair(4))
    w.addstr(10, 55, spacer, c.color_pair(4))
    if p["starving"]:
        w.addstr(12, 56, "S", c.color_pair(3))
    if not p["torch"]:
        w.addstr(13, 56, "L", c.color_pair(3))
    if p["blessing"]:
        w.addstr(12, 55, "B", c.color_pair(2))
    if p["fury"]:
        w.addstr(13, 55, "F", c.color_pair(2))
    if p["environment_bonus"]:
        w.addstr(11, 55, str(p["environment_bonus"]), c.color_pair(8))
    w.addstr(14, 55, spacer, c.color_pair(4))
    w.addstr(21, 55, spacer, c.color_pair(4))
    w.addstr(11, 26, "@", c.color_pair(1))
