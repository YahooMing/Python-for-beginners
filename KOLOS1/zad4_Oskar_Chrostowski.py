#Zad 4 Oskar Chrostowski
import random

a=int(input('Proszę o podanie pierwszej liczby z zakresu: '))
b=int(input('Proszę o podanie ostatniej liczby z zakresu: '))
rand=random.randint(a,b) #losowa liczba naturalna z przedziału [a,b]


if rand%3==0 and rand%5==0:
    print("SykBzyk")
    print("Liczba bez zmian: ",rand)
elif rand%3==0:
    print("Syk")
    print("Liczba bez zmian: ",rand)
elif rand%5==0:
    print("Bzyk")
    print("Liczba bez zmian: ",rand)
else:
    print("Liczba bez zmian: ",rand)
