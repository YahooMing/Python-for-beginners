#Oskar Chrostowski zad 2

wybor=int(input("Zamiana Fahrenheita na Celsjusza - wpisz 1.\n Zamiana Celcjusza na Fahrenheita - wpisz 2 \n Wybór: "))
temperatura = float(input("Podaj wartość: "))
if wybor==1 :
    c = 5*(temperatura - 32)/9
    print("Temperatura wynosi ",c," stopni Celcjusza")
elif wybor==2 :
    f = (9*temperatura)/5 +32
    print("Temperatura wynosi",f," stopni Fahrenheita")
else:
    print("Prosze o wybranie 1 albo 2.")
