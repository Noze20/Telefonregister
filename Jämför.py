
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

        print(
            f"{'Efternamn':12} {'Förnamn':12} {'Mobil':15} "
            f"{'Epost':25} {'Adress'}")
        print("=" * 90)

        for efternamn, förnamn, mobil, epost, adress in resultat:
            print(f"{efternamn:12} {förnamn:12} {mobil:15} "
                  f"{epost:25} {adress}")
        print("=" * 90)

    @staticmethod
    def unika_i_något(reg1, reg2):
        """
        Jämför två register och ser vilka som finns i något av registrerna.
        Printar ut alla som finns i något med alla kontaktuppgifter.
        """

        upsättning1 = {(tuple(p.values())) for p in reg1.personer}
        uppsättning2 = {(tuple(p.values())) for p in reg2.personer}

        resultat = upsättning1 ^ uppsättning2

        print(f"{'Efternamn':12} {'Förnamn':12} {'Mobil':15} "
              f"{'Epost':25} {'Adress'}")
        print("=" * 90)

        for efternamn, förnamn, mobil, epost, adress in resultat:
            print(f"{efternamn:12} {förnamn:12} {mobil:15} "
                  f"{epost:25} {adress}")
        print("=" * 90)
