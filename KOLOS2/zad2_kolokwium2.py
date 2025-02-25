#Oskar Chrostowski gr.1 zad 2
import random

lista=[]
def get_random_students(liczba):
    alfabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in range(liczba):
        imieL=[]
        nazwL=[]
        indexL=[]
        for x in range(3):
            losowanko = random.randint(0,len(alfabet)-1)
            imieL.append(alfabet[losowanko])
        imie=str("".join(imieL))
        #print(imie)
        for y in range(5):
            losowanko1 = random.randint(0,len(alfabet)-1)
            nazwL.append(alfabet[losowanko1])
        nazwisko=str("".join(nazwL))
        #print(nazwisko)
        for z in range(6):
            losowanko2=random.randint(0,9)
            losowanko2=str(losowanko2)
            indexL.append(losowanko2)
        index=int(str("".join(indexL)))
        #print(index)
        for o in range(1):
            ocena = random.randint(2,5)
        #print(ocena)
        sztudent=[imie,nazwisko,index,ocena]
        #print(sztudent)
        lista.append(sztudent)




get_random_students(2)
print(lista)
