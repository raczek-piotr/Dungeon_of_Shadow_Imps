from consts import path

from time import time, ctime
import ast
from os import remove


# logfile
def write2log(message): #type → str
    with open(path + "log.txt", "a") as txt:
        txt.write(ctime(time()) + " " + message + "\n")

def write2log_newline():
    with open(path + "log.txt", "a") as txt:
        txt.write("\n")

# game saving/loading part1 — trades
def trades_save(t):
    with open(path + "save.txt", "a") as txt: #"ba"
        txt.write("\n")
        txt.write(str(t)) #.encode(encoding="utf-8")
    return
def trades_load():
    with open(path + "save.txt", "r") as txt:
        ret = txt.read().split("\n")[1]
    return ast.literal_eval(ret)
from local_npc import trades_do_save, trades_do_load

# game saving/loading part2 — events
def events_save(A, B):
    with open(path + "save.txt", "a") as txt: #"ba"
        txt.write("\n")
        txt.write(str(A)) #.encode(encoding="utf-8")
        txt.write("\n")
        txt.write(str(B)) #.encode(encoding="utf-8")
    return
def events_load():
    with open(path + "save.txt", "r") as txt:
        try:
            txt = txt.read().split("\n")
            ret = (ast.literal_eval(txt[2]), ast.literal_eval(txt[3]))
        except:
            return False
    return ret
from local_event import events_do_save, events_do_load

# game saving/loading part3 — player
def savegame(p):
    try:
        with open(path + "save.txt", "w") as txt: #"bw"
            txt.write(str(p)) #.encode(encoding="utf-8")
        trades_do_save()
        events_do_save()
        return True
    except:
        return False

def loadgame():
    try: # reverse order PR
        events_do_load()
        trades_do_load()
        with open(path + "save.txt", "r") as txt:
            ret = txt.read().split("\n")[0]
        p = ast.literal_eval(ret)
        return p
    except:
        return []

# romove game saving
def clearsave():
    try:
        remove(path + "save.txt")
    except:
        pass
    return
