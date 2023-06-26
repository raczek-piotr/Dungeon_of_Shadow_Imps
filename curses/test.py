import curses as c
from curses import wrapper
from local_input_key import get_in
def mainloop(w):
    c.initscr()
    c.noqiflush()
    c.curs_set(0)
    w.resize(24,80)
    c.resize_term(24,80)
    w.addstr(0, 0, "?")
    w.refresh()
    ga = "?"

    while True:
        gi = get_in(w)
        w.clear()
        w.addstr(0, 0, gi+":"+str(gi == ga))
        ga = gi
        w.refresh()

wrapper(mainloop) # MY curses IS working on linux :) -PR-
