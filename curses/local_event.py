from local_output import output
from local_translator import translate
from local_iostream import write2log
# for ending the game
from local_equip import get_equip_values
from local_scores import scoreboard_append, scoreboard_print
from local_iostream import events_save, events_load
from local_game_exit import game_exit

events_done = []

all_events = [
    {"id":    "the book after",
     "filter" : [["ifdone", "the book"], ["ifpos", 2, 6, "."], ["player", "depth", 40]],
     "dialog" : ["~ After two days will he revive us:", "~ on the third day he will raise us up,", "~ and we shall live in his sight.", "~ ‪Hosea 6:2"],
     "changes": [["gameend", "win"]],
     "once" : True,
    },
    {"id":    "the book",
     "filter" : [["ground", "?066."], ["player", "depth", 40]],
     "dialog" : ["- YES, IT IS ONE COPY OF BOOK OF BOOKS", "- WHAT? SO WHY IT IS SPECIAL? SHOULDN'T IT BE IN ONE COPY?", "- YOU SEE, IF YOU HAVE GOOD NEWS, THEY ARE NOT 'IN ONE COPY'", "- HMM... SO WHAT ARE THE GOOD NEWS?", "- BUT AT FIRST THE BAD NEWS", "- SO WHAT ARE THE BAD NEWS?", "- BAD NEW SAID THAT WE ARE ALL BAD, SO WE SHALL DIE", "- BUT MY FATHER WAS A FINE MAN!", "- HE WAS, BUT HE WASN'T PERFECT; LIKE ALL PEOPLE", "- I SEE, I'M NOT PERFECT TOO...", "- YOU ARE RIGHT, BUT THEN ARE GOOD NEWS COMMING", "- SO, WHAT ARE THE GOOD NEW?", "- THE GOOD NEWS ARE wonderful MESSAGE FROM GOD", "- SO, WHAT IS THE MESSAGE?", "- JUST READ IT, I HAVE TO GO", "- WAIT, WHO ARE YOU?", "- SHARE THE GOOD NEWS! THE SHERIF IS STILL WAITING FOR THEM!"],
     "changes": [["setpos", 2, 7, "."]],
     "once" : True,
    },
    {"id":    "enable alt",
     "filter" : [["player", "depth", 30]],
     "dialog" : [],
     "changes" : [["player", "alt", True]],
     "once" : True,
    },
]

def events_do_save():
    global all_events, events_done
    return events_save(all_events, events_done)
def events_do_load():
    global all_events, events_done
    AB = events_load()
    if AB:
        all_events, events_done = AB


def check_events(w, c, m, p, ground):
    global all_events, events_done
    for i in range(len(all_events)-1, -1, -1):
        event = all_events[i]
        for filtr in event["filter"]:
            if filtr[0] == "ground":
                if filtr[1] != ground:
                    break
            elif filtr[0] == "ifpos":
                if m["r"][filtr[1]][filtr[2]] != filtr[3]:
                    break
            elif filtr[0] == "player":
                if p[filtr[1]] != filtr[2]:
                    break
            elif filtr[0] == "ifdone":
                if filtr[1] not in events_done:
                    break
            
        else: # do it -PR-
            write2log("event start, id: " + event["id"])
            for dialog in event["dialog"]:
                w.clear()
                output(w, c, m, p)
                w.addstr(23, 0, translate(dialog), c.color_pair(1))
                w.refresh()
                w.getkey()
            for change in event["changes"]:
                if change[0] == "setpos":
                    m["r"][change[1]][change[2]] = change[3]
                elif change[0] == "player":
                    p[change[1]] = change[2]
                elif change[0] == "gameend":
                    write2log("player wins")
                    clearsave()
                    get_equip_values(p)
                    score = scoreboard_append(w, c, p, True)
                    write2log("player ends his game with score: "+str(score))
                    w.clear()
                    output(w, c, m, p)
                    w.addstr(23, 0, translate("YOU WIN! THANKS FOR PLAYING!"))
                    w.addstr(23, 56, "score: "+str(score), c.color_pair(2))
                    w.getkey()
                    game_exit()
                    change[1]
            if event["once"]: # and check poping it -PR-
                events_done.append(all_events.pop(i)["id"])
                
                
    
