lang_PL = {
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
    }
def translate(ang, number = 0):
    lang = "none"
    match lang:
        case "PL":
            return l_pl(ang, number)
        case _:
            return ang
def l_pl(ang, number):
    global lang_PL # why not? -PR-
    return lang_PL.get(ang+("" if number == 0 else "1" if number == 1 else "2" if number < 5 or number % 10 in [2, 3, 4] and number > 20 else "5"), ang)