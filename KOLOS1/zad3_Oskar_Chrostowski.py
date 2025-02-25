#Zad 3 Oskar Chrostowski
def f(liczba, k1, k2):
    if k1=='cm' and k2=='m': #wypisanie wszystkich możliwości
        wynik=liczba*0.01
    elif k1=='m' and k2=='cm':
        wynik=liczba*100
    elif k1=='cm' and k2=='mm':
        wynik=liczba*10
    elif k1=='m' and k2=='mm':
        wynik=liczba*1000
    elif k1=='mm' and k2=='cm':
        wynik=liczba*0.1
    elif k1=='mm' and k2=='m':
        wynik=liczba*0.001
    print(wynik)
k1=input("Z jakiej miary przechodzimy? (m, cm, mm): ")
k2=input("Na jaką miare przechodzimy? (m, cm, mm): ")
liczba=float(input("Proszę podać liczbę: "))
f(liczba,k1,k2)
