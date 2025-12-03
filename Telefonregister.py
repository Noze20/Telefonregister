"""
Program som hanterar flera telefonregister. Användaren kan skapa,
ändra, söka, sortera och ta bort personer från ett specifikt register.
Programmet kan även hjälpa användaren att jämföra två olika telefonregister,
både veta vilka som finns i båda och vilka som finns i något av registerna.
Programmet är uppbygt utifrån en meny och sparar registrerna och personerna i
registrerna i textfiler.
"""

import sys
import Hjälp
import Kontroll as k
from Register import Register
from Jämför import Jämför

REGISTER_FIL = "register.txt"
KODNING = "utf-8"


def menyloop(titel, meny_val):
    """
    Menyloop som körs utifrån ett uppslagsverk av menyval.

    Nyckeln i uppslagverket är ett strängval och varje
    värde är en tuple -> (text: str, funktion) 

    Args:
        titel(str): Namnet på menyn
        meny_val(dict): uppslagsverk för meny {"str": (text: str, funktion(_): anropsbar)}

    Returns:
        none
    """

    while True:
        print(f"\n=== {titel.upper()} ===")
        for nyckel, (text, _) in meny_val.items():
            print(f"{nyckel}. {text}")
        if titel != "Huvudmeny":
            print("X. Tillbaka")

        val = input("Välj: ").strip().upper()

        if val == "X" and titel != "Huvudmeny":
            break
        elif val in meny_val:
            _, funktion = meny_val[val]
            try:
                funktion()
            except Exception as fel:
                print("Ett fel uppstod", fel)
        else:
            print("Ogiltigt val.")


def läs_registerlista():
    """
    Skapar en lista, öppnar filen register.txt och skriver in varje rad
    i listan utan mellanslag. Om filen saknas skapas en ny fil med samma namn.

    Returns:
        register_lista(list): Lista med alla registernamn från REGISTER_FIL
    """
    register_lista = []
    try:
        with open(REGISTER_FIL, encoding=KODNING) as fil:
            for rader in fil:
                register_namn = rader.strip()
                if register_namn:
                    register_lista.append(register_namn)
    except FileNotFoundError:
        open(REGISTER_FIL, "x", encoding=KODNING).close()
    except Exception as fel:
        print("Fel vid läsning av registerfil:", fel)
    return register_lista


def register_meny(register):
    """
    Returnerar meny uppslagsverk för ett Register-objekt.
    
    Args:
        register(obj): Specifika objektet som ska hanteras av Register-klassen

    Returns:
        Ett uppslagsverk för ett Register-objekt av register
    """
    
    return {
        "1": ("Öppna fil", register.fil_öppning),
        "2": ("Sök i registret", register.sök_i_registret),
        "3": ("Ändra i registret", register.ändra_i_registret),
        "4": ("Lägg till i registret", register.lägga_till_i_registret),
        "5": ("Ta bort från registret", register.ta_bort_från_registret),
        "6": ("Sortera registret", register.sortera_registret),
        "7": ("Spara registret", register.spara_till_registret),
        "8": ("Visa alla i registret", register.visa_hela_registret)
    }


def välj_register():
    """
    Visar alla register och låter användaren välja ett, för att sedan starta specifik meny.
    Hanterar ogiltligt inmatning, samt om det inte finns några register startar funktionen
    skapa_register() så att användaren kan skapa ett register. Funktionen avslutas när
    användaren matar in X/x.
    """
    register_lista = läs_registerlista()
    if not register_lista:
        print("Inga register finns. Skapa ett nytt register först.")
        skapa_register()
        register_lista = läs_registerlista()

    while True:
        print("\n=== VÄLJ REGISTER ===")
        for position, namn in enumerate(register_lista, start=1):
            print(f"{position}: {namn}")
        print("X. Tillbaka")

        val = input("Välj ett register: ").strip().upper()
        if val == "X":
            return

        if val.isdigit():
            position = int(val) - 1
            if 0 <= position < len(register_lista):
                registernamn = register_lista[position]
                register = Register(registernamn)
                menyloop(f"Register: {registernamn}", register_meny(register))
                register_lista = läs_registerlista()
            else:
                print("Ogiltigt val: index utanför spann.")
        else:
            print("Ogiltigt val. Ange siffra eller X.")


