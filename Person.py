
class Person:
    """
    Skapar en individ

    Parameters:
        efternamn(str):
        förnamn(str):
        mobil(str):
        epost(str):
        adress(str):
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
