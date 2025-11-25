
class Jämför:

    @staticmethod
    def personer_i_båda(reg1, reg2):

        set1 = {(tuple(p.values())) for p in reg1.personer}
        set2 = {(tuple(p.values())) for p in reg2.personer}

        resultat = set1 & set2

        print(f"{'Efternamn':12} {'Förnamn':12} {'Mobil':15} {'Epost':25} {'Adress'}")
        print("=" * 90)

        for förnamn, efternamn, mobil, epost, adress in resultat:
                print(f"{efternamn:12} {förnamn:12} {mobil:15} {epost:25} {adress}")
        print("=" * 90)

    @staticmethod
    def unika_i_något(reg1, reg2):

        set1 = {(tuple(p.values())) for p in reg1.personer}
        set2 = {(tuple(p.values())) for p in reg2.personer}

        resultat = set1 ^ set2

        print(f"{'Efternamn':12} {'Förnamn':12} {'Mobil':15} {'Epost':25} {'Adress'}")
        print("=" * 90)

        for förnamn, efternamn, mobil, epost, adress in resultat:
            print(f"{efternamn:12} {förnamn:12} {mobil:15} {epost:25} {adress}")
        print("=" * 90)

