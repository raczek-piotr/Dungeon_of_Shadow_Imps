from local_output import output
from local_input_key import *
from local_enemies_class import enemies_class_is_cast
from local_translator import translate

from random import randint


spell_list = [
# name,						 2%-6=,chance,2D_value,inteligence_needed, flag_if_value_is_False
[translate("SPARKING BALL"), 2,    70,    2,       1],   #0
[translate("MAGIC LIGHT"),   1,    100,   False,   2, 0],#1
[translate("DRUID'S SHOT"),  2,    70,    4,       3],   #2
[translate("WATER STORM"),   6,    60,    16,      4],   #3
[translate("HEALING 2HP"),   6,    20,    False,   5, 2],#4
[translate("TELEPORTATION"), 1,    40,    False,   4, 1],#5
[translate("MAGIC MISSLE"),  1,    60,    5,       6],   #6
[translate("HEALING 4HP"),   2,    20,    False,   7, 4],#7
[translate("FIRE BALL"),     1,    70,    8,       8],   #8
[translate("HYDROGEN BLAST"),6,    80,    30,      9],   #9
]

def spell_menager(w, c, m, p):
    q = "-1" # not in slots -PR-
    slots = set()
    colors = list()
    for i in range(len(p["magic_list"])):
        q = m["r"][p["y"]][p["x"]][0]
        ml = spell_list[p["magic_list"][i]]
        if ml[4] <= p["inteligence"] and (ml[1] == 1 or (ml[1] == 2 and q == "%") or (ml[1] == 6 and q == "=")):
            slots.add(str(i+1))
            colors.append(ml[1])
        else:
            colors.append(0)
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
        w.addstr(23, 0, translate("CHOOSE A SPELL TO CAST"), c.color_pair(1))
        q = get_in(w)
    q = int(q)-1
    if spell_list[p["magic_list"][q]][2] <= randint(0, 99):
        return[translate("YOU FAILED TO CAST THE SPELL"), True]
    if spell_list[p["magic_list"][q]][3]:
        w.clear()
        output(w, c, m, p)
        w.addstr(23, 0, translate("IN WHAT DIRECTION DO YOU WANT TO CAST THE SPELL?"), c.color_pair(1))
        it = get_in(w)
        dy, dx, t1 = player_move(it)
        if t1 and it != "5":
            enemies_class_is_cast(m, p, [dy, dx], spell_list[p["magic_list"][q]][3], spell_list[p["magic_list"][q]][2])
            return[p["echo"], True]
        return[translate("WRONG DIRECTION!"), False]
    #else:
    if spell_list[p["magic_list"][q]][5] == 0:
        if p["torch"] == False:
            p["torchtime"] = 10
            p["torch"] = True
            return[translate("SPARKS FLY AROUND YOU..."), True]
        return[translate("YOU HAVE A LIGHT, CAN'T SPELL"), False] # 0% to fail the spell -PR-
    elif spell_list[p["magic_list"][q]][5] == 1:
        mx, my = m["sx"]-2, m["sy"]-2
        q = "#"
        while q[0] not in {".",","," ","]","}",")","$","~","-","*","!","?","<",">","= ","=","% "} or q == "  ":
            x, y = randint(1, mx), randint(1, my)
            q = m["r"][y][x]
        p["x"], p["y"] = x, y
        return[translate("TELEPORTED"), True]
    else:
        if p["hp"] == p["maxhp"]:
            return[translate("YOU CAN'T BE HEALED MORE"), False]
        p["hp"] += spell_list[p["magic_list"][q]][5]
        if p["hp"] > p["maxhp"]:
            p["hp"] = p["maxhp"]
            return[translate("HEALED"), True]