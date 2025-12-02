
import sys
import Hjälp
import Kontroll as k
from Register import Register
from Jämför import Jämför

REGISTER_FIL = "register.txt"
KODNING = "utf-8"


def menyloop(titel, meny_val):
    """
    Menyloop som hanterar en dictionary, 
    där nyckel är en tuple av beskrivande text och funktion. 

    Args:
        titel(str): Namnet på menyn
        meny_val(dict): Dictionary för meny där nyckel -> (text: str, funktion)
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
            funktion()
        else:
            print("Ogiltigt val.")


def läs_registerlista():
    """
    Returnerar lista med register-namn från REGISTER_FIL (utan tomma rader).
    """
    registren = []
    try:
        with open(REGISTER_FIL, encoding=KODNING) as f:
            for rad in f:
                register_namn = rad.strip()
                if register_namn:
                    registren.append(register_namn)
    except FileNotFoundError:
        # Skapa filen om den saknas
        open(REGISTER_FIL, "x", encoding=KODNING).close()
    except Exception as e:
        print("Fel vid läsning av registerfil:", e)
    return registren


def register_meny_factory(register):
    """
    Returnerar meny-dict för ett Register-objekt.
    
    Args:
        register: Specifika objektet som ska hanteras av Register-klassen

    Returns:
        Ett dictionary för ett Register-objekt
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
    registren = läs_registerlista()
    if not registren:
        print("Inga register finns. Skapa ett nytt register först.")
        skapa_register()

    while True:
        print("\n=== VÄLJ REGISTER ===")
        for position, namn in enumerate(registren, start=1):
            print(f"{position}: {namn}")
        print("X. Tillbaka")

        val = input("Välj ett register: ").strip().upper()
        if val == "X":
            return

        if val.isdigit():
            position = int(val) - 1
            if 0 <= position < len(registren):
                registernamn = registren[position]
                register = Register(registernamn)
                menyloop(f"Register: {registernamn}", register_meny_factory(register))
                # Återläs listan utifall registerfil ändrats (t.ex. sparats med nytt namn)
                registren = läs_registerlista()
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

    # Skriv till register-listan (endast om det inte redan finns)
    registren = läs_registerlista()
    if nytt_register in registren:
        print(f"Registret '{nytt_register}' finns redan.")
    else:
        try:
            with open(REGISTER_FIL, "a", encoding=KODNING) as r:
                # Om filen inte var tom, lägg till newline först
                if registren:
                    r.write("\n" + nytt_register)
                else:
                    r.write(nytt_register)
            print(f"Registret '{nytt_register}' skapades.")
        except Exception as e:
            print("Fel vid skapande av register:", e)
            return

    # Skapa registerfil om den inte redan finns
    try:
        open(nytt_register + ".txt", "x", encoding=KODNING).close()
    except FileExistsError:
        pass
    except Exception as e:
        print("Fel vid skapande av registerfil:", e)

    # Gå direkt in i registermenyn för det nya registret
    register = Register(nytt_register)
    menyloop(f"Register: {nytt_register}", register_meny_factory(register))


def välj_två_register():
    """
    Låter användaren välja två olika register från registerlistan.
    Returnerar tuple (reg1_namn, reg2_namn) eller (None, None) om avbrutet.
    """
    registren = läs_registerlista()
    if len(registren) < 2:
        print("Minst två register krävs för jämförelse.")
        return None, None

    valda = []
    for i in range(1, 3):
        while True:
            print("\n=== VÄLJ REGISTER FÖR JÄMFÖRELSE ===")
            for position, namn in enumerate(registren, start=1):
                marker = "(valt)" if namn in valda else ""
                print(f"{position}: {namn} {marker}")
            print("X. Avbryt jämförelse")

            val = input(f"Välj register #{i}: ").strip().upper()
            if val == "X":
                return None, None
            if not val.isdigit():
                print("Ogiltigt val. Ange siffra.")
                continue
            position = int(val) - 1
            if not (0 <= position < len(registren)):
                print("Ogiltigt index.")
                continue
            valt = registren[position]
            if valt in valda:
                print("Du har redan valt detta register. Välj ett annat.")
                continue
            valda.append(valt)
            break

    if len(valda) == 2:
        return valda[0], valda[1]
    return None, None


def välj_jämförelsemetod_och_kör(reg1_namn, reg2_namn):
    """
    Visar jämförelsemetoder och kör vald metod med två registren innehåll.
    """
    if not reg1_namn or not reg2_namn:
        print("Felaktiga register för jämförelse.")
        return

    # Skapa Register-objekt (antas att Register tar hand om att läsa innehåll)
    r1 = Register(reg1_namn)
    r2 = Register(reg2_namn)

    meny = {
        "1": ("Personer i båda registerna", lambda: Jämför.personer_i_båda(r1, r2)),
        "2": ("Personer i något av registerna (unika)", lambda: Jämför.unika_i_något(r1, r2)),
    }

    menyloop(f"Jämför: {reg1_namn} / {reg2_namn}", meny)


def jämför_register_flöde():
    """
    Kör funktionen väl_två_register() och ansätter valen till två variabler. Om inga
    register väljs går programmet tillbaka till huvudmenyn. Om två register väljs körs
    funktionen välj_jämförelsemetod_och_kör()
    """
    reg1, reg2 = välj_två_register()
    if not reg1 or not reg2:
        print("Jämförelse avbröts eller misslyckades.")
        return
    välj_jämförelsemetod_och_kör(reg1, reg2)


def main():
    """
    Main som också hanterar dictionaryn huvudmeny, skickas direkt till
    menyloop()
    """
    huvudmeny = {
        "1": ("Välj register", välj_register),
        "2": ("Lägg till register", skapa_register),
        "3": ("Jämför register", jämför_register_flöde),
        "?": ("Hjälpmeny", lambda: Hjälp.huvud_hjälp_meny()),
        "0": ("Avsluta", lambda: sys.exit())
    }

    menyloop("Huvudmeny", huvudmeny)


if __name__ == "__main__":
    main()
