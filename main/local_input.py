from random import randint

from local_translator import translate
from local_output import item


def item_menager(m, p):
    t1 = "\n\n\n\n\n\n\n\n\n\n\n\n\n       Equipted:\n   " + item(p["attack"], 9, p["strength"]) + "\n   " + item(p["hand"], 9, p["strength"]) + "\n   " + item(p["armor"], 9, p["strength"]) + "\n\n       Backpack:\n"
    for i in range(6):
        t1 += str(i+1)+": "+item(p["BP"], i, p["strength"]) + "\n"
    print(t1, end="\nWhat do you want to do?:")
    input()
    return["", True]

# def item_menager_keyin(m, p,key):

def keyin(m, p, pos, key):
    match key:
        case "-":
             return item_menager(m, p)
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
