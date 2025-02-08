from time import time, ctime
import ast
from os import remove


# logfile
def write2log(message): #type → str
    with open("log.txt", "a") as txt:
        txt.write(ctime(time()) + " " + message + "\n")

def write2log_newline():
    with open("log.txt", "a") as txt:
        txt.write("\n")

# game saving/loading part1
def trades_save(t):
    with open("save.txt", "a") as txt: #"ba"
        txt.write("\n")
        txt.write(str(t)) #.encode(encoding="utf-8")
    return
def trades_load():
    with open("save.txt", "r") as txt:
        ret = txt.read().split("\n")[1]
    return ast.literal_eval(ret)

# game saving/loading part2
from local_npc import trades_do_save, trades_do_load
def savegame(p):
    try:
        with open("save.txt", "w") as txt: #"bw"
            txt.write(str(p)) #.encode(encoding="utf-8")
        trades_do_save()
        return True
    except:
        return False

def loadgame():
    try:
        with open("save.txt", "r") as txt:
            ret = txt.read().split("\n")[0]
        p = ast.literal_eval(ret)
        trades_do_load()
        return p
    except:
        return []

# romove game saving
def clearsave():
    try:
        remove("save.txt")
    except:
        pass
    return
