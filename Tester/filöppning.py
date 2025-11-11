

def filöppning():
    inmatning = input("Filnamn ").lower()
    filnamn = inmatning + ".txt"
    register = []
    
    try:
        with open(filnamn, encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(";")
                
                # Säkerställ att raden innehåller exakt 5 fält
                if len(parts) != 5:
                    print("Felaktig rad, hoppade över:", line)
                    continue

                # Skapa dictionary direkt från listan
                person = {
                    "efternamn": parts[0].strip(),
                    "förnamn": parts[1].strip(),
                    "mobil": parts[2].replace(" ", "").replace("-", ""),
                    "epost": parts[3].strip().lower(),
                    "adress": parts[4].strip()
                }

                # Lägg till personen i registret
                register.append(person)

    except FileNotFoundError:
        print(f"Filen '{filnamn}' hittades inte.")
        exit()

    # --- Sortera registret på efternamn ---
    register.sort(key=lambda x: x["efternamn"].lower())

    # --- Skriv ut registret i snygg tabell ---
    print(f"{'Efternamn':12} {'Förnamn':10} {'Mobil':12} {'Epost':25} {'Adress'}")
    print("=" * 90)
    for person in register:
        print(f"{person['efternamn']:12} {person['förnamn']:10} {person['mobil']:12} "
            f"{person['epost']:25} {person['adress']}")
    print("=" * 90)


filöppning()