def skapa_register():
    """
    Skapa nytt register och gå direkt in i registermenyn för det nya registret.
    """
    nytt_register = k.skapa_fil_kontroll("Nytt registernamn: ")
    if not nytt_register:
        print("Inget giltigt namn angavs.")
        return

    register_lista = läs_registerlista()
    if nytt_register in register_lista:
        print(f"Registret '{nytt_register}' finns redan.")
    else:
        try:
            with open(REGISTER_FIL, "a", encoding=KODNING) as r:
                    r.write("\n" + nytt_register)
            print(f"Registret {nytt_register} skapades.")
        except Exception as fel:
            print("Fel vid skapande av register:", fel)
            return

    register = Register(nytt_register)
    menyloop(f"Register: {nytt_register}", register_meny(register))


def välj_två_register():
    """
    Låter användaren välja två olika register från registerlistan.
    Returnerar tuple (register1_namn, register2_namn) eller (None, None) om avbrutet.
    """
    register_lista = läs_registerlista()
    if len(register_lista) < 2:
        print("Minst två register krävs för jämförelse.")
        return None, None

    valda_register = []
    for i in range(1, 3):
        while True:
            print("\n=== VÄLJ REGISTER FÖR JÄMFÖRELSE ===")
            for position, namn in enumerate(register_lista, start=1):
                marker = "(valt)" if namn in valda_register else ""
                print(f"{position}: {namn} {marker}")
            print("X. Avbryt jämförelse")

            val = input(f"Välj register #{i}: ").strip().upper()
            if val == "X":
                return None, None
            if not val.isdigit():
                print("Ogiltigt val. Ange siffra.")
                continue
            position = int(val) - 1
            if not (0 <= position < len(register_lista)):
                print("Ogiltigt index.")
                continue
            valt = register_lista[position]
            if valt in valda_register:
                print("Du har redan valt detta register. Välj ett annat.")
                continue
            valda_register.append(valt)
            break

    if len(valda_register) == 2:
        return valda_register[0], valda_register[1]
    return None, None


def välj_jämförelsemetod(register1_namn, register2_namn):
    """
    Visar jämförelsemetoder och kör vald metod med två register_lista innehåll.
    """
    if not register1_namn or not register2_namn:
        print("Felaktiga register för jämförelse.")
        return

    r1 = Register(register1_namn)
    r2 = Register(register2_namn)

    meny = {
        "1": ("Personer i båda registerna", lambda: Jämför.personer_i_båda(r1, r2)),
        "2": ("Personer i något av registerna (unika)", lambda: Jämför.unika_i_något(r1, r2)),
    }

    menyloop(f"Jämför: {register1_namn} / {register2_namn}", meny)


def jämför_register():
    """
    Kör funktionen väl_två_register() och ansätter valen till två variabler. Om inga
    register väljs går programmet tillbaka till huvudmenyn. Om två register väljs körs
    funktionen välj_jämförelsemetod()
    """
    register1, register2 = välj_två_register()
    if not register1 or not register2:
        print("Jämförelse avbröts eller misslyckades.")
        return
    välj_jämförelsemetod(register1, register2)


def main():
    """
    Main som också hanterar dictionaryn huvudmeny, skickas direkt till
    menyloop()
    """
    huvudmeny = {
        "1": ("Välj register", välj_register),
        "2": ("Lägg till register", skapa_register),
        "3": ("Jämför register", jämför_register),
        "?": ("Hjälpmeny", lambda: Hjälp.huvud_hjälp_meny()),
        "0": ("Avsluta", lambda: sys.exit())
    }

    menyloop(f"Huvudmeny", huvudmeny)


if __name__ == "__main__":
    main()
