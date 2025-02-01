# API off ↓

def translate(ang, number = 0):
    return ang


# translation API

"""
'''lang_PL = {
    #"A MONSTER": "POTWORA",
    "AND IT WILL GIVE YOU LIGHT FOR": "I BĘDZIE TOBIE DAWAĆ ŚWIATŁO PRZEZ",
    "ARROW": "STRZAŁĘ",
    "ARROW1": "STRZAŁA",
    "ARROWS2": "STRZAŁY",
    "ARROWS5": "STRZAŁ",
    "BOW": "ŁUK",
    "BREAD": "CHLEB",
    "BREAD1": "CHLEB",
    "BREADS2": "CHLEBY",
    "BREADS5": "CHLEBÓW",
    "CORPSE": "TRUPA",
    "CORPSE1": "TRUP",
    "CORPSES2": "TRUPY",
    "CORPSES5": "TRUPÓW",
    "CROSBOW": "KUSZA",
    "DAGGER": "SZTYLET",
    "FUR": "FUTRO",
    "GOLD1": "ZŁOTO",
    "GOLD2": "ZŁOTE",
    "GOLD5": "ZŁOTYCH",
    "HERE ARE": "TUTAJ JEST",
    "HERE IS A WALL": "TU JEST ŚCIANA",
    "HERE IS": "TUTAJ JEST",
    "KNIFE": "NÓŻ",
    "LONG BOW": "DŁUGI ŁUK",
    "MACE": "BUŁAWA",
    "MIXTURE": "MIXTURKĘ",
    "MIXTURE1": "MIXTURKA",
    "RING OF POWER": "PIERŚCIEŃ MOCY",
    "RING": "PIERŚCIEŃ",
    "SHORT BOW": "KRÓTKI ŁUK",
    "SHORT SWORD": "KRÓTKI MIECZ",
    "SLING": "PROCA",
    "THIS TILE IS CLOSED": "TO POLE JEST ZAMKNIĘTE",
    "TORCH": "POCHODNIĘ",
    "TORCH1": "POCHODNIA",
    "TORCHES2": "POCHODNIE",
    "TORCHES5": "POCHODNI",
    "TURNS": "TUR",
    "YOU ATE A": "ZJADŁEŚ",
    "YOU CAN'T GO DOWN HERE": "NIE MOŻESZ TUTAJ ZEJŚĆ NA DÓŁ",
    "YOU CAN'T GO UP HERE": "NIE MOŻESZ TUTAJ WEJŚĆ DO GÓRY",
    "YOU DRANK A": "WYPIŁEŚ",
    "YOU HIT A": "ZRANIŁEŚ",
    "YOU KILL A": "ZABIŁEŚ",
    "YOU LIGHT A": "ZAPALIŁEŚ",
    "YOU MISS A": "SPUDŁOWAŁEŚ",
    "YOU WENT DOWN": "ZSZEDŁEŚ W DÓŁ",
    "YOU WENT UP": "WSZEDŁEŚ DO GÓRY",
    "YOU TOOK": "WZIĄŁEŚ",
    }'''
lang_PL = {
    "CHOOSE A SPELL TO CAST:": "WYBIERZ ZAKLĘCIE KTÓRE CHCESZ RZUCIĆ:",
    "YOU FAILED TO CAST THE SPELL": "NIE UDAŁO CI SIĘ RZUCIĆ ZAKLĘCIA",
    "TELEPORTED": "PRZETELEPORTOWANO",
    "HEALED": "ULECZONY",
    "DETECTED": "PRZESKANOWANO POZIOM",
    "TELEPORTED": "PRZETELEPORTOWANO",
    "YOU CAN'T BE HEALED MORE": "NIE MOŻESZ ZOSTAĆ BARDZEJ ULECZONY",
    "YOU CAN'T CAST THE SPELL HERE!": "NIE MOŻESZ W TYM MIEJSCU RZUCIĆ ZAKLĘCIA!",
    "YOU FAILED TO CAST THE SPELL": "NIE UDAŁO CI SIĘ RZUCIĆ ZAKLĘCIA",
    "IN WHAT DIRECTION DO YOU WANT TO CAST THE SPELL?:": "W JAKIM KIERUNKU CHCESZ RZUCIĆ ZAKLĘCIE?:",
    "WRONG DIRECTION!": "ZŁY KIERUNEK!",
    "SPARKS FLY AROUND YOU...": "ISKRY LATAJĄ WOKÓŁ CIEBIE...",
    "YOU HAVE LIGHT, YOU CAN'T SPELL MORE": "MASZ ŚWIATŁO, WIĘC NIE MOŻESZ RZUCIĆ ZAKLĘCIA PRZYWOŁANIA ŚWIATŁA",
    "MAGIC LIGHT": "MAGICZNE ŚWAITŁO",
    "TELEPORTATION": "TELEPORTACJA",
    "MAGIC MISSLE": "MAGICZNY POCISK",
    "DEDECT NATURE": "ZNAJDZ NATURĘ",
    "DRUID'S SHOT": "DRUIDZKI STRZAŁ",
    "WORDS OF NATURE": "SŁOWA NATURY",
    #"HERBALIZM": "HERBALIZM",
    "DETECT WATER": "ZNAJDZ WODĘ",
    "WATER JUMP": "WODNA TELEPORTACJA",
    "CONDENCE HUMID": "SKONDENSUJ WILGOĆ",
    "WATER FIST": "WODNA PIĘŚĆ",
    #"TSUNAMI": "TSUNAMI",
    "HYDROGEN BLAST": "WYBUCH WODORU",
    "FIRE BALL": "KULA OGNIA",
    "LIGHTNING": "BŁUSKAWICA",
    "BLAST!": "WYBUCH!",
}
def translate(ang, number = 0):
    lang = "PL" #not all done yet
    match lang:
        case "PL":
            return l_pl(ang, number)
        case _:
            return ang
def l_pl(ang, number):
    global lang_PL # why not? -PR-
    return lang_PL.get(ang+("" if number == 0 else "1" if number == 1 else "2" if number < 5 or number % 10 in [2, 3, 4] and number > 20 else "5"), ang)"""