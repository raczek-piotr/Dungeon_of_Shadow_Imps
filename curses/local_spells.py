from local_output import output
from local_input_key import *
from local_enemies_class import enemies_class_is_cast, enemies_class_is_blast
from local_translator import translate

from random import randint, choice

F = 0
spell_list = [
# name,						2% 6=,chance,inteligence_needed,id
# spellbook (PALLADIN 9~12)
[translate("LAMPYRIDAE"),        1, 60, 9,  0], #0
[translate("DETECT STAIRS"),     1, 60, 9,  1], #1
[translate("READY STRIKE"),      1, 60, 10, 2], #2
# druid spells (DRUID 10~13)
[translate("DEDECT NATURE"),     1, 60, 10, 3], #3
[translate("HERBALIZM"),         2, 60, 10, 4], #4
[translate("WORDS OF NATURE"),   1, 60, 11, 5], #5
[translate("NATURE WITH ME"),    2, 60, 12, 6], #6
# water language (WATER MAGE 12~15)
[translate("DETECT WATER"),      1, 60, 12, 7], #7
[translate("WATER JUMP"),        1, 60, 12, 8], #8
[translate("CONDENCE HUMID"),    1, 60, 13, 9], #9
[translate("HYDROGEN BLAST"),    6, 60, 14, 10],#10
]
# fire conpendium (WIZARD 12~15)
fire_compendium = lambda p, option: (2 + int(p["lw"]**1.1) // 3 if p["ismage"] else 1 + int(p["lw"]**1.1) // 6) if option == 1 else 95 if option == 2 else 1
'''def staff_of_fire(p, option):
    match option:
        case 1:
            if p["ismage"]:
                return 2 + int(p["lw"]**1.1) // 3
            return 1 + int(p["lw"]**1.1) // 6
        case 2:
            return 95
        case _:
            return 1'''

def spell_menager(w, c, m, p):
    q = "-1" # not in slots -PR-
    slots = set()
    colors = list()
    for i in range(len(p["magic_list"])):
        q = m["r"][p["y"]][p["x"]][0]
        ml = spell_list[p["magic_list"][i]]
        if ml[3] <= p["inteligence"]:
            if (ml[1] == 1 or (ml[1] == 2 and q == "%") or (ml[1] == 6 and q == "=")):
                slots.add(str(i+1))
                colors.append(1)
            else:
                colors.append(ml[1])
        else:
            colors.append(5) # color grey
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

    chance = spell_list[p["magic_list"][q]][2]
    if spell_list[p["magic_list"][q]][3] < p["inteligence"]:
        chance = 95
    match spell_list[p["magic_list"][q]][4]:

     case 0: #LAMPYRIDAE
        if m["r"][p["y"]][p["x"]][0] in {" ", ",", "%", "="}:
            if chance > randint(0, 99): # ! test the spell -PR-
                m["r"][p["y"]][p["x"]] = "."
                return[translate("LAMPYRIDAE"), True]
            return[translate("YOU FAILED TO CAST THE SPELL"), True]
        return[translate("YOU CAN'T CAST THE SPELL HERE!"), False]
     case 1: #DEDECT STAIRS
        if chance <= randint(0, 99): # test the spell -PR-
            return[translate("YOU FAILED TO CAST THE SPELL"), True]
        lista = [] #list -PR-
        for y in range(m["sy"]): # O(n²) PR
            for x in range(m["sx"]):
                if m["r"][y][x][0] == "<" and m["v"][y][x][0] == " ":
                    lista.append([y, x])
                elif m["r"][y][x][0] == ">" and m["v"][y][x][0] == " ":
                    lista.append([y, x])
        if lista == []:
            return[translate("THERE ARE NO MORE UNCOVERED STAIRS TILES ON THIS LEVEL"), False]
        lista = choice(lista) # one element now -PR-
        m["v"][lista[0]][lista[1]] = m["r"][lista[0]][lista[1]][0]
        return[translate("DETECTED"), True]
     case 2: #READY STRIKE
        if p["blessing"] == 0 and p["fury"] == 0 and p["hp"] == p["maxhp"]:
            if chance > randint(0, 99): # ! test the spell -PR-
                p["blessing"] = 2
                p["fury"] = 2
                return[translate("READY"), True]
            return[translate("YOU FAILED TO CAST THE SPELL"), True]
        return[translate("YOU ARE TOO LOW HP OR YOU HAVE SOME BUFFS (F,B)"), False]
     case 3: #DEDECT NATURE
        if chance <= randint(0, 99): # test the spell -PR-
            return[translate("YOU FAILED TO CAST THE SPELL"), True]
        lista = [] #list -PR-
        for y in range(m["sy"]): # O(n²) PR
            for x in range(m["sx"]):
                if m["r"][y][x][0] == "%" and m["v"][y][x][0] == " ":
                    lista.append([y, x])
        if lista == []:
            return[translate("THERE ARE NO MORE UNCOVERED NATURE TILES ON THIS LEVEL"), False]
        lista = choice(lista) # one element now -PR-
        m["v"][lista[0]][lista[1]] = m["r"][lista[0]][lista[1]][0]
        return[translate("DETECTED"), True]
     case 4: #HERBALIZM
        if p["hp"] == p["maxhp"]:
            return[translate("YOU CAN'T BE HEALED MORE"), False]
        if p["fullness"] < 100:
            return[translate("EAT MORE FOOD"), False]
        if chance <= randint(0, 99): # test the spell -PR-
            return[translate("YOU FAILED TO CAST THE SPELL"), True]
        p["hp"] += p["maxhp"] // 5
        p["fullness"] -= 80
        if p["hp"] > p["maxhp"]:
            p["hp"] = p["maxhp"]
        return[translate("HEALED"), True]
     case 5: #WORDS OF NATURE
        if m["r"][p["y"]][p["x"]][0] in {" ", ".", ",", "="}:
            if chance > randint(0, 99): # ! test the spell -PR-
                m["r"][p["y"]][p["x"]] = "%"
                return[translate("NATURE AROUND YOU"), True]
            return[translate("YOU FAILED TO CAST THE SPELL"), True]
        return[translate("YOU CAN'T CAST THE SPELL HERE!"), False]
     case 6: #NATURE WITH ME
        if p["blessing"] == 0 and 2*p["hp"] <= p["maxhp"]:
            if chance > randint(0, 99): # ! test the spell -PR-
                p["blessing"] = 21
                return[translate("BLESSED"), True]
            return[translate("YOU FAILED TO CAST THE SPELL"), True]
        return[translate("BLESSED OR NOT LOW HP"), False]
     case 7: #DETECT WATER
        if chance <= randint(0, 99): # test the spell -PR-
            return[translate("YOU FAILED TO CAST THE SPELL"), True]
        lista = [] #list -PR-
        for y in range(m["sy"]): # O(n²) PR
            for x in range(m["sx"]):
                if m["r"][y][x][0] == "=" and m["v"][y][x][0] == " ":
                    lista.append([y, x])
        if lista == []:
            return[translate("THERE ARE NO MORE UNCOVERED WATER TILES ON THIS LEVEL"), False]
        lista = choice(lista) # one element now -PR-
        m["v"][lista[0]][lista[1]] = m["r"][lista[0]][lista[1]][0]
        return[translate("DETECTED"), True]
     case 8: #WATER JUMP -PR-
        if chance <= randint(0, 99): # test the spell -PR-
            return[translate("YOU FAILED TO CAST THE SPELL"), True]
        lista = [] #list -PR-
        for y in range(m["sy"]): # O(n²) PR
            for x in range(m["sx"]):
                if m["v"][y][x][0] == "=":
                    lista.append([y, x])
        if lista == []:
            return[translate("THERE ARE NO EMPTY WATER TILES SEEN ON THIS LEVEL"), False]
        lista = choice(lista) # one element now -PR-
        p["y"], p["x"] = lista[0], lista[1]
        return[translate("WATERJUMPED"), True]
     case 9: #CONDENCE HUMID -PR-
        if m["r"][p["y"]][p["x"]][0] in {" ", ".", ",", "%"}:
            if chance > randint(0, 99): # ! test the spell -PR-
                m["r"][p["y"]][p["x"]] = "="
                return[translate("SHALLOW WATER"), True]
            return[translate("YOU FAILED TO CAST THE SPELL"), True]
        return[translate("YOU CAN'T CAST THE SPELL HERE!"), False]
     case _: #HYDROGEN BLAST -PR-
        if chance <= randint(0, 99): # test the spell -PR-
            return[translate("YOU FAILED TO CAST THE SPELL"), True]
        enemies_class_is_blast(m, p, 8)
        if p["inteligence"] >= 15 and randint(0, 100) < 40:
            enemies_class_is_blast(m, p, 8)
            return [translate("HYDROGEN BLAST DETONATED! CHAIN REACTION! DOUBLE DAMAGE!"), True]
        return[translate("HYDROGEN BLAST DETONATED!"), True]