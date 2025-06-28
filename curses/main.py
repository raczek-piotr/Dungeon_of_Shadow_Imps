# Author           : Piotr Raczek
# Created On       : several months before 05.12.2022
# Last Modified By : Piotr Raczek
# Last Modified On : 1.06.2025
#
# Product          : Dungeon of Shadow Imps
# Version          : 1.0
#
# Description      : Classic ascii rogue game played in console
#
# Licensed under GPL
# (see /usr/share/common-licenses/GPL for more details
# or see license.txt [should be next to main.py]
# or contact # the Free Software Foundation for a copy)


import curses as c
from curses import wrapper
from local_manager import manager
from local_output import output
# update
from local_room import test_room
from local_enemies_class import enemies_class_update
from local_event import check_events
# keys
from local_input_key import get_in, player_move
from local_input import keyin
from local_terrain import terrain
# alwayes
from local_scripts import sort
from local_iostream import write2log, write2log_newline
# used in advancing
from local_equip import get_equip_values
# quit and log
from local_game_exit import check_exit
from consts import version

# my command for making exe file for windows -PR-
#C:\Users\piotr\Documents\Thonny\python.exe -OO -m PyInstaller --onefile C:\Users\piotr\Desktop\Dungeon_of_Shadow_Imps-main\curses\main.py -c --ico logo.ico --optimize 2

def mainloop(w):
    c.start_color()
    c.use_default_colors()
    c.initscr()
    c.noqiflush()
    c.curs_set(0) # no visible cursor
    w.resize(24,80)
    c.resize_term(24,80)
    write2log("initialing curses... Done")
    write2log("loading stuff...")
    m, p, path = manager(w, c) # from there are imported maps and player :) -PR-
    reg_time, manacounter, foodcounter = 0, 0, 0
    test_room(m, [p["y"], p["x"]])
    write2log("run main game loop")

    while p["hp"] > 0:
        sort(p)
        c.flushinp() # flush the input -PR-
        w.clear()
        output(w, c, m, p)
        w.addstr(23, 0, p["echo"]+":", c.color_pair(1))
        w.refresh()
        p["wasattackby"] = ""
        gi = get_in(w)
        check_exit(gi)
        check_events(w, c, m, p, m["r"][p["y"]][p["x"]])
        p["dy"], p["dx"], t1 = player_move(gi)
        if t1:
            move, p["echo"], p["moved"] = terrain(w, c, m, p, [p["dy"] + p["y"], p["dx"] + p["x"]], (p["dy"] == 0 and p["dx"] == 0))
            if move:
                p["y"], p["x"] = p["dy"] + p["y"], p["dx"] + p["x"]
        else:
            p["echo"], p["moved"] = keyin(w, c, m, p, [p["y"], p["x"]], gi)
        if p["echo"][:1] == "#": # it could be "" … -PR-
            manager(w, c, p["echo"], m, p) # next map? -PR-
            if p["echo"] == "#":
                return # close the game -PR-

        if p["torch"]:
            test_room(m, [p["y"], p["x"]])

        if p["moved"]:
            p["time"] += 1  # for the player, not for me (not now) -PR-
            if p["torch"]:
                p["torchtime"] -= p["normal_level"] #on „idle levels” player do not need to eat and... -PR-
                if p["torchtime"] < 0:
                    p["torch"] = False
            if not p["starving"]:
                p["fullness"] -= p["normal_level"]
                if p["fullness"] < 1:
                    p["starving"] = True
                    c.beep() # alarm the player -PR-
            if p["fury"]:
                p["fury"] -= 1
            if p["blessing"]:
                p["blessing"] -= 1
            while p["xp"] >= p["needxp"]:
                p["lw"] += 1
                p["maxhp"] += p["hpchange"]
                p["hp"] += p["hpchange"]
                if p["lw"] >= 10 * p["skill"]:
                    p["skill"] += 1
                    p["strength"] += 1
                    p["dexterity"] += 1
                    if p["inteligence"] > 0:
                        p["inteligence"] += 1
                p["xpchange"] = int((p["xpchange"]*1.06+3)//1)
                p["needxp"] += p["xpchange"]
                get_equip_values(p)
            p["wasattackby"] = ""

            enemies_class_update(m, p, [p["y"], p["x"]])

            reg_time += 1
            if reg_time > p["reg_time"]:
                reg_time -= p["reg_time"]
                if p["starving"]:
                    p["hp"] -= 1
                    c.beep() # alarm the player of loosing hit points -PR-
                else:
                    p["hp"] += p["maxhp"]//p["reg_1/"]
            if p["hp"] > p["maxhp"]:
                p["hp"] = p["maxhp"]
            if p["hp"] <= 0:
                write2log("player dies")
                manager(w, c, "#E", m, p) #End game -PR-
                break
    write2log("exit main game loop")

write2log_newline()
write2log("starting game " + version)
write2log("initialing curses...")
wrapper(mainloop)
write2log("game ends (terminates) " + version)
