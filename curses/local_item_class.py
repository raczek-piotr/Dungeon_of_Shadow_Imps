from random import randint, choice
from local_scripts import zero3


item = [
["-",  [['ROCK', 'ROCKS'], '-', 1, True, 1]],  #0
["-",  [['ARROW', 'ARROWS'], '-', 1, True, 2]],  #1
["-",  [['BOLT', 'BOLTS'], '-', 1, True, 2]],  #2
["*",  [['RATION OF FOOD', 0, 1000], '*', 1, True, 6]],  #3
["*",  [['BREAD', 0, 600], '*', 1, True, 3]],  #4
["*",  [['FISH', 0, 400], '*', 1, True, 2]],  #5
["*",  [['MOLD', 0, 200], '*', 1, True, 1]],  #6
["~",  [['OILED TORCH', 1, 1400], '~', 1, True, 10]],  #7
["~",  [['TORCH', 1, 800], '~', 1, True, 5]],  #8
["?",  [['SCROLL', 2, 1], '?', 1, False, 100]],  #9
 # changed from identyfication to teleport -PR-
["?",  [['SCROLL', 2, 1], '?', 1, False, 100]],  #10
["?",  [['SCROLL', 2, 2], '?', 1, False, 100]],  #11
["?",  [['SCROLL', 2, 3], '?', 1, False, 5]],  #12
["!",  [['POTION', 3, 0], '!', 1, False, 100]],  #13
["!",  [['POTION', 3, 1], '!', 1, False, 100]],  #14
["!",  [['POTION', 3, 2], '!', 1, False, 100]],  #15
["!",  [['POTION', 3, 3], '!', 1, False, 5]],  #16
[")",  [['T-SHIRT', 'e_armor'], ')', [0, 1], True, 0]],  #17
[")",  [['SOFT LEATHER', 'e_armor'], ')', [1, 16], True, 30]],  #18
[")",  [['HARD LEATHER', 'e_armor'], ')', [2, 21], True, 130]],  #19
[")",  [['LEATHER MAIL', 'e_armor'], ')', [4, 41], True, 520]],  #20
[")",  [['CHAIN MAIL', 'e_armor'], ')', [5, 51], True, 810]],  #21
[")",  [['CHAIN ARMOR', 'e_armor'], ')', [7, 61], True, 1595]],  #22
[")",  [['PLATE ARMOR', 'e_armor'], ')', [8, 71], True, 2080]],  #23
[")",  [['CLOTHES', 'e_shield'], ')', [0, 1], True, 20]],  #24
[")",  [['CLOTHES', 'e_shield'], ')', [0, 1], True, 20]],  #25
[")",  [['CLOTHES', 'e_shield'], ')', [0, 1], True, 20]],  #26
["]",  [['KNIFE', 'e_attack'], ']', [1, 3, 1, 60, 6, 7], True, 120]],  #27
["]",  [['LONG KNIFE', 'e_attack'], ']', [1, 5, 1, 60, 7, 8], True, 270]],  #28
["]",  [['2 KNIFES', 'e_attack'], ']', [1, 3, 2, 60, 8, 9], True, 480]],  #29
["]",  [['DAGGER', 'e_attack'], ']', [2, 4, 1, 60, 9, 10], True, 750]],  #30
["]",  [['LONG DAGGER', 'e_attack'], ']', [2, 6, 1, 60, 10, 12], True, 1470]],  #31
["]",  [['HEAVY DAGGER', 'e_attack'], ']', [2, 9, 1, 60, 11, 13], True, 3000]],  #32
["}",  [['SLING', 'e_hand', 'ROCK'], '}', [1, 1, 1, 60, 6, 7], True, 48]],  #33
["}",  [['SHORT BOW', 'e_hand', 'ARROW'], '}', [1, 5, 1, 60, 7, 11], True, 432]],  #34
["}",  [['BOW', 'e_hand', 'ARROW'], '}', [1, 9, 1, 60, 8, 12], True, 1200]],  #35
["}",  [['COMPOSIVE BOW', 'e_hand', 'ARROW'], '}', [1, 15, 1, 70, 9, 13], True, 4176]],  #36
["}",  [['LONG BOW', 'e_hand', 'ARROW'], '}', [1, 22, 1, 80, 10, 14], True, 11280]],  #37
["}",  [['HAND CROSSBOW', 'e_hand', 'BOLT'], '}', [1, 8, 1, 40, 10, 8], True, 432]],  #38
["}",  [['LIGHT CROSSBOW', 'e_hand', 'BOLT'], '}', [1, 10, 1, 40, 11, 9], True, 640]],  #39
["}",  [['CROSSBOW', 'e_hand', 'BOLT'], '}', [1, 15, 1, 40, 11, 11], True, 1360]],  #40
["}",  [['HAEVY CROSSBOW', 'e_hand', 'BOLT'], '}', [1, 21, 1, 40, 12, 12], True, 2576]],  #41
["}",  [['HAND REPETER', 'e_hand', 'BOLT'], '}', [1, 1, 3, 40, 8, 10], True, 48]],  #42
["}",  [['LIGHT REPETER', 'e_hand', 'BOLT'], '}', [2, 2, 3, 40, 9, 11], True, 432]],  #43
["}",  [['REPETER', 'e_hand', 'BOLT'], '}', [2, 4, 3, 40, 10, 12], True, 1200]],  #44
["}",  [['HAEVY REPETER', 'e_hand', 'BOLT'], '}', [1, 16, 3, 44, 11, 13], True, 4176]],  #45
[")",  [['CLOTHING', 'e_armor'], ')', [0, 0, 0, 0, 6, 6], True, 30]],  #46
[")",  [['SMALL SHIELD', 'e_armor'], ')', [0, 0, 0, 0, 6, 6], True, 80]],  #47
[")",  [['CLOTHING', 'e_armor'], ')', [0, 0, 0, 0, 6, 6], True, 30]],  #48
[")",  [['CLOTHING', 'e_armor'], ')', [0, 0, 0, 0, 6, 6], True, 30]],  #49

]

def item_class_get(it): # in the future, when I will remake the itemlist -PR-
    q = item[it][1].copy()
    if q[1] in {"]",")","}"}:
        q[2] = item[it][1][2].copy()
    elif q[1] in {"?","!"}:
        q[0] = item[it][1][0].copy()
        q[0][0] = q[0][0]+" "+rname()
    return q

def get_item(it):
    q = item[it][1].copy()
    if q[1] in {"]",")","}"}:
        q[2] = item[it][1][2].copy()
    elif q[1] in {"?","!"}:
        q[0] = item[it][1][0].copy()
        q[0][0] = q[0][0]+" "+rname()
    return q

def get_item_more(it):
    q = item[it][1].copy()
    if q[1] in {"]",")","}"}:
        q[2] = item[it][1][2].copy()
    elif q[1] in {"?","!"}:
        q[0] = item[it][1][0].copy()
        q[0][0] = q[0][0]+" "+rname()
    return q

def disable_disabled_weapons(s, d):
    global item
    #for i in range(len(item)):
    #    if item[i][0] in {"]","}"}:
    #        t = item[i][1][2][2]
    #        if t[0] > s+3 or t[1] > d+3:
    #            item[i] = item[(i%4+5)]

def randitem(hm): # how many -PR-
    global item
    i, q = len(item)-1, []
    for _ in range(hm):
        r = randint(0, i) # r → randitem_index -PR-
        q.append(item[r][0]+zero3(r))
    return q

def rname():
    q = ""
    for _ in range(5):
        q += chr(randint(65,90))
    return q