#Oskar Chrostowski gr.1 zad 3 lista 10
from itertools import combinations

class Klasa():
    lista = []
    def __init__(self, lista):
        self.lista = lista
    def Kombinacje(self):
        kombinacja = list(combinations(self.lista, 3))
        podlisty = []
        for i in kombinacja:
            if sum(i) == 0:
                podlisty.append(list(i))
        return podlisty

staraLista= [1,2,3,4,5,6,-1,-2,-3,-4,-5,-6]
nowaLista = Klasa(staraLista)
print("Lista: ",staraLista)
print("Lista z podlistami: ",nowaLista.Kombinacje())
