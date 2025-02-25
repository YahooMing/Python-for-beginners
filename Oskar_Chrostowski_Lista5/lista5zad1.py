# Oskar Chrostowski gr.1 zad.1 lista 5
def funkcja(slowo):
    slownik={
        "pięćdziesiąt": 50,
        "czterdzieści": 40,
        "trzydzieści": 30,
        "dwadzieścia": 20,
        "dziewiętnaście":19,
        "osiemnaście":18,
        "siedemnaście":17,
        "szesnaście":16,
        "piętnaście":15,
        "czternaście":14,
        "trzynaście":13,
        "dwanaście":12,
        "jedenaście":11,
        "dziesięć":10,
        "dziewięć":9,
        "osiem":8,
        "siedem":7,
        "sześć":6,
        "pięć":5,
        "cztery":4,
        "trzy":3,
        "dwa":2,
        "jeden":1,
        "zero":0,
        }
    liczba = 0
    if slowo in slownik:
        liczba = liczba + slownik.get(slowo)
    else:
        slowo = slowo.split(" ")
        if slowo[0] in slownik:
            liczba = liczba + slownik.get(slowo[0])
        if slowo[1] in slownik:
            liczba = liczba + slownik.get(slowo[1])
        if slowo[0] not in slownik:
            print(slowo[0]," nie jest poprawnym słowem określającym liczbę")
        if slowo[1] not in slownik:
            print(slowo[1]," nie jest poprawnym słowem określającym liczbę")
    print(liczba)
        
    
slowo=input('Podaj liczbe słownie: ')
funkcja(slowo)

