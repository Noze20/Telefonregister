from pathlib import Path


def huvud_hjälp_meny():
    """"""
    Huvudmeny = {
        "1": ("Vad kan jag göra med programmet?", lambda: hjälp_meny_1()),
        "2": ("Hur fungerar menyerna i programmet?", lambda: hjälp_meny_2()),
        "3": ("Vad kan jag göra i ett register?", lambda: hjälp_menny_3())
    }

    meny_loop("Hjälpmeny", Huvudmeny)


def meny_loop(titel, meny_val):
    """"""
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


def hjälp_meny_1():
    """"""
    fil_sök = Path(__file__).parent / "Hjälpmapp" / "hjälp1.txt"
    try:
        with open(fil_sök, "r", encoding="utf-8") as f:
            innehåll = f.read()
            print(innehåll)
    except FileNotFoundError:
        print("Fel har uppstått i programet. Vänligen avsluta och försök igen")
    except Exception as e:
        print(f"{e}")


def hjälp_meny_2():
    """"""
    fil_sök = Path(__file__).parent / "Hjälpmapp" / "hjälp2.txt"
    try:
        with open(fil_sök, "r", encoding="utf-8") as f:
            innehåll = f.read()
            print(innehåll)
    except FileNotFoundError:
        print("Fel har uppstått i programet. Vänligen avsluta och försök igen")
    except Exception as e:
        print(f"{e}")


def hjälp_menny_3():
    """"""
    fil_sök = Path(__file__).parent / "Hjälpmapp" / "hjälp3.txt"
    try:
        with open(fil_sök, "r", encoding="utf-8") as f:
            innehåll = f.read()
            print(innehåll)
    except FileNotFoundError:
        print("Fel har uppstått i programet. Vänligen avsluta och försök igen")
    except Exception as e:
        print(f"{e}")
