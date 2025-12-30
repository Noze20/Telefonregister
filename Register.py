import Kontroll as k
from Person import Person


# UI blankspace
EFTERNAMN_BLANK = 12
FÖRNAMN_BLANK = 12
MOBIL_BLANK = 15
EPOST_BLANK = 25
N_PRINT = 90

# Filhantering
KODNING = "utf-8"


class Register:
    """
    Klassen hanterar register som objekt.

    Parameters:
        registernamn: registrets namn
    """

    def __init__(self, registernamn):
        self.registernamn = registernamn
        self.personer: list[Person] = []
        self.öppna_fil_vid_start(registernamn)

    def öppna_fil_vid_start(self, registernamn):
        """
        Öppnar filen kopplad till objektet när någon metod i klassen körs.
        """

        filnamn = registernamn + ".txt"

        try:
            with open(filnamn) as f:
                for rad in f:
                    delar = rad.strip().split(";")

                    if len(delar) != 5:
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
            open(filnamn, "x")

    def rubrik_utskrift(self):
        return (f"\n{'Efternamn':{EFTERNAMN_BLANK}} "
                f"{'Förnamn':{FÖRNAMN_BLANK}} "
                f"{'Mobil':{MOBIL_BLANK}} "
                f"{'Epost':{EPOST_BLANK}} "
                f"{'Adress'}")

    def fil_öppning(self):
        """
        Öppnar en fil så att användaren kan importera ett register.
        """
        inmatning = input("Filnamn ").lower()
        filnamn = inmatning + ".txt"

        try:
            with open(filnamn, encoding=KODNING) as f:
                for rad in f:
                    delar = rad.strip().split(";")

                    if len(delar) != 5:
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
        Låter användaren söka efter en person på efternamn.
        """
        if not self.personer:
            print("Det finns inga personer i detta register")

        sök_efternamn = k.namn_kontroll("Vad heter personen i efternamn? ")
        hittad = False
        rubrik = False

        for p in self.personer:
            if p["efternamn"] == sök_efternamn:
                if rubrik is False:
                    print(self.rubrik_utskrift())
                    rubrik = True
                print(f"{p['efternamn']:{EFTERNAMN_BLANK}} "
                      f"{p['förnamn']:{FÖRNAMN_BLANK}} "
                      f"{p['mobil']:{MOBIL_BLANK}} "
                      f"{p['epost']:{EPOST_BLANK}} "
                      f"{p['adress']}")
                print("=" * N_PRINT)
                hittad = True

        if not hittad:
            print(f"Ingen person med efternamnet {sök_efternamn} hittades")

    def ändra_i_registret(self):
        """
        Låter användaren ändra uppgifter till en person. Användaren behöver
        bara skriva in det dem vill.
        """
        if not self.personer:
            print("Det finns inga i dethär registret att ändra")
            return

        ändra_person_förnamn = input("Ange förnamnet på den du vill ändra: ")
        ändra_person_efternamn = input("Ange efternamnet på den du vill ändra: ")

        for p in self.personer:
            if (p["förnamn"] == ändra_person_förnamn
                    and p["efternamn"] == ändra_person_efternamn):
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

        print(f"Ingen person med namnet: {ändra_person_förnamn} "
              f"{ändra_person_efternamn}, hittades")

    def lägga_till_i_registret(self):
        """
        Lägger till en person i registret
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
                print("Personen finns redan i registret, testa att ändra "
                      "uppgifterna istället")
            else:
                self.personer.append(person)
                print(f"{förnamn} {efternamn} har lagts till i "
                      f"{self.registernamn}")

    def ta_bort_från_registret(self):
        """
        Låter användaren ta bort en person från registret.
        """
        if not self.personer:
            print("Det finns inga personer att ta bort från detta registrer")
            return

        ta_bort_förnamn = input("Ange förnamnet du vill ta bort: ")
        ta_bort_efternamn = input("Ange efternamnet du vill ta bort: ")
        for p in self.personer:
            if (p["förnamn"] == ta_bort_förnamn
                    and p["efternamn"] == ta_bort_efternamn):
                self.personer.remove(p)
                print(f"{p["förnamn"]} {p["efternamn"]} har tagits bort från "
                      f"{self.registernamn}")
        print(f"Ingen person med namnet: {ta_bort_förnamn} "
              f"{ta_bort_efternamn}, hittades")

    def sortera_registret(self):
        """
        Låter användaren sortera registret på efternamn.
        """
        rubrik = False
        self.personer.sort(key=lambda x: x["efternamn"].lower())
        for p in self.personer:
            if not rubrik:
                print(self.rubrik_utskrift())
                print("=" * N_PRINT)
                rubrik = True
            print(f"{p['efternamn']:{EFTERNAMN_BLANK}} "
                  f"{p['förnamn']:{FÖRNAMN_BLANK}} "
                  f"{p['mobil']:{MOBIL_BLANK}} "
                  f"{p['epost']:{EPOST_BLANK}} "
                  f"{p['adress']}")
        print("=" * N_PRINT)

        if not self.personer:
            print("Inga att visa")

    def spara_till_registret(self):
        """
        Låter användaren spara registret till .txt filen.
        """
        filnamn = self.registernamn + ".txt"

        with open(filnamn, "w", encoding=KODNING) as f:
            for p in self.personer:
                rad = f"{p['efternamn']};{p['förnamn']};{p['mobil']};"
                f"{p['epost']};{p['adress']}\n"
                f.write(rad)
        print(f"registret sparat i filen {filnamn}")

    def visa_hela_registret(self):
        """
        Låter användaren se hela registret osorterat.
        """
        rubrik = False

        for p in self.personer:
            if rubrik is False:
                print(self.rubrik_utskrift())
                print("=" * N_PRINT)
                rubrik = True
            print(f"{p['efternamn']:{EFTERNAMN_BLANK}} "
                  f"{p['förnamn']:{FÖRNAMN_BLANK}} "
                  f"{p['mobil']:{MOBIL_BLANK}} "
                  f"{p['epost']:{EPOST_BLANK}} "
                  f"{p['adress']}")
        print("=" * N_PRINT)

        if not self.personer:
            print("Inga att visa")
