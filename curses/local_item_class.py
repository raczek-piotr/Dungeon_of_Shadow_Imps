from random import randint, choice
from local_scripts import zero3


item = [
["-",  [['ROCK', 'ROCKS'], '-', 1, True, 1]],  #0
["-",  [['ARROW', 'ARROWS'], '-', 1, True, 2]],  #1
["-",  [['BOLT', 'BOLTS'], '-', 1, True, 2]],  #2
["-",  [['9mm AMMO', '9mm AMMOS'], '-', 1, True, 5]],  #3
["*",  [['MOLD', 0, 300], '*', 1, True, 3]],  #4
["*",  [['BREAD', 0, 900], '*', 1, True, 13]],  #5
["*",  [['RATION OF FOOD', 0, 1500], '*', 1, True, 25]],  #6
["~",  [['TORCH', 1, 1200], '~', 1, True, 19]],  #7
["?",  [['SCROLL', 2, 0], '?', 1, False, 80]],  #8
["?",  [['SCROLL', 2, 1], '?', 1, False, 50]],  #9
["?",  [['SCROLL', 2, 2], '?', 1, False, 100]],  #10
["?",  [['SCROLL', 2, 3], '?', 1, False, 120]],  #11
["!",  [['POTION', 3, 0], '!', 1, False, 120]],  #12
["!",  [['POTION', 3, 1], '!', 1, False, 120]],  #13
["!",  [['POTION', 3, 2], '!', 1, False, 100]],  #14
["!",  [['POTION', 3, 3], '!', 1, False, 10]],  #15
[")",  [['A T-SHIRT', 'e_armor'], ')', [0, 1], True, 1]],  #16
[")",  [['SOFT LEATHER', 'e_armor'], ')', [1, 3], True, 32]],  #17
[")",  [['HARD LEATHER', 'e_armor'], ')', [2, 6], True, 130]],  #18
[")",  [['LEATHER MAIL', 'e_armor'], ')', [4, 13], True, 520]],  #19
[")",  [['CHAIN MAIL', 'e_armor'], ')', [5, 27], True, 813]],  #20
[")",  [['CHAIN ARMOR', 'e_armor'], ')', [7, 37], True, 1595]],  #21
[")",  [['PLATE ARMOR', 'e_armor'], ')', [8, 47], True, 2083]],  #22
["]",  [['KNIFE', 'e_attack'], ']', [1, 3, 1, 60, 6, 7], True, 120]],  #23
["]",  [['WOODEN CLUB', 'e_attack'], ']', [2, 2, 2, 30, 8, 7], True, 270]],  #24
["]",  [['SICKLE', 'e_attack'], ']', [1, 5, 1, 50, 8, 9], True, 187]],  #25
["]",  [['SHOWEL', 'e_attack'], ']', [2, 3, 1, 40, 9, 8], True, 213]],  #26
["]",  [['PICK', 'e_attack'], ']', [1, 7, 1, 40, 10, 7], True, 213]],  #27
["]",  [['LONG KNIFE', 'e_attack'], ']', [1, 5, 1, 60, 7, 8], True, 270]],  #28
["]",  [['2 KNIFES', 'e_attack'], ']', [1, 3, 2, 60, 8, 9], True, 480]],  #29
["]",  [['DAGGER', 'e_attack'], ']', [2, 4, 1, 60, 9, 10], True, 750]],  #30
["]",  [['LONG DAGGER', 'e_attack'], ']', [2, 6, 1, 60, 10, 12], True, 1470]],  #31
["]",  [['HEAVY DAGGER', 'e_attack'], ']', [2, 9, 1, 60, 11, 13], True, 3000]],  #32
["]",  [['FOIL', 'e_attack'], ']', [1, 2, 2, 80, 8, 9], True, 270]],  #33
["]",  [['RAPIER', 'e_attack'], ']', [1, 3, 2, 60, 9, 10], True, 480]],  #34
["]",  [['SABRE', 'e_attack'], ']', [2, 4, 1, 60, 10, 11], True, 750]],  #35
["]",  [['KATANA', 'e_attack'], ']', [2, 6, 1, 60, 11, 12], True, 1470]],  #36
["]",  [['PUGINALE', 'e_attack'], ']', [3, 3, 1, 40, 11, 7], True, 270]],  #37
["]",  [['HANDAXE', 'e_attack'], ']', [2, 3, 1, 70, 11, 8], True, 653]],  #38
["]",  [['CLUB', 'e_attack'], ']', [2, 3, 2, 35, 11, 8], True, 653]],  #39
["]",  [['SMALL SWORD', 'e_attack'], ']', [2, 5, 1, 50, 12, 8], True, 750]],  #40
["]",  [['SPEAR', 'e_attack'], ']', [2, 9, 1, 30, 12, 8], True, 750]],  #41
["]",  [['SWORD', 'e_attack'], ']', [2, 8, 1, 50, 12, 9], True, 1687]],  #42
["]",  [['AXE', 'e_attack'], ']', [3, 4, 1, 60, 12, 9], True, 1687]],  #43
["]",  [['MACE', 'e_attack'], ']', [2, 4, 2, 45, 12, 9], True, 1687]],  #44
["]",  [['PIKE', 'e_attack'], ']', [3, 9, 1, 30, 12, 9], True, 1687]],  #45
["]",  [['BATTLE AXE', 'e_attack'], ']', [4, 5, 1, 60, 13, 10], True, 4320]],  #46
["]",  [['GREAT FLAIL', 'e_attack'], ']', [2, 7, 2, 45, 13, 10], True, 4320]],  #47
["]",  [['HALABEARD', 'e_attack'], ']', [4, 10, 1, 35, 14, 10], True, 4940]],  #48
["]",  [['GREAT SWORD', 'e_attack'], ']', [2, 13, 1, 55, 14, 10], True, 4940]],  #49
["}",  [['SLING', 'e_hand', 'ROCK'], '}', [1, 1, 1, 60, 6, 7], True, 15]],  #50
["}",  [['SHORT BOW', 'e_hand', 'ARROW'], '}', [1, 5, 1, 60, 7, 11], True, 135]],  #51
["}",  [['BOW', 'e_hand', 'ARROW'], '}', [1, 9, 1, 60, 8, 12], True, 375]],  #52
["}",  [['COMPOSIVE BOW', 'e_hand', 'ARROW'], '}', [1, 15, 1, 70, 9, 13], True, 1306]],  #53
["}",  [['LONG BOW', 'e_hand', 'ARROW'], '}', [1, 22, 1, 80, 10, 14], True, 3526]],  #54
["}",  [['HAND CROSSBOW', 'e_hand', 'BOLT'], '}', [1, 8, 1, 40, 10, 8], True, 135]],  #55
["}",  [['LIGHT CROSSBOW', 'e_hand', 'BOLT'], '}', [1, 10, 1, 40, 11, 9], True, 201]],  #56
["}",  [['CROSSBOW', 'e_hand', 'BOLT'], '}', [1, 15, 1, 40, 11, 11], True, 426]],  #57
["}",  [['HAEVY CROSSBOW', 'e_hand', 'BOLT'], '}', [1, 21, 1, 40, 12, 12], True, 806]],  #58
["}",  [['GUN', 'e_hand', '9mm AMMO'], '}', [2, 1, 1, 90, 7, 7], True, 135]],  #59
]

def get_item(it):
    q = item[it][1].copy()
    if q[1] in {"]",")","}"}:
        q[2] = item[it][1][2].copy()
    return q

def change_item(it):
    return item[it][1]

def randitem(hm, p = 0, k = 0): # how many -PR-
    global item
    if k == 0:
        k = len(item)-1
    q = []
    for _ in range(hm):
        r = randint(p, k) # r → randitem_index -PR-
        q.append(item[r][0]+zero3(r))
    return q