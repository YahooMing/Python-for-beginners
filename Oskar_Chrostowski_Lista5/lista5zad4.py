# Oskar Chrostowski gr.1 zad.4 lista 5
klucz_s = {
    "a" : "y",
    "e" : "i",
    "i" : "o",
    "o" : "a",
    "y" : "e"
}
klucz_d = {
    'y': 'a',
    'i': 'e',
    'o': 'i',
    'a': 'o',
    'e': 'y'
}

def szyfrowanie(slowo):
    s = []
    for i in range(len(slowo)):
        if slowo[i] in klucz_s:
            s.append(klucz_s.get(slowo[i]))
        else:
            s.append(slowo[i])
    slowo = "".join(s)
    return slowo

def deszyfrowanie(slowo):
    d = []
    for i in range(len(slowo)):
        if slowo[i] in klucz_d:
            d.append(klucz_d.get(slowo[i]))
        else:
            d.append(slowo[i])
    slowo = "".join(d)
    return slowo






wybor = int(input("Szyfrowanie - wybierz 1, Deszyfrowanie - wybierz 2. Wybranie cokolwiek innego zakończy działanie programu. Wybór: "))

if wybor == 1:
    slowo = list(input('Proszę podać słowo bądź zdanie: '))
    print("Po zaszyfrowaniu: ",szyfrowanie(slowo))
elif wybor == 2:
    slowo = list(input('Proszę podać słowo bądź zdanie: '))
    print("Po odszyfrowaniu: ",deszyfrowanie(slowo))
else:
    print("Program zakończono")
