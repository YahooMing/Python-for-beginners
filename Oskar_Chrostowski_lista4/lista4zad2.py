# Oskar Chrostowski gr.1 zad.2 lista 4
import random

def wycinanie(tab):
    tab1=[]
    for i in tab:
        if i not in tab1:
            tab1.append(i)
    return tab1
    
l = int(input('Podaj liczbę losowych elementów w tablicy: '))
lista = [ random.randint(0,9) for i in range(l)]
print("Lista przed przekształceniem: "+str(lista))
print("Lista po przekształceniu: "+str(wycinanie(lista)))
