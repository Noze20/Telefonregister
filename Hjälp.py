
from pathlib import Path


def huvud_hjälp_meny():
    """
    Huvudhjälp menyn med dictionary för hjälpmenyn.
    Skickar vidare direkt till meny_loop()
    """
    HJÄLP_1 = Path(__file__).parent / "Hjälpmapp" / "hjälp1.txt"
    HJÄLP_2 = Path(__file__).parent / "Hjälpmapp" / "hjälp2.txt"
    HJÄLP_3 = Path(__file__).parent / "Hjälpmapp" / "hjälp3.txt"
    HJÄLP_4 = Path(__file__).parent / "Hjälpmapp" / "hjälp4.txt"

    Huvudmeny = {
        "1": ("Vad kan jag göra med programmet?",
              lambda: hjälp_meny(HJÄLP_1)),
        "2": ("Hur fungerar menyerna i programmet?",
              lambda: hjälp_meny(HJÄLP_2)),
        "3": ("Vad kan jag göra i ett register?",
              lambda: hjälp_meny(HJÄLP_3)),
        "4": ("Hur kan jag jämföra två register?",
              lambda: hjälp_meny(HJÄLP_4))
    }

    meny_loop("Hjälpmeny", Huvudmeny)


def meny_loop(titel, meny_val):
    """
    Menyloop som hanterar en dictionary,
    där nyckel är en tuple av beskrivande text och funktion.

    Args:
        titel(str): Namnet på menyn
        meny_val(dict): uppslagsverk för meny {"str": (text: str, funktion(_): anropsbar)}
    """
    # Printar hjälpmenyn
    while True:
        print(f"\n=== {titel.upper()} ===")
        for nyckel, (text, _) in meny_val.items():
            print(f"{nyckel}. {text}")
        print("X. Tillbaka")

        val = input("Välj: ").strip().upper()

        if val == "X":
            break
        elif val in meny_val:
            _, funktion = meny_val[val]
            funktion()
        else:
            print("Ogiltigt val.")


def hjälp_meny(hjälp):
    """
    Visar upp text från en .txt fil för hjälp av vad som kan göras
    med programmet.

    Args:
        hjälp(Path): .txt-fil från mappen Hjälpmapp
    """
    fil_sök = hjälp
    try:
        with open(fil_sök, "r", encoding="utf-8") as fil:
            innehåll = fil.read()
            print("\n" + innehåll)
    except FileNotFoundError:
        print("Fel har uppstått i programet. Vänligen avsluta och försök igen")
    except Exception as fel:
        print(f"{fel}")


def start_hjälp():
    HJÄLP_START = Path(__file__).parent / "Hjälpmapp" / "hjälp5.txt"

    hjälp_meny(HJÄLP_START)