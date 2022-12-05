enable_windows_stuff = False
try:
    from getch import getch
except:
    from msvcrt import getch
    enable_windows_stuff = True


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
        case _:
            return [0, 0, False]

def get_in():
    global enable_windows_stuff
    if enable_windows_stuff:
        return str(getch())[2]
    return getch()
