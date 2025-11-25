
import sys
import Hjälp
import Kontroll as k
from Register import Register
from Jämför import Jämför

REGISTER_LIST_FIL = "register.txt"
ENCODING = "utf-8"


def menyloop(titel: str, meny_val: dict):
    """Generisk menyloop. meny_val är en dict där nyckel -> (text, funktion)."""
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


def läs_registerlista() -> list:
    """Returnerar lista med register-namn från REGISTER_LIST_FIL (utan tomma rader)."""
    registers = []
    try:
        with open(REGISTER_LIST_FIL, encoding=ENCODING) as f:
            for rad in f:
                namn = rad.strip()
                if namn:
                    registers.append(namn)
    except FileNotFoundError:
        # Skapa filen om den saknas
        open(REGISTER_LIST_FIL, "x", encoding=ENCODING).close()
    except Exception as e:
        print("Fel vid läsning av registerfil:", e)
    return registers


def register_meny_factory(register: Register):
    """Returnerar meny-dict för ett Register-objekt.
    Observera: vi antar att Register-klassen har de metoder som användes tidigare.
    """
    # Om Register behöver ladda innehåll från fil någonstans, anta att Register init tar hand om det.
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
    """Visa listan med register och öppna valt register i registermenyn."""
    registers = läs_registerlista()
    if not registers:
        print("Inga register finns. Skapa ett nytt register först.")
        skapa_register()

    while True:
        print("\n=== VÄLJ REGISTER ===")
        for idx, namn in enumerate(registers, start=1):
            print(f"{idx}: {namn}")
        print("X. Tillbaka")

        val = input("Välj ett register: ").strip().upper()
        if val == "X":
            return

        if val.isdigit():
            idx = int(val) - 1
            if 0 <= idx < len(registers):
                registernamn = registers[idx]
                register = Register(registernamn)
                menyloop(f"Register: {registernamn}", register_meny_factory(register))
                # Återläs listan utifall registerfil ändrats (t.ex. sparats med nytt namn)
                registers = läs_registerlista()
            else:
                print("Ogiltigt val: index utanför spann.")
        else:
            print("Ogiltigt val. Ange siffra eller X.")


def skapa_register():
    """Skapa nytt register och gå direkt in i registermenyn för det nya registret."""
    nytt_register = k.skapa_fil_kontroll("Nytt registernamn: ")
    if not nytt_register:
        print("Inget giltigt namn angavs.")
        return

    # Skriv till register-listan (endast om det inte redan finns)
    registers = läs_registerlista()
    if nytt_register in registers:
        print(f"Registret '{nytt_register}' finns redan.")
    else:
        try:
            with open(REGISTER_LIST_FIL, "a", encoding=ENCODING) as r:
                # Om filen inte var tom, lägg till newline först
                if registers:
                    r.write("\n" + nytt_register)
                else:
                    r.write(nytt_register)
            print(f"Registret '{nytt_register}' skapades.")
        except Exception as e:
            print("Fel vid skapande av register:", e)
            return

    # Skapa registerfil om den inte redan finns (Register-klass kan också göra detta, men vi säkrar)
    try:
        open(nytt_register + ".txt", "x", encoding=ENCODING).close()
    except FileExistsError:
        pass
    except Exception as e:
        print("Fel vid skapande av registerfil:", e)

    # Gå direkt in i registermenyn för det nya registret
    register = Register(nytt_register)
    menyloop(f"Register: {nytt_register}", register_meny_factory(register))


def välj_två_register() -> tuple:
    """Låter användaren välja två olika register från registerlistan.
    Returnerar tuple (reg1_namn, reg2_namn) eller (None, None) om avbrutet.
    """
    registers = läs_registerlista()
    if len(registers) < 2:
        print("Minst två register krävs för jämförelse.")
        return None, None

    valda = []
    for i in range(1, 3):
        while True:
            print("\n=== VÄLJ REGISTER FÖR JÄMFÖRELSE ===")
            for idx, namn in enumerate(registers, start=1):
                marker = "(valt)" if namn in valda else ""
                print(f"{idx}: {namn} {marker}")
            print("X. Avbryt jämförelse")

            val = input(f"Välj register #{i}: ").strip().upper()
            if val == "X":
                return None, None
            if not val.isdigit():
                print("Ogiltigt val. Ange siffra.")
                continue
            idx = int(val) - 1
            if not (0 <= idx < len(registers)):
                print("Ogiltigt index.")
                continue
            valt = registers[idx]
            if valt in valda:
                print("Du har redan valt detta register. Välj ett annat.")
                continue
            valda.append(valt)
            break

    if len(valda) == 2:
        return valda[0], valda[1]
    return None, None


def välj_jämförelsemetod_och_kör(reg1_namn: str, reg2_namn: str):
    """Visar jämförelsemetoder och kör vald metod med två registers innehåll."""
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
    """Högre nivå-flöde: välj två register -> välj metod -> kör jämförelse."""
    reg1, reg2 = välj_två_register()
    if not reg1 or not reg2:
        print("Jämförelse avbröts eller misslyckades.")
        return
    välj_jämförelsemetod_och_kör(reg1, reg2)


def main():
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
