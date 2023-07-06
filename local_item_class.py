from random import randint, choice
from local_scripts import zero3

item = [
    #  values": [damage, acc, [str|dex], tier, attacks]
["]", {'item': 'KNIFE [', 'type': ']', 'values': [2, 60, [2, 2], 1, 1], 'cost': 72, 'grouping': False, 'ident': True}], #0
["}", {'item': 'SLING {', 'type': '}', 'values': [1, 60, [2, 2], 1, 1], 'cost': 18, 'grouping': False, 'ident': True}], #1
["~", {'item': 'TORCH', 'type': '', 'values': [1, 'TORCHES'], 'cost': 30, 'grouping': True, 'ident': True}], #2
["*", {'item': 'BREAD', 'type': '', 'values': [1, 'BREADS'], 'cost': 50, 'grouping': True, 'ident': True}], #3
["*", {'item': 'CORPSE', 'type': '', 'values': [1, 'CORPSES'], 'cost': 5, 'grouping': True, 'ident': True}], #4
["-", {'item': 'ARROW', 'type': '', 'values': [2, 'ARROWS'], 'cost': 1, 'grouping': True, 'ident': True}], #5
["-", {'item': 'ARROW', 'type': '', 'values': [3, 'ARROWS'], 'cost': 1, 'grouping': True, 'ident': True}], #6
["-", {'item': 'ARROW', 'type': '', 'values': [4, 'ARROWS'], 'cost': 1, 'grouping': True, 'ident': True}], #7
["-", {'item': 'ARROW', 'type': '', 'values': [5, 'ARROWS'], 'cost': 1, 'grouping': True, 'ident': True}], #8
["!", {'item': 'POTION OF HEALING', 'type': '!', 'values': [1, 'POTIONS OF HEALING'], 'cost': 200, 'grouping': True, 'ident': True}], #9
["!", {'item': 'POISON', 'type': '!', 'values': [1, 'POISON'], 'cost': 0, 'grouping': True, 'ident': True}], #10
["!", {'item': 'POISON', 'type': '!', 'values': [1, 'POISON'], 'cost': 0, 'grouping': True, 'ident': True}], #11
["?", {'item': 'SCROLL OF TELEPORT', 'type': '?', 'values': [1, 'SCROLLS OF TELEPORT'], 'cost': 40, 'grouping': True, 'ident': True}], #12
["?", {'item': 'GAIN EXPERIENCE', 'type': '?', 'values': [1, 'GAIN EXPERIENCE'], 'cost': 2500, 'grouping': True, 'ident': True}], #13
["]", {'item': 'LONG KNIFE [', 'type': ']', 'values': [3, 60, [2, 5], 1, 1], 'cost': 162, 'grouping': False}], #14
["]", {'item': '2 KNIFES [', 'type': ']', 'values': [2, 60, [3, 5], 1, 2], 'cost': 288, 'grouping': False}], #15
["]", {'item': 'SHORT DAGGER [', 'type': ']', 'values': [4, 75, [4, 6], 1, 1], 'cost': 450, 'grouping': False}], #16
["]", {'item': 'DAGGER [', 'type': ']', 'values': [5, 78, [5, 7], 1, 1], 'cost': 760, 'grouping': False}], #17
["]", {'item': 'LONG DAGGER [', 'type': ']', 'values': [6, 80, [6, 8], 1, 1], 'cost': 1152, 'grouping': False}], #18
["]", {'item': 'CLUB [', 'type': ']', 'values': [7, 30, [4, 3], 1, 1], 'cost': 220, 'grouping': False}], #19
["]", {'item': 'WOODEN CLUB [', 'type': ']', 'values': [10, 33, [6, 4], 1, 1], 'cost': 544, 'grouping': False}], #20
["]", {'item': 'MACE [', 'type': ']', 'values': [8, 30, [7, 5], 1, 2], 'cost': 1152, 'grouping': False}], #21
["]", {'item': 'FLAIL [', 'type': ']', 'values': [7, 30, [8, 6], 1, 3], 'cost': 1984, 'grouping': False}], #22
["]", {'item': 'SHOVEL [', 'type': ']', 'values': [3, 50, [4, 2], 1, 1], 'cost': 112, 'grouping': False}], #23
["]", {'item': 'SICKLE [', 'type': ']', 'values': [2, 70, [2, 4], 1, 1], 'cost': 98, 'grouping': False}], #24
["]", {'item': 'PUGINALE [', 'type': ']', 'values': [6, 40, [6, 2], 1, 1], 'cost': 288, 'grouping': False}], #25
["]", {'item': 'SPEAR [', 'type': ']', 'values': [11, 30, [7, 3], 1, 1], 'cost': 544, 'grouping': False}], #26
["]", {'item': 'PIKE [', 'type': ']', 'values': [16, 30, [8, 4], 1, 1], 'cost': 1152, 'grouping': False}], #27
["]", {'item': 'HALBEARD [', 'type': ']', 'values': [22, 30, [9, 5], 1, 1], 'cost': 2178, 'grouping': False}], #28
["]", {'item': 'HAND AXE [', 'type': ']', 'values': [3, 60, [5, 2], 1, 1], 'cost': 162, 'grouping': False}], #29
["]", {'item': 'AXE [', 'type': ']', 'values': [5, 60, [6, 3], 2, 1], 'cost': 450, 'grouping': False}], #30
["]", {'item': 'HAEVY AXE [', 'type': ']', 'values': [8, 60, [7, 4], 3, 1], 'cost': 1152, 'grouping': False}], #31
["]", {'item': 'BROAD AXE [', 'type': ']', 'values': [10, 60, [8, 5], 4, 1], 'cost': 1800, 'grouping': False}], #32
["]", {'item': 'BATTLE AXE [', 'type': ']', 'values': [11, 60, [9, 5], 4, 1], 'cost': 2178, 'grouping': False}], #33
["]", {'item': 'SHORT SWORD [', 'type': ']', 'values': [8, 40, [6, 3], 1, 1], 'cost': 512, 'grouping': False}], #34
["]", {'item': 'SWORD [', 'type': ']', 'values': [12, 40, [7, 4], 2, 1], 'cost': 1152, 'grouping': False}], #35
["]", {'item': 'LONG SWORD [', 'type': ']', 'values': [15, 40, [8, 5], 3, 1], 'cost': 1800, 'grouping': False}], #36
["]", {'item': 'GREAT SWORD [', 'type': ']', 'values': [16, 40, [9, 5], 4, 1], 'cost': 2048, 'grouping': False}], #37
["]", {'item': 'FOIL [', 'type': ']', 'values': [2, 60, [4, 4], 1, 2], 'cost': 288, 'grouping': False}], #38
["]", {'item': 'RAPIER [', 'type': ']', 'values': [2, 55, [5, 5], 1, 3], 'cost': 544, 'grouping': False}], #39
["]", {'item': 'SABRE [', 'type': ']', 'values': [3, 50, [6, 6], 1, 3], 'cost': 1012, 'grouping': False}], #40
["]", {'item': 'KATANA [', 'type': ']', 'values': [7, 40, [7, 7], 2, 2], 'cost': 1568, 'grouping': False}], #41
["}", {'item': 'SHORT BOW {', 'type': '}', 'values': [3, 60, [2, 6], 1, 1], 'cost': 162, 'grouping': False}], #42
["}", {'item': 'BOW {', 'type': '}', 'values': [5, 60, [3, 7], 2, 1], 'cost': 450, 'grouping': False}], #43
["}", {'item': 'REFLEXIVE BOW {', 'type': '}', 'values': [8, 60, [4, 8], 3, 1], 'cost': 1152, 'grouping': False}], #44
["}", {'item': 'LONGBOW {', 'type': '}', 'values': [11, 60, [5, 9], 4, 1], 'cost': 2178, 'grouping': False}], #45
["}", {'item': 'HAND CROSBOW {', 'type': '}', 'values': [3, 40, [5, 3], 1, 1], 'cost': 72, 'grouping': False}], #46
["}", {'item': 'CROSBOW {', 'type': '}', 'values': [8, 40, [7, 7], 4, 1], 'cost': 512, 'grouping': False}], #47
[")", {'item': 'CLOTHING (', 'type': ')', 'values': [0, 'e_armor', [2, 2]], 'cost': 4, 'grouping': False}], #48
[")", {'item': 'SOFT LEATHER (', 'type': ')', 'values': [1, 'e_armor', [2, 2]], 'cost': 144, 'grouping': False}], #49
[")", {'item': 'FABRIC (', 'type': ')', 'values': [0, 'e_shield', 6], 'cost': 0, 'grouping': False}], #50
[")", {'item': 'SMALL SHIELD (', 'type': ')', 'values': [1, 'e_shield', 8], 'cost': 112, 'grouping': False}], #51
]

def item_class_get(it): # in the future, when I will remake the itemlist -PR-
    q = item[it][1].copy()
    q["values"] = item[it][1]["values"].copy()
    return q

def get_item(it):
    q = item[it][1].copy()
    q["values"] = item[it][1]["values"].copy()
    return q

def get_item_more(it):
    q = item[it].copy()
    q[1]["values"] = item[it][1]["values"].copy()
    return q

def disable_disabled_weapons(s, d):
    global item
    for i in range(len(item)):
        if item[i][0] in {"]","}"}:
            t = item[i][1]["values"][2]
            if t[0] > s+3 or t[1] > d+3:
                item[i] = item[(i%4+5)]

def randitem(hm): # how many -PR-
    global item
    i, q = len(item)-1, []
    for _ in range(hm):
        r = randint(0, i) # r → randitem_index -PR-
        q.append(item[r][0]+zero3(r))
    return q