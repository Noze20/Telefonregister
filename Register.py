import Kontroll as k
from Person import Person

class Register:
    """
    """

    def __init__(self, registernamn):
        self.registernamn = registernamn
        self.personer: list[Person] = []

    def fil_öppning(self):
        """
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
            print(f"Filen {inmatning} hittades inte")

    def sök_i_registret(self):
        """
        """
        if not self.personer:
            print("Det finns inga personer i detta register")

        sök_efternamn = k.namn_kontroll("Vad heter personen i efternamn? ")
        hittad = False
        rubrik = False

        for p in self.personer:
            if p["efternamn"] == sök_efternamn:
                if rubrik == False:
                    print(f"{'Efternamn':12} {'Förnamn':10} {'Mobil':15} {'Epost':25} {'Adress'}")
                    rubrik = True
                print(f"{p['efternamn']:12} {p['förnamn']:10} {p['mobil']:15} {p['epost']:25} {p['adress']}")
                print("=" * 85)
                hittad = True

        if not hittad:
            print(f"Ingen person med efternamnet {sök_efternamn} hittades")

    def ändra_i_registret(self):
        """"""
        if not self.personer:
            print("Det finns inga i dethär registret att ändra")
            return

        ändra_person_förnamn = input("Ange förnamnet på den du vill ändra: ")
        ändra_person_efternamn = input("Ange efternamnet på den du vill ändra: ")

        for p in self.personer:
            if p["förnamn"] == ändra_person_förnamn and p["efternamn"] == ändra_person_efternamn:
                print("Ändra personens uppgifter. Lämna tomt om du inte vill ändra\n")
                print(f"Efternamn:  {p["efternamn"]}")
                nytt_efternamn = k.namn_kontroll("Nytt efternamn: ")
                print(f"Förnamn:    {p["förnamn"]}")
                nytt_förnamn = k.namn_kontroll("Nytt förnamn: ")
                print(f"Telefon:    {p["mobil"]}")
                nytt_telefonnummer = k.telefon_kontrol("Nytt telefonnummer: ")
                print(f"E-mail:     {p["epost"]}")
                ny_epost = k.epost_kontroll("Ny e-post: ")
                print(f"Adress:     {p["adress"]}")
                ny_adress = k.adress_kontroll("Ny adress: ")

                if nytt_efternamn:
                    p["efternamn"] = nytt_efternamn
                if nytt_förnamn:
                    p["förnamn"] = nytt_förnamn
                if nytt_telefonnummer:
                    p["mobil"] = nytt_telefonnummer
                if ny_epost:
                    p["epost"] = ny_epost
                if ny_adress:
                    p["adress"] = ny_adress

            print(f"Ingen person med namnet: {ändra_person_förnamn} {ändra_person_efternamn}, hittades")

    def lägga_till_i_registret(self):
        """
        """
        print("Ange personuppgifterna: ")
        efternamn = k.namn_kontroll("Efternamn: ")
        förnamn = k.namn_kontroll("Förnamn: ")
        mobil = k.telefon_kontrol("Mobilnummer: ")
        epost = k.epost_kontroll("E-post: ")
        adress = k.adress_kontroll("Adress: ")

        person = {
            "efternamn": efternamn,
            "förnamn": förnamn,
            "mobil": mobil,
            "epost": epost,
            "adress": adress
        }

        for p in self.personer:
            if p["förnamn"] == förnamn and p["efternamn"] == efternamn:
                print("Personen finns redan i registret, testa att ändra uppgifterna istället")
            else:
                self.personer.append(person)
                print(f"{förnamn} {efternamn} har lagts till i {self.registernamn}")

    def ta_bort_från_registret(self):
        """
        """
        if not self.personer:
            print("Det finns inga personer att ta bort från detta registrer")
            return

        ta_bort_förnamn = input("Ange förnamnet du vill ta bort: ")
        ta_bort_efternamn = input("Ange efternamnet du vill ta bort: ")
        for p in self.personer:
            if p["förnamn"] == ta_bort_förnamn and p["efternamn"] == ta_bort_efternamn:
                self.personer.remove(p)
                print(f"{p["förnamn"]} {p["efternamn"]} har tagits bort från {self.registernamn}")
        print(f"Ingen person med namnet: {ta_bort_förnamn} {ta_bort_efternamn}, hittades")

    def sortera_registret(self):
        """
        """
        rubrik = False
        self.personer.sort(key=lambda x: x["efternamn"].lower())
        for p in self.personer:
            if not rubrik:
                print(f"{'Efternamn':12} {'Förnamn':10} {'Mobil':15} {'Epost':25} {'Adress'}")
                print("=" * 90)
                rubrik = True
            print(f"{p['efternamn']:12} {p['förnamn']:10} {p['mobil']:15} {p['epost']:25} {p['adress']}")
        print("=" * 90)

        if not self.personer:
            print("Inga att visa")

    def spara_till_registret(self, registernamn):
        """
        """
        filnamn = registernamn.registernamn + ".txt"

        with open(filnamn, "w", encoding="utf-8") as f:
            for p in self.personer:
                rad = f"{p['efternamn']};{p['förnamn']};{p['mobil']};{p['epost']};{p['adress']}\n"
                f.write(rad)
        print(f"registret sparat i filen {filnamn}")

    def visa_hela_registret(self):
        """"""
        rubrik = False

        for p in self.personer:
            if rubrik == False:
                print(f"{'Efternamn':12} {'Förnamn':10} {'Mobil':15} {'Epost':25} {'Adress'}")
                print("=" * 90)
                rubrik = True
            print(f"{p['efternamn']:12} {p['förnamn']:10} {p['mobil']:15} {p['epost']:25} {p['adress']}")
        print("=" * 90)

        if not self.personer:
            print("Inga att visa")
