import re

def namn_kontroll(svar):

    while True:
        testa_namn = str(input(svar).strip())

        är_okej = (testa_namn
                   .replace("-", "")
                   .replace(" ", "")
                   .replace("'", "")
                   .isalpha()
                   )

        if är_okej:
            return testa_namn
        else:
            print("Ogiltigt namn. Använd bara bokstäver A_Ö, mellanslag, "
                  "bindestreck eller apostrof. Försök igen")
            continue


def telefon_kontrol(svar):

    while True:
        testa_nummer = input(svar).strip()
        mönster = r"^0\d{1,3}[- ]?\d{5,8}$"

        if re.match(mönster, testa_nummer):
            return testa_nummer
        else:
            print("Ogiltligt nummer! Format som stöds är:\n"
                  "07x-xxxxxxx\n"
                  "08-xxxxxxx\n"
                  "0xx-xxxxxxx")


def epost_kontroll(svar):

    while True:
        testa_epost = input(svar).strip().lower()
        mönster = r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$"     # ZeroBounce.net

        if re.match(mönster, testa_epost):
            return testa_epost
        else:
            print("Email adressen är fel, vänligen skriv in igen")


def adress_kontroll(svar):

    while True:
        testa_adress = str(input(svar)).strip()
        mönster = r"^[A-Za-zÅÄÖåäö]+\s+\d+[A-Za-z]?,\s*[A-Za-zÅÄÖåäö]+$"

        if re.match(mönster, testa_adress):
            return testa_adress
        else:
            print("Fel adressformat: Gatunamn nummer, ort")


def skapa_fil_kontroll(svar):

    while True:
        testa_filnamn = str(input(svar).strip())

        är_okej = (testa_filnamn
                   .lower()
                   .replace("-", "")
                   .replace(" ", "")
                   .replace("'", "")
                   .replace("å", "a")
                   .replace("ä", "a")
                   .replace("ö", "o")
                   .isalpha()
                   )

        if är_okej:
            return testa_filnamn
        else:
            print("Felaktigt filnamn")
