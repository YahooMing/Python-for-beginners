# Oskar Chrostowski gr.1 zad.1 lista 4
import random

l = int(input('Podaj liczbę elementów w tablicy: '))
lista = [ random.randint(0,9) for i in range(l)]
iloczyn = 1
suma = 0
for j in range(l):
    iloczyn = iloczyn*lista[j]
    suma = suma + lista[j]
print("Suma wynosi: "+str(suma))
print("Iloczyn wynosi: "+str(iloczyn))
print("Wypisanie listy: "+str(lista))
