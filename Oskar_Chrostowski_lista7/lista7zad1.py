#Oskar Chrostowski gr.1 zad 1 lista 7
import time
def forem(n):
    czas = time.time()
    print("Iteracyjnie: ")
    if n==0 or n==1:
        print(n)
    x,y = 0, 1
    for i in range(n-1):
        x,y = y,x+y
        if i==0:
            print(0)
        print(y)
    print("Czas działania: ",(time.time()-czas)," s","\n")
def rekurencyjnie(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    return rekurencyjnie(n-1)+rekurencyjnie(n-2)
def wypisywanie(n):
    print("Rekurencyjnie: ")
    czas = time.time()
    for i in range(n+1):
        print(rekurencyjnie(i))
    print("Czas działania: ",(time.time()-czas)," s","\n")
    

n=int(input('Podaj numer ostatniego elementu szeregu Fibonacciego: '))
forem(n)
wypisywanie(n)

