

class Person:
    """
    Skapar en individ

    Attribut:
    """

    def __init__(self, efternamn, förnamn, mobil, epost, adress):
        self.efternamn = efternamn
        self.förnamn = förnamn
        self.mobil = mobil
        self.epost = epost
        self.adress = adress

    def __str__(self):
        return (f"{self.förnamn}, {self.efternamn}, {self.mobil}, "
                f"{self.epost}, {self.adress}")


class Register:
    """
    Skapar och hanterar ett register

    Attribut:
    """

    def __init__(self, registernamn):
        self.registernamn = registernamn
        self.personer: list[Person] = []

    def fil_öppning(self):
        """
            JOJO
        """
        inmatning = input("Filnamn ").lower()
        filnamn = inmatning + ".txt"

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

                    self.personer.append(ny_person)
        except FileNotFoundError:
            print(f"Filen {filnamn} hittades inte")

    def sök_i_registret(self):
        """
        Metoden låter användaren söka i registret

        Användaren söker på förnamn och efternamn, och utifrån
        det kommer all information upp om personen
        """
        if not self.personer:
            print("Det finns inga personer i detta register")

        sök_efternamn = input("Vad heter personen i efternamn? ")
        for p in self.personer:
            if p.efternamn == sök_efternamn:
                print(f"{p['efternamn']:12} {p['förnamn']:10} {p['mobil']:12} \
                      {p['epost']:25} {p['adress']}")
            print("=" * 80)
        print(f"Ingen person med efternamnet {sök_efternamn} hittades")

    def ändra_i_registret(self):
        """
        Metoden låter användaren ändra uppgifter hos en person

        Användaren söker upp en person den vill ändra på och
        ändrar endast det dem vill
        """

    def lägga_till_i_registret(self):
        """
        Metoden låter användaren lägga till en person i registret

        Användaren skriver in alla uppgifterna om personen
        """
        print("Ange personuppgifterna: ")
        efternamn = input("Efternamn: ").strip()
        förnamn = input("Förnamn: ").strip
        mobil = input("Mobilnummer: ").strip()
        epost = input("E-post: ").strip().lower()
        adress = input("Adress: ").strip

        person = {
            "efternamn": efternamn,
            "förnamn": förnamn,
            "mobil": mobil,
            "epost": epost,
            "adress": adress
        }

        self.personer.append(person)
        print(f"{förnamn} {efternamn} har lagts till")

    def ta_bort_från_registret(self):
        """
        Metoden låter användaren ta bort en person från registret

        Användaren skriven in förnamn och efternamn på personen den vill ta
        bort
        """
        if not self.personer:
            print("Det finns inga personer att ta bort från detta registrer")

        ta_bort_förnamn = input("Ange förnamnet du vill ta bort: ")
        ta_bort_efternamn = input("Ange efternamnet du vill ta bort: ")
        for p in self.personer:
            if p.förnamn == ta_bort_förnamn & p.efternamn == ta_bort_efternamn:
                self.personer.remove(p)
                print(f"{p.förnamn} {p.efternamn} har tagits bort från \
                      {self.registernamn}")
        print(f"Ingen person med namnet: {ta_bort_förnamn} \
              {ta_bort_efternamn}, hittades")

    def sortera_registret(self):
        """
        Metoden låter användaren sortera registret
        Användaren kan välja att sortera i registret baserat på förnamn,
        efternamn, adress
        """
        self.personer.sort(key=lambda x: x["efternamn"].lower())
        print(f"{'Efternamn':12} {'Förnamn':10} {'Mobil':12} \
              {'Epost':25} {'Adress'}")
        print("=" * 80)
        for p in self.personer:
            print(f"{p['efternamn']:12} {p['förnamn']:10} {p['mobil']:12} "
                  f"{p['epost']:25} {p['adress']}")
        print("=" * 80)

    def spara_till_registret(self, filnamn):
        """
            JOJO
        """
        with open(filnamn, "w", encoding="utf-8") as f:
            for p in self.personer:
                rad = f"{p['efternamn']};{p['förnamn']};{p['mobil']};\
                    {p['epost']};{p['adress']}\n"
                f.write(rad)
        print(f"registret sparat i filen {filnamn}")

    def visa_hela_registret(self):
        """"""

        if not self.personer:
            print("Inga att visa")
        else:
            for i, p in enumerate(self.personer, start=1):
                print(f"{i}, {p}")


def main():
    """Main"""

    registernamn = Register(input("Register: ").strip().lower())

    meny_val = {
        "1": ("Öppna fil", registernamn.fil_öppning),
        "2": ("Sök i regitret", registernamn.sök_i_registret),
        "3": ("Ändra i registret", registernamn.ändra_i_registret),
        "4": ("Lägg till i registret", registernamn.lägga_till_i_registret),
        "5": ("Ta bort från registret", registernamn.ta_bort_från_registret),
        "6": ("Sortera registret", registernamn.sortera_registret),
        "7": ("Spara registret", registernamn.spara_till_registret),
        "8": ("Visa alla i registret", registernamn.visa_hela_registret)
    }

    while True:
        print("\n Huvudmeny \n")
        for key, (label, _) in meny_val.items():
            print(f"{key} {label}")
        print("q Avsluta")

        val = input("Val: ").strip().lower()
        if val in meny_val:
            _, func = meny_val[val]
            func()
        elif val == "q":
            print("Avslutar...")
            break
        else:
            print("Ogiltligt val, försök igen!")


if __name__ == "__main__":
    main()
