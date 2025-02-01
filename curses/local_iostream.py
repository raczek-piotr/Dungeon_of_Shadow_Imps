# for logfile
from time import time, ctime


def write2log(message): #type → str
    with open("log.txt", "a") as txt:
        txt.write("\n" + ctime(time()) + " " + message + "\n")