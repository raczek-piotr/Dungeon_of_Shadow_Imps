from random import randint

from local_output import output, item

from local_translator import translate
from local_input_key import *
from local_enemies_class import enemies_class_is_shoted
from local_equip import get_equip_values


def item_menager(m, p):
    t1 = "\n\n\n\n\n\n\n\n\n\n\n\n\n       Equipted:\n   " + item(p["e_attack"], 9, p["strength"]) + "\n   " + item(p["e_hand"], 9, p["strength"]) + "\n   " + item(p["e_armor"], 9, p["strength"]) + "\n\n       Backpack:\n"
    for i in range(6):
        t1 += str(i+1)+": "+item(p["BP"], i, p["strength"]) + "\n"
    print(t1, end="\nWhat do you want to do?:")
    input()
    return["", True]

def shot_menager(m, p):
    print(output(m, p) + translate("WHERE DO YOU WANT TO SHOT?"))
    gi = get_in()
    dy, dx, t1 = player_move(gi)
    if (dy != 0 or dx != 0) and p["arrows_id"] != -1:
        enemies_class_is_shoted(m, p, [dy, dx], p["bow"])
        get_equip_values(p)
        return[p["echo"], True]
    if p["arrows_id"] == -1:
        return[translate("YOU DON'T HAVE ARROWS!"), False]
    return[translate("YOU CAN'T SHOT THERE!"), False]

# def item_menager_keyin(m, p,key):

def keyin(m, p, pos, key):
    match key:
        case "-":
             return item_menager(m, p)
        case "0":
             return shot_menager(m, p)
        # case "-":
        #     return f_arrows(rmap, vmap, p, np, gold, baner, backpack, direction)
        # # case "!":
        # #     return f_orantium(rmap, vmap, p, np, gold, baner, backpack, direction)
        # case "+":
        #     return f_door(rmap, vmap, p, np, gold, baner, backpack, direction)
        # case "]":
        #     return f_weapon(rmap, vmap, p, np, gold, baner, backpack, direction)
        # case "}":
        #     return f_putter(rmap, vmap, p, np, gold, baner, backpack, direction)
        # case ")":
        #     return f_armor(rmap, vmap, p, np, gold, baner, backpack, direction)
        # case "~":
        #     return f_torch(rmap, vmap, p, np, gold, baner, backpack, direction)
        # case "?":
        #     return f_potion(rmap, vmap, p, np, gold, baner, backpack, direction)
        # case "=":
        #     return [p, gold, translate("THIS TILE IS CLOSE"), 0]
        # case ".":
        #     return [np, gold, "", 1]
        # case ",":
        #     return [np, gold, "", 1]
        # case " ":
        #     return [np, gold, "", 1]
        # case "#":
        #     return [p, gold, translate("HERE IS A WALL"), 0]
        case ">":
            if m["r"][pos[0]][pos[1]][0] == ">":
                return ["#D", False]
            return [translate("YOU CAN'T GO DOWN HERE"), False]
        case "<":
            if m["r"][pos[0]][pos[1]][0] == "<":
                return ["#U", False]
            return [translate("YOU CAN'T GO UP HERE"), False]
        case _:
           # move a player? (but in where!?),
           #		echo, moved?
            return ["? - for help", False]
