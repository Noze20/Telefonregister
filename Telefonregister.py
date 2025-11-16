import sys
import Hjälp
import Kontroll as k
from Register import Register
from Jämför import Jämför

def menyloop(titel, meny_val):
    """"""
    while True:
        print(f"\n=== {titel.upper()} ===")
        for nyckel, (text, _) in meny_val.items():
            print(f"{nyckel}. {text}")
        if titel != "Huvudmeny":
            print("X Tillbaka")

        val = input("Välj: ").strip().upper()

        if val == "X" and titel != "Huvudmeny":
            break
        elif val in meny_val:
            _, funktion = meny_val[val]
            funktion()
        else:
            print("Ogiltigt val.")


def register_meny(register):

    filnamn = register.registernamn + ".txt"
    try:
        with open(filnamn, encoding="utf-8") as f:
            for rad in f:
                delar = rad.strip().split(";")  # Skapar en lista, med nytt element varje ;

                if len(delar) != 5:     # Tillser att ingen rad är mer än 5 "delar"
                    print("Felaktig rad, hoppade över", rad)
                    continue

                ny_person = {
                    "efternamn": delar[0].strip(),
                    "förnamn": delar[1].strip(),
                    "mobil": delar[2].strip(),
                    "epost": delar[3].strip(),
                    "adress": delar[4].strip()
                }

                register.personer.append(ny_person)

    except FileNotFoundError:
        open(filnamn, "x")

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

    register_dict = {}
    try:
        with open("register.txt") as r:
            for i, rad in enumerate(r, start=1):
                register_dict[i] = rad.strip()
    except Exception as e:
        print("Fel vid filinläsning", e)
        return

    while True:
        print("\n===REGISTER===")
        for radnmmer, registernamn in register_dict.items():
            print(f"{radnmmer}: {registernamn}")
        print("X: Tillbaka")

        val = (input("Välj ett register: ")).strip().upper()

        if val in register_dict:
            registernamn = register_dict[val]
            register = Register(registernamn)
            menyloop(f"{registernamn}", register_meny(register))
        elif val == "X":
            break
        else:
            print("Ogiltligt val!")


def skapa_register():

    nytt_register = k.skapa_fil_kontroll("Nytt registernamn: ")
    try:
        with open("register.txt", "a") as r:
            r.write("\n" + nytt_register)

    except Exception as e:
        print("Fel vid filinläsning", e)

    # Lägga till så att man kommer direkt in till registermenyn


def välj_jämförelsemetod():

    jämför = {
        "1": ("Personer i båda registerna", Jämför.personer_i_båda),
        "2": ("Personer i något av registerna", Jämför.unika_i_något)
    }


def main():

    huvudmeny = {
        "1": ("Välj register", välj_register),
        "2": ("Lägg till register", skapa_register),
        "3": ("Jämför register", välj_jämförelsemetod),
        "?": ("Hjälpmeny", lambda: Hjälp.huvud_hjälp_meny()),
        "0": ("Avsluta", lambda: sys.exit())
    }

    menyloop("Huvudmeny", huvudmeny)


if __name__ == "__main__":
    main()
