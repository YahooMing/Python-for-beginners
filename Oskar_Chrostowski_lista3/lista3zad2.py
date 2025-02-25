# Oskar Chrostowski gr.1 zad.2 lista 3
print("Rozwiązanie z wykorzystaniem if: ")

liczba=int(input("Podaj liczbę całkowitą: "))
    
if liczba%2==0:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")


print("Rozwiązanie bez if: ")
typ=("Parzysta","Nieparzysta")
liczba2=int(input("Podaj liczbę całkowitą: "))
print("Liczba jest "+typ[liczba2%2]) #tutaj z liczby parzystej zawsze będzie 0, więc typ[0] to Parzysta, a typ[1] Nieparzysta

    




