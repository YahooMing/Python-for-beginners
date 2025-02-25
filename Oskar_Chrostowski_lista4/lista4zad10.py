# Oskar Chrostowski gr.1 zad.10 lista 4
a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))
def fynkcyja(a,b):
    while a!=b:
        if a>b:
            a=a-b
        else:
            b=b-a
    return a
print("Największy wspólny dzielnik ma wartość: ", fynkcyja(a,b))
