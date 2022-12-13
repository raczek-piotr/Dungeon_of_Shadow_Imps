# import curses as c
# from curses import wrapper
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
m, p, path = menager()
hpcounter, manacounter = 0, 0
test_room(m, [p["y"], p["x"]])

while p["hp"] > 0:
    print(output(m, p) + p["echo"]+":")
    p["wasattackby"] = ""
    gi = get_in()
    p["dy"], p["dx"], t1 = player_move(gi)
    if t1:
        move, p["echo"], p["moved"] = terrain(m, p, [p["dy"] + p["y"], p["dx"] + p["x"]], (True if p["dy"] == 0 and p["dx"] == 0 else False))
        if move:
            p["y"], p["x"] = p["dy"] + p["y"], p["dx"] + p["x"]
    else:
        p["echo"], p["moved"] = keyin(m, p, [p["y"], p["x"]], gi)
        if p["echo"][:1] == "#": # it could be "" -PR-
            menager(p["echo"], m, p)
    test_room(m, [p["y"], p["x"]])
    # if t1:
    # else:
    #
    if p["moved"]:
        p["time"] += 1  # for the player, not for me (not now) -PR-
        if p["torch"]:
            p["torchtime"] -= 1
            if p["torchtime"] < 0:
                p["torch"] = False
        while p["xp"] >= p["needxp"]:
            p["lw"] += 1
            p["needxp"] = (p["lw"] + 4) * (p["lw"] + 5) * (2 * p["lw"] + 9) // 30 - 6 # sum of ((x+4)**2)//5 -PR-
            p["maxhp"] += p["hpchange"]
            p["hp"] += p["hpchange"]
        p["wasattackby"] = ""
        if p["mana"] == p["maxmana"]:
            manacounter = 0
        else:
            manacounter += 1
            if manacounter > p["manacounter"]:
                manacounter -= p["manacounter"]
                p["mana"] += 1

        enemies_class_update(m, p, [p["y"], p["x"]])

        if p["hp"] == p["maxhp"]:
            hpcounter = 0
        else:
            hpcounter += 1
            if hpcounter > p["hpcounter"]:
                hpcounter -= p["hpcounter"]
                p["hp"] += 1
        if p["hp"] > p["maxhp"]:
            p["hp"] = p["maxhp"]
        if p["hp"] <= 0:
            break
menager("#E", m, p)
input(output(m, p) + p["echo"]+"\n"+"wynik")
# die - PR
    # c.init_pair(0, c.COLOR_BLUE, c.COLOR_BLACK)
    # s.clear()
    # s.addstr(1,1,"gh",c.color_pair(0))
# wrapper(mainloop) # MY curses is not working (but on linux curses is working) :( -PR-
