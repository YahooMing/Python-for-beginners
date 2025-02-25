#Oskar Chrostowski gr.1 zad 1 lista 8

import cezar
import time
import os.path
from datetime import date

dzis = date.today()
rok = str(dzis.year)
miesiac = str(dzis.month)
dzionek = str(dzis.day)
klucz = 11
while (klucz > 10) or (klucz < 1):
    klucz = int(input("Podaj przesunięcie szyfru. Dopuszczalnie od 1 do 10: "))
kluczyk = str(klucz)
sciezka1= input("Podaj ścieżkę, gdzie znajduje sie plik do szyfrowania: ");
plik = input("Podaj nazwę pliku, który ma zostać zaszyfrowany: ");
plik = plik + ".txt"
sciezka2 = input("Podaj ścieżkę, gdzie nowy plik ma zostać stworzony: ");

plikZaszyfr = "plik_zaszyfrowany" + kluczyk + '_' + rok + miesiac + dzionek + ".txt"
try:
    zaszyfr = open(os.path.join(sciezka2,plikZaszyfr),"w+")
    try:
        with open(os.path.join(sciezka1,plik),"r") as f: 
            zaszyfrowany = cezar.szyfrowanie(f.read(), klucz)
            zaszyfr.write(zaszyfrowany)
            print("ZAKOŃCZONO")
    except IOError:
        print("Nie znaleziono pliku o nazwie ", plik)
except IOError:
    print("Nie znaleziono ścieżki.")
zaszyfr.close()
