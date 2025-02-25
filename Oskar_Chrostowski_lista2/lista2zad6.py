# Oskar Chrostowski gr.1 zad.6 lista 2
import cmath
lista=["Kasia", "Basia","Marek","Darek"]
print("Lista studentów: "+ str(lista))
lista.append("Józek")
print("Z funkcją append: "+str(lista))
ekstend=["Ania","Basia"] #tutaj musiałem stworzyć ekstend po to aby zapobiec iterowaniu 
lista.extend(ekstend)
print("Z funkcją extend: "+str(lista))
lista.sort()
print("Posortowana: "+str(lista))
print("Czwarty student na liście: "+lista[3])
print("Dwóch pierwszych studentów na liście: "+lista[0]+","+lista[1])
print("Dwóch ostatnich studentów na liście: "+lista[-2]+","+lista[-1])
lista.remove("Basia")
lista.remove("Basia")
print("Użycie remove: "+str(lista))
print("Ilość studentów: "+str(len(lista)))
krotka=tuple(lista)
print("Krotka: "+str(krotka))
