# for logfile
from time import time, ctime


def write2log(message): #type → str
    with open("log.txt", "a") as txt:
        txt.write(ctime(time()) + " " + message + "\n")

def write2log_newline():
    with open("log.txt", "a") as txt:
        txt.write("\n")