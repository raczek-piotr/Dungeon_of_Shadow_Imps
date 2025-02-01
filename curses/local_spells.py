from local_output import output
from local_input_key import *
from local_enemies_class import enemies_class_is_cast, enemies_class_is_blast
from local_translator import translate

from random import randint, choice


spell_list = [
# name,						 2% 6=,chance,2D_value,inteligence_needed, magic, flag_if_value_is_False
# spellbook (10)
[translate("MAGIC LIGHT"),    1,    70,  False,   10, 3, 0],#0
[translate("TELEPORTATION"),  1,    70,  False,   10, 3, 1],#1
[translate("MAGIC MISSLE"),   1,    70,  1,       10, 1],   #2
# druid spells (10)
[translate("DEDECT NATURE"),  1,    60,  False,   10, 5, 3],#3
[translate("DRUID'S SHOT"),   2,    60,  5,       11, 1],   #4
[translate("WORDS OF NATURE"),1,    60,  False,   12, 3, 4],#5
[translate("HERBALIZM"),      2,    60,  False,   13, 1, 2],#6
# water language (12)
[translate("DETECT WATER"),   1,    80,  False,   10, 5, 5],#7
[translate("WATER JUMP"),     1,    80,  False,   11, 1, 7],#8
[translate("CONDENCE HUMID"), 1,    80,  False,   12, 3, 6],#9
[translate("WATER FIST"),     6,    80,  5,       13, 1],   #10
[translate("TSUNAMI"),        6,    80,  8,       14, 2],   #11
[translate("HYDROGEN BLAST"), 6,    60,  False,   15, 5, 8],#12
# fire conpendium (12)
[translate("FIRE BALL"),      1,    70,  5,       13, 1],   #13
[translate("LIGHTNING"),      1,    70,  9,       14, 5],   #14
]

