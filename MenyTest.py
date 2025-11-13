
def menyloop(titel, meny_val):
    """"""
    while True:
        print(f"\n==={titel.upper()}===")
        for nyckel, (metod, _) in meny_val.items():
            print(f"{nyckel} {metod}")
        print("0 tillbaka")

        val = input("Val: ").strip().lower()
        if val in meny_val:
            _, func = meny_val[val]
            func()
        elif val == "0":
            break
        else:
            print("Ogiltiligt val, försök igen!")


def main():
    registernamn = Register(input("Välj ett register att ändra i: ")).strip().lower()

    huvudmeny = {
        "1": ("Välj register", lambda: menyloop("Listmeny", register_meny)), 
        "2": ("Om programmet", lambda: print("TBC")),
        "3": ("Avsluta", lambda: exit())
    }

    register_meny = {{
        "1": ("Öppna fil", registernamn.fil_öppning),
        "2": ("Sök i regitret", registernamn.sök_i_registret),
        "3": ("Ändra i registret", registernamn.ändra_i_registret),
        "4": ("Lägg till i registret", registernamn.lägga_till_i_registret),
        "5": ("Ta bort från registret", registernamn.ta_bort_från_registret),
        "6": ("Sortera registret", registernamn.sortera_registret),
        "7": ("Spara registret", registernamn.spara_till_registret),
        "8": ("Visa alla i registret", registernamn.visa_hela_registret)
    }}

    menyloop("Huvudmeny", huvudmeny)
