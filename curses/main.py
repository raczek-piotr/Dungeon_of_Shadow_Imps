#import curses as c
from curses import wrapper
from local_output import output
# update
from local_room import test_room
from local_enemies_class import enemies_class_update
# keys
from local_input_key import get_in, player_move
from local_input import keyin
from local_terrain import terrain
# from takein import takein


from local_menager import menager
def mainloop(w):
    m, p, path = menager()
    hpcounter, manacounter, foodcounter = 0, 0, 0
    test_room(m, [p["y"], p["x"]])

    while p["hp"] > 0:
        w.clear()
        output(w, m, p)
        w.addstr(23, 0, p["echo"]+":") # curses worked normally on linux -PR-
        w.refresh()
        p["wasattackby"] = ""
        gi = get_in(w)
        p["dy"], p["dx"], t1 = player_move(gi)
        if t1:
            move, p["echo"], p["moved"] = terrain(m, p, [p["dy"] + p["y"], p["dx"] + p["x"]], (True if p["dy"] == 0 and p["dx"] == 0 else False))
            if move:
                p["y"], p["x"] = p["dy"] + p["y"], p["dx"] + p["x"]
        else:
            p["echo"], p["moved"] = keyin(w, m, p, [p["y"], p["x"]], gi)
        if p["echo"][:1] == "#": # it could be "" -PR-
            menager(p["echo"], m, p)
        test_room(m, [p["y"], p["x"]])
        # if t1:
        # else:
        #
        if p["moved"]:
            p["time"] += 1  # for the player, not for me (not now) -PR-
            if p["torch"]:
                p["torchtime"] -= p["normal_level"] #on Boss_levels player do not need to eat and... -PR-
                if p["torchtime"] < 0:
                    p["torch"] = False
            if not p["starving"]:
                p["fullness"] -= p["normal_level"]
                if p["fullness"] < 0:
                    p["starving"] = True
            while p["xp"] >= p["needxp"]:
                p["needxp"] += 20 + 5*p["lw"] #(p["lw"] + 4) * (p["lw"] + 5) * (2 * p["lw"] + 9) // 15 - 3 # sum of 2*((x+4)**2)//5 -PR-
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
                else:
                    p["hp"] += 1
            if p["hp"] > p["maxhp"]:
                p["hp"] = p["maxhp"]
            if p["hp"] <= 0:
                break
    while True: # die - PR
        menager("#E", m, p)
        w.clear()
        output(w, m, p)#translator
        w.addstr(23, 0, p["echo"]+"    "+("SCORE")+": "+str(5*(2*p["lw"]+p["attack"]+p["bow"]+p["armor"])+p["depth"]+p["xp"]-25))
        w.getkey()

wrapper(mainloop) # MY curses IS working on linux :) -PR-
