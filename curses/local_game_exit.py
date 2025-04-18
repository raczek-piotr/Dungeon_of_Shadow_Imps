from local_iostream import write2log


def game_exit():
    write2log("game_exit()")
    exit()

def check_exit(char):
    if char == "q":
        game_exit()