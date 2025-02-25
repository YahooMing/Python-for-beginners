#Oskar Chrostowski gr.1 zad.4 lista 10
from urllib.request import urlopen, Request
from itertools import combinations
from xml.etree.ElementTree import parse, fromstring

class Kursy():
    lista = []
    #Zamiast ścieżki do pliku przekazuje sie link
    def __init__(self, link):
        self.url = urlopen(Request(link)).read()
        self.xml = fromstring(self.url)

    def wyswietlanie(self):
        for item in self.xml.findall('pozycja'):
            waluta = [item.findtext('nazwa_waluty'), item.findtext('przelicznik'), item.findtext('kurs_sredni').replace(",", ".")]
            self.lista.append(waluta)
        print("\t\t\t\tKURS")
        for i in self.lista:
            print(i[0], "\t", i[1], "\t", i[2])

    def polskie(self, waluta, val, przeliczanie):
        for i in self.lista:
            if waluta in i:
                if przeliczanie == "na_zlotowki":
                    wart = float(i[2])*val
                    print(val, waluta, " = ", round(wart, 2), "zlotych")
                elif przeliczanie == "ze_zlotowek":
                    wart = val/float(i[2])
                    print(val, "zlotych = ", round(wart, 2), waluta)

    def przeliczanie(self, waluta1, waluta2, val):
        pierwsza, druga = 0, 0
        for i in self.lista:
            if waluta1 in i:
                pierwsza = val*float(i[2])
            if waluta2 in i:
                druga = float(i[2])
        print(val, waluta1, " = ", round(pierwsza/druga, 2), waluta2)


kantorek = Kursy("https://www.nbp.pl/kursy/xml/a012z210120.xml")
#Podpunkt pierwszy
kantorek.wyswietlanie()
print("\n Przeliczanie")
#Podpunkt drugi
kantorek.polskie('euro', 50, "ze_zlotowek")
kantorek.polskie('korona islandzka', 1, "na_zlotowki")
#Podpunkt trzeci
kantorek.przeliczanie("lej rumuński", "dolar australijski", 100)
kantorek.przeliczanie("kuna (Chorwacja)", "dolar amerykański", 50)
