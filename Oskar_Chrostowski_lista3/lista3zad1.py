# Oskar Chrostowski gr.1 zad.1 lista 3
literka = "literka"

while len(literka)!=1:
    literka = input("Podaj tylko jedną literę: ")
    samogloski=('a', 'e', 'i', 'o','u','ó','y','ą','ę')
    for x in samogloski:
        if x==literka and len(literka)==1:
            print("To samogłoska")
            break
        if x!=literka and len(literka)==1:
            print("To spółgłoska")
            break

    




