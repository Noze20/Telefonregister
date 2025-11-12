def menyval():

    register = Register(input("Här"))

    HUVUDMENY = {
        "title": "Huvudmeny",
        "choices": {
            "1": ("Välj ett register, skapa ett register eller ta bort ett register", "MENYA1"),
            "B": ("Gå till meny B", "MENYB")
        }

    }

    MENYA1 = {
        "title": "Registermeny",
        "choices": {
            "1": ("")
        }
    }

    MENYA2 = {
        "title": register,
        "choices": {
        "1": ("Sök i registret", register.sök_i_registret),
        "2": ("Lägg till i registret", register.lägga_till_i_registret),
        "3": ("Sortera regisret", register.sortera_registret),
        "4": ("Ändra i reggistret", register.ändra_i_registret),
        "5": ("Ta bort från registret", register.ta_bort_från_registret)
        }
    }

    MENYB = {

    }
