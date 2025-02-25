# Oskar Chrostowski gr.1 zad.2 lista 5
def funkcja(liczba):
    slownik={
        "tysiąc":1000,
        "dziewięćset":900,
        "osiemset":800,
        "siedemset":700,
        "sześćset":600,
        "pięćset":500,
        "czterysta":400,
        "trzysta":300,
        "dwieście":200,
        "sto":100,
        "dziewięćdziesiąt":90,
        "osiemdziesiąt":80,
        "siedemdziesiąt":70,
        "sześćdziesiąt":60,
        "pięćdziesiąt":50,
        "czterdzieści":40,
        "trzydzieści":30,
        "dwadzieścia":20,
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
        "":0,
        }
    slownie = str(liczba)
    dlugosc = int(len(slownie))
    if dlugosc == 1:
        if liczba == 0:
            print("zero")
        else:
            print(list(slownik.keys())[list(slownik.values()).index(liczba)])
    if dlugosc == 2 and liczba>=10 and liczba<=20:
        d=int(slownie[0])
        j=int(slownie[1])
        liczba = d*10 + j
        print(list(slownik.keys())[list(slownik.values()).index(liczba)])
    if dlugosc == 2 and liczba>20:
        d=int(slownie[0])*10
        j=int(slownie[1])
        print(list(slownik.keys())[list(slownik.values()).index(d)]," ",list(slownik.keys())[list(slownik.values()).index(j)])
    if dlugosc == 3:
        s=int(slownie[0])*100
        d=int(slownie[1])*10
        j=int(slownie[2])
        if (d+j)>=10 and (d+j)<=20:
            print(list(slownik.keys())[list(slownik.values()).index(s)]," ",list(slownik.keys())[list(slownik.values()).index(d+j)])
        else:
            print(list(slownik.keys())[list(slownik.values()).index(s)]," ",list(slownik.keys())[list(slownik.values()).index(d)]," ",list(slownik.keys())[list(slownik.values()).index(j)])
    if dlugosc == 4:
        t=int(slownie[0])*1000
        s=int(slownie[1])*100
        d=int(slownie[2])*10
        j=int(slownie[3])
        if (d+j)>=10 and (d+j)<=20:
            print(list(slownik.keys())[list(slownik.values()).index(t)]," ",list(slownik.keys())[list(slownik.values()).index(s)]," ",list(slownik.keys())[list(slownik.values()).index(d+j)])
        else:
            print(list(slownik.keys())[list(slownik.values()).index(t)]," ",list(slownik.keys())[list(slownik.values()).index(s)]," ",list(slownik.keys())[list(slownik.values()).index(d)]," ",list(slownik.keys())[list(slownik.values()).index(j)])
        
liczba=int(input('Podaj liczbe: '))
funkcja(liczba)




    
