def player_move(p):
    match p:
        case "1":
            return [1, -1, True]
        case "2":
            return [1, 0, True]
        case "3":
            return [1, 1, True]
        case "4":
            return [0, -1, True]
        case "5":
            return [0, 0, True]
        case "6":
            return [0, 1, True]
        case "7":
            return [-1, -1, True]
        case "8":
            return [-1, 0, True]
        case "9":
            return [-1, 1, True]
        case "z":
            return [1, -1, True]
        case "x":
            return [1, 0, True]
        case "c":
            return [1, 1, True]
        case "a":
            return [0, -1, True]
        case "s":
            return [0, 0, True]
        case "d":
            return [0, 1, True]
        case "q":
            return [-1, -1, True]
        case "w":
            return [-1, 0, True]
        case "e":
            return [-1, 1, True]
        case _:
            return [0, 0, False]

def get_in(w):
    q = w.getkey()
    match q: # you need it only on windows, maybe… -PR-
        case "PADPLUS":
            q = "+"
        case "PADMINUS":
            q = "-"
        case "PADSTAR":
            q = "*"
        case "PADSLASH":
            q = "/"
    return q
