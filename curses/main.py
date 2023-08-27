import curses as c
from curses import wrapper
from local_output import output
# update
from local_room import test_room
from local_enemies_class import enemies_class_update
# keys
from local_input_key import get_in, player_move
from local_input import keyin
from local_terrain import terrain
# alwayes
from local_scripts import sort


from local_menager import menager
def mainloop(w):
    c.initscr()
    c.noqiflush()
    c.curs_set(0)
    w.resize(24,80)
    c.resize_term(24,80)
    m, p, path = menager(w, c) # from there are imported maps and other things :) -PR-
    hpcounter, manacounter, foodcounter = 0, 0, 0
    test_room(m, [p["y"], p["x"]])

    while p["hp"] > 0:
        sort(p)
        c.flushinp() # I want no flush -PR-
        w.clear()
        output(w, c, m, p)
        w.addstr(23, 0, p["echo"]+":")
        w.refresh()
        p["wasattackby"] = ""
        gi = get_in(w)
        p["dy"], p["dx"], t1 = player_move(gi)
        if t1:
            move, p["echo"], p["moved"] = terrain(w, c, m, p, [p["dy"] + p["y"], p["dx"] + p["x"]], (p["dy"] == 0 and p["dx"] == 0))
            if move:
                p["y"], p["x"] = p["dy"] + p["y"], p["dx"] + p["x"]
        else:
            p["echo"], p["moved"] = keyin(w, c, m, p, [p["y"], p["x"]], gi)
        if p["echo"][:1] == "#": # it should't be "", but ... -PR-
            menager(w, c, p["echo"], m, p) # next map? -PR-

        test_room(m, [p["y"], p["x"]])

        if p["moved"]:
            p["time"] += 1  # for the player, not for me (not now) -PR-
            if p["torch"]:
                p["torchtime"] -= p["normal_level"] #on Boss_levels player do not need to eat and... -PR-
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
                p["needxp"] += 30 + 15*p["lw"]
                p["lw"] += 1
                p["maxhp"] += p["hpchange"]
                p["hp"] += p["hpchange"]
            p["wasattackby"] = ""

            enemies_class_update(m, p, [p["y"], p["x"]])

            hpcounter += 1
            if hpcounter > p["hpcounter"]:
                hpcounter -= p["hpcounter"]
                if p["starving"]:
                    p["hp"] -= 1
                    c.beep() # alarm the player of loosing hit points -PR-
                else:
                    p["hp"] += 1
            if p["hp"] > p["maxhp"]:
                p["hp"] = p["maxhp"]
            if p["hp"] <= 0:
                break
    menager(w, c, "#E", m, p) #End game -PR-
    w.clear()
    output(w, c, m, p)#translator
    w.addstr(23, 0, p["echo"]+"...")
    w.addstr(23, 56, "score: "+str(p["xp"]+(p["attack"]*(p["attack_damage"]+1)*p["attack_acc"]*p["attack_hits"])//5+(p["bow"]*(p["bow_damage"]+1)*p["bow_acc"]*p["bow_hits"])//10+10*(p["lw"]+p["depth"])-74), c.color_pair(4))
    w.getkey()

wrapper(mainloop)