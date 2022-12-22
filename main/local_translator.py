lang_PL = {
    "YOU WENT UP": "WSZEDŁEŚ DO GÓRY",
    "YOU WENT DOWN": "ZSZEDŁEŚ W DÓŁ",
    "YOU CAN'T GO UP HERE": "NIE MOŻESZ TUTAJ WEJŚĆ DO GÓRY",
    "YOU CAN'T GO DOWN HERE": "NIE MOŻESZ TUTAJ ZEJŚĆ NA DÓŁ",
    "HERE IS A WALL": "TU JEST ŚCIANA",
    "HERE IS": "TUTAJ JEST",
    "HERE ARE": "TUTAJ JEST",
    "YOU TAKE": "WZIĄŁEŚ",
    "TORCH": "POCHODNIĘ",
    "TORCH1": "POCHODNIA",
    "TORCHES2": "POCHODNIE",
    "TORCHES5": "POCHODNI",
    "ARROW": "STRZAŁĘ",
    "ARROW1": "STRZAŁA",
    "ARROWS2": "STRZAŁY",
    "ARROWS5": "STRZAŁ",
    "BREAD": "CHLEB",
    "BREAD1": "CHLEB",
    "BREADS2": "CHLEBY",
    "BREADS5": "CHLEBÓW",
    "CORPSE": "TRUPOWI",
    "CORPSE1": "TRUP",
    "CORPSES2": "TRUPY",
    "CORPSES5": "TRUPÓW",
    "MIXTURE": "MIXTURKĘ",
    "MIXTURE1": "MIXTURKA",
    "KNIFE": "NÓŻ",
    "DAGGER": "SZTYLET",
    "SHORT SWORD": "KRÓTKI MIECZ",
    "MACE": "BUŁAWA",
    "SLING": "PROCA",
    "SHORT BOW": "KRÓTKI ŁUK",
    "BOW": "ŁUK",
    "LONG BOW": "DŁUGI ŁUK",
    "CROSBOW": "KUSZA",
    "RING": "PIERŚCIEŃ",
    "RING OF POWER": "PIERŚCIEŃ MOCY",
    "FUR": "FUTRO",
    "YOU KILL": "ZABIŁEŚ",
    "YOU HIT": "ZRANIŁEŚ",
    "YOU MISS": "SPUDŁOWAŁEŚ", # YOU MISS. -PR-
    "A MONSTER": "POTWORA",
    "YOU LIGHT A": "ZAPALIŁEŚ",
    "AND IT WILL GIVE YOU LIGHT FOR": "I BĘDZIE TOBIE DAWAĆ ŚWIATŁO PRZEZ",
    "TURNS": "TUR",
    "THIS TILE IS CLOSED": "TO POLE JEST ZAMKNIĘTE",
    "GOLD1": "ZŁOTO",
    "GOLD2": "ZŁOTE",
    "GOLD5": "ZŁOTYCH",
    }
def translate(ang, number = 0):
    lang = "PL"
    match lang:
        case "PL":
            return(l_pl(ang, number))
        case _:
            return(ang)
def l_pl(ang, number):
    global lang_PL
    return(lang_PL.get(ang+("" if number == 0 else "1" if number == 1 else "2" if number < 5 or number % 10 in [2, 3, 4] and number > 20 else "5"), ang))

