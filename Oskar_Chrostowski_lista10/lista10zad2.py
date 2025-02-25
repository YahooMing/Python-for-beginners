#Oskar Chrostowski gr.1 zad 2 lista 10
from itertools import combinations
from itertools import chain

class Klasa():
    def __init__(self, lista):
        self.lista = lista
    def kombinacje(self):
        kombinacja = [combinations(self.lista, i) for i in range(len(self.lista)+1)]
        zwroc = chain(*kombinacja)
        zwroc = [list(i) for i in zwroc]
        return zwroc
staraLista = ["a","b","c","d"]
nowaLista = Klasa(staraLista)
print("Lista: ",staraLista)
print("Lista z podlistami: ",nowaLista.kombinacje())
