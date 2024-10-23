def kalkulacka():
    print("Jednoduchá kalkulačka")
    print("Vyber operaci:")
    print("1. Sčítání")
    print("2. Odčítání")
    print("3. Násobení")
    print("4. Dělení")

    # Vstup pro uživatele
    volba = input("Zadej číslo operace (1/2/3/4): ")

    # Zkontrolujeme, zda byla zadána platná volba
    if volba in ['1', '2', '3', '4']:
        # Vstup pro čísla
        cislo1 = float(input("Zadej první číslo: "))
        cislo2 = float(input("Zadej druhé číslo: "))

        # Provádění operací na základě volby
        if volba == '1':
            vysledek = cislo1 + cislo2
            print(f"Výsledek: {cislo1} + {cislo2} = {vysledek}")
        elif volba == '2':
            vysledek = cislo1 - cislo2
            print(f"Výsledek: {cislo1} - {cislo2} = {vysledek}")
        elif volba == '3':
            vysledek = cislo1 * cislo2
            print(f"Výsledek: {cislo1} * {cislo2} = {vysledek}")
        elif volba == '4':
            if cislo2 != 0:
                vysledek = cislo1 / cislo2
                print(f"Výsledek: {cislo1} / {cislo2} = {vysledek}")
            else:
                print("Chyba: Dělení nulou není možné!")
    else:
        print("Neplatná volba, zkuste to znovu.")

# Spustíme kalkulačku
kalkulacka()