def spell_menager(w, c, m, p):
    q = "-1" # not in slots -PR-
    slots = set()
    colors = list()
    for i in range(len(p["magic_list"])):
        q = m["r"][p["y"]][p["x"]][0]
        ml = spell_list[p["magic_list"][i]]
        if ml[4] <= p["inteligence"]:
            if (ml[1] == 1 or (ml[1] == 2 and q == "%") or (ml[1] == 6 and q == "=")):
                slots.add(str(i+1))
                colors.append(1)
            else:
                colors.append(ml[1])
        else:
            colors.append(9)
    q = "-1" # not in slots -PR-
    while q not in slots:
        if q in {"PADENTER","\n", ",", "\x1b", "0"}:
            return[p["echo"], False]
        w.clear()
        output(w, c, m, p)
        for i in range(6):
            w.addstr(15+i, 55, " "*24, c.color_pair(1))
        for i in range(len(p["magic_list"])):
            ml = spell_list[p["magic_list"][i]]
            w.addstr(15+i, 55, str(i+1) + ". " + ml[0], c.color_pair(colors[i]))
        w.addstr(23, 0, translate("CHOOSE A SPELL TO CAST:"), c.color_pair(2))
        q = get_in(w)
    q = int(q)-1
    if spell_list[p["magic_list"][q]][3]:
        w.clear()
        output(w, c, m, p)
        w.addstr(23, 0, translate("IN WHAT DIRECTION DO YOU WANT TO CAST THE SPELL?:"), c.color_pair(2))
        it = get_in(w)
        dy, dx, t1 = player_move(it)
        if t1 and it != "5":
            p["cur_magic"] += spell_list[p["magic_list"][q]][5]
            if spell_list[p["magic_list"][q]][2] <= randint(0, 99): # test the spell -PR-
                return[translate("YOU FAILED TO CAST THE SPELL"), True]
            enemies_class_is_cast(m, p, [dy, dx], spell_list[p["magic_list"][q]][3])
            return[p["echo"], True]
        return[translate("WRONG DIRECTION!"), False]
    #else:
    p["cur_magic"] += spell_list[p["magic_list"][q]][5]
    match spell_list[p["magic_list"][q]][6]:
     case 0:
        if p["torch"] == False:
            p["torchtime"] = 10
            p["torch"] = True
            if spell_list[p["magic_list"][q]][2] <= randint(0, 99): # test the spell -PR-
                return[translate("YOU FAILED TO CAST THE SPELL"), True]
            return[translate("SPARKS FLY AROUND YOU..."), True]
        p["cur_magic"] -= spell_list[p["magic_list"][q]][5] # reverse it -PR-
        return[translate("YOU HAVE LIGHT, YOU CAN'T SPELL MORE"), False]
     case 1:
        if spell_list[p["magic_list"][q]][2] <= randint(0, 99): # test the spell -PR-
            return[translate("YOU FAILED TO CAST THE SPELL"), True]
        mx, my = m["sx"]-2, m["sy"]-2
        q = "#"
        while q[0] not in {".",","," ","]","}",")","$","~","-","*","!","?","<",">","= ","=","% "} or q == "  ":
            x, y = randint(1, mx), randint(1, my)
            q = m["r"][y][x]
        p["x"], p["y"] = x, y
        return[translate("TELEPORTED"), True]
     case 2:
        if 4*p["hp"]+1 > 3*p["maxhp"]:
            p["cur_magic"] -= spell_list[p["magic_list"][q]][5] # reverse it -PR-
            return[translate("YOU CAN'T BE HEALED MORE"), False]
        if spell_list[p["magic_list"][q]][2] <= randint(0, 99): # test the spell -PR-
            return[translate("YOU FAILED TO CAST THE SPELL"), True]
        p["hp"] += 2
        if 4*p["hp"] > 3*p["maxhp"]:
            p["hp"] = (3*p["maxhp"])//4
        return[translate("HEALED"), True]
     case 3:
        if spell_list[p["magic_list"][q]][2] <= randint(0, 99): # test the spell -PR-
            return[translate("YOU FAILED TO CAST THE SPELL"), True]
        for y in range(m["sy"]):
            for x in range(m["sx"]):
                if "%" in m["r"][y][x]:
                    m["v"][y][x] = "%"
        return[translate("DETECTED"), True]
     case 5:
        if spell_list[p["magic_list"][q]][2] <= randint(0, 99): # test the spell -PR-
            return[translate("YOU FAILED TO CAST THE SPELL"), True]
        for y in range(m["sy"]):
            for x in range(m["sx"]):
                if "=" in m["r"][y][x]:
                    m["v"][y][x] = "="
        return[translate("DETECTED"), True]
     case 4:
        if m["r"][p["y"]][p["x"]][0] in {" ", ".", "="}:
            if spell_list[p["magic_list"][q]][2] > randint(0, 99): # ! test the spell -PR-
                m["r"][p["y"]][p["x"]] = "%"
                return[translate("NATURE AROUND YOU"), True]
            return[translate("YOU FAILED TO CAST THE SPELL"), True]
        return[translate("YOU CAN'T CAST THE SPELL HERE!"), False]
     case 6:
        if m["r"][p["y"]][p["x"]][0] in {" ", ".", "%"}:
            if spell_list[p["magic_list"][q]][2] > randint(0, 99): # ! test the spell -PR-
                m["r"][p["y"]][p["x"]] = "="
                return[translate("SHALLOW WATER"), True]
            return[translate("YOU FAILED TO CAST THE SPELL"), True]
        return[translate("YOU CAN'T CAST THE SPELL HERE!"), False]
     case 7: #water jump -PR-
        if spell_list[p["magic_list"][q]][2] <= randint(0, 99): # test the spell -PR-
            return[translate("YOU FAILED TO CAST THE SPELL"), True]
        lista = [] #list -PR-
        for y in range(m["sy"]):
            for x in range(m["sx"]):
                if "=" in m["r"][y][x]:
                    lista.append([y, x])
        if lista == []:
            return[translate("NO WATER ON THIS LEVEL"), False]
        lista = choice(lista) #one element now -PR-
        p["y"], p["x"] = lista[0], lista[1]
        return[translate("TELEPORTED"), True]
     case _: #blast -PR-
        if spell_list[p["magic_list"][q]][2] <= randint(0, 99): # test the spell -PR-
            return[translate("YOU FAILED TO CAST THE SPELL"), True]
        enemies_class_is_blast(m, p, 8)
        return[translate("BLAST!"), True]
