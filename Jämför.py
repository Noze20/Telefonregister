
# UI blankspace
EFTERNAMN_BLANK = 12
FÖRNAMN_BLANK = 12
MOBIL_BLANK = 15
EPOST_BLANK = 25
N_PRINT = 90


class Jämför:

    @staticmethod
    def personer_i_båda(reg1, reg2):
        """
        Jämför två register och ser vilka personer som finns i båda.
        Printar ut alla som finns i båda med alla kontaktuppgifter.
        """

        upssättning1 = {(tuple(p.values())) for p in reg1.personer}
        uppsättning2 = {(tuple(p.values())) for p in reg2.personer}

        resultat = upssättning1 & uppsättning2

        print(f"\n{'Efternamn':{EFTERNAMN_BLANK}} "
              f"{'Förnamn':{FÖRNAMN_BLANK}} "
              f"{'Mobil':{MOBIL_BLANK}} "
              f"{'Epost':{EPOST_BLANK}} "
              f"{'Adress'}")
        print("=" * N_PRINT)

        for efternamn, förnamn, mobil, epost, adress in resultat:
            print(f"{efternamn:{EFTERNAMN_BLANK}} "
                  f"{förnamn:{FÖRNAMN_BLANK}} "
                  f"{mobil:{MOBIL_BLANK}} "
                  f"{epost:{EPOST_BLANK}} "
                  f"{adress}")
        print("=" * N_PRINT)

    @staticmethod
    def unika_i_något(reg1, reg2):
        """
        Jämför två register och ser vilka som finns i något av registrerna.
        Printar ut alla som finns i något med alla kontaktuppgifter.
        """

        upsättning1 = {(tuple(p.values())) for p in reg1.personer}
        uppsättning2 = {(tuple(p.values())) for p in reg2.personer}

        resultat = upsättning1 | uppsättning2

        print(f"\n{'Efternamn':{EFTERNAMN_BLANK}} "
              f"{'Förnamn':{FÖRNAMN_BLANK}} "
              f"{'Mobil':{MOBIL_BLANK}} "
              f"{'Epost':{EPOST_BLANK}} "
              f"{'Adress'}")
        print("=" * N_PRINT)

        for efternamn, förnamn, mobil, epost, adress in resultat:
            print(f"{efternamn:{EFTERNAMN_BLANK}} "
                  f"{förnamn:{FÖRNAMN_BLANK}} "
                  f"{mobil:{MOBIL_BLANK}} "
                  f"{epost:{EPOST_BLANK}} "
                  f"{adress}")
        print("=" * N_PRINT)
