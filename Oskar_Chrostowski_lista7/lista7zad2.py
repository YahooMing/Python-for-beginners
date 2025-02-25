#Oskar Chrostowski gr.1 zad 2 lista 7
import random
import time

start= time.time()
def wstawianie(lista):
    for i in range(1, len(lista)):
        temp = lista[i]
        j = i - 1
        while j >= 0 and temp < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = temp


lista1=[]
lista2=[]
lista3=[]
for x in range(0,100):
    lista1.append(random.randint(0,20))
for y in range(0,200):
    lista2.append(random.randint(0,20))
for z in range(0,300):
    lista3.append(random.randint(0,20))
print("Lista 1: ",lista1)
wstawianie(lista1)
print("\n Lista 1 posortowana: ",lista1)
print("\n \n Lista 2: ",lista2)
wstawianie(lista2)
print("\n Lista 2 posortowana: ",lista2)
print("\n \n Lista 3: ",lista3)
wstawianie(lista3)
print("\n Lista 2 posortowana: ",lista3)
print("\n Czas działania programu: ",(time.time()-start)," s")
