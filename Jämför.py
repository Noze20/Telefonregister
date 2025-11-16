
class Jämför:
    def __init__(self, register1, register2):
        self.register1 = register1
        self.register2 = register2

    def personer_i_båda(self):
        
        register_dict = {}

        try:
            with open("register.txt") as r:
                for i, rad in enumerate(r, start=1):
                    register_dict[i] = rad.strip()
        except Exception as e:
            print("Fel vid filinläsning", e)

        for i in range(2):
            print("\n===REGISTER===")
            for radnmmer, registernamn in register_dict.items():
                print(f"{radnmmer}: {registernamn}")

            try:
                val = int(input("Välj ett register: "))
            except ValueError:
                print("Ogiltligt val!")

            if val in register_dict:
                registernamn = register_dict[val]
                if i == 1:
                    reg1 = registernamn
                else:
                    reg2 = registernamn
            else:
                print("Ogiltligt val!")
        
        
        
        reg1 = {(p["förnamn"], p["efternamn"]) for p in self.register1}
        reg2 = {(p["förnamn"], p["efternamn"]) for p in self.register2}

        alla = reg1 & reg2

        # Printa ut alla

    def unika_i_något(self):

        reg1 = {(p["förnamn"], p["efternamn"]) for p in self.register1}
        reg2 = {(p["förnamn"], p["efternamn"]) for p in self.register2}
    
        alla = reg1 ^ reg2

        # Printa ut alla
