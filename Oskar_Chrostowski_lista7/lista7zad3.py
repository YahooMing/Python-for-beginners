#Oskar Chrostowski gr.1 zad 3 lista 7
import random
import time

start= time.time()
def bombelkowe(lista):
  for i in range(len(lista)):
    for j in range(len(lista)-1): #Odpowiada za zmiane elementów i ich porównywanie
      if lista[j] > lista[j+1]:       #Jeśli element jest większy od elementu za nim to zamieni je miejscami
        lista[j], lista[j+1] = lista[j+1], lista[j]
  return lista

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
lista1_s = bombelkowe(lista1)
print("\n Lista 1 posortowana: ",lista1_s)
print("\n \n Lista 2: ",lista2)
lista2_s = bombelkowe(lista2)
print("\n Lista 2 posortowana: ",lista2_s)
print("\n \n Lista 3: ",lista3)
lista3_s = bombelkowe(lista3)
print("\n Lista 2 posortowana: ",lista3_s)
print("\n Czas działania programu: ",(time.time()-start)," s")
        
