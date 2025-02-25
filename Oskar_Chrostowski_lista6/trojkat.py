#moduł trójkąt,  Oskar Chrostowski gr.1 zad.1 lista 6
"""
Ten moduł służy do obliczenia obowodu i pola trójkąta
Dodatkowo podaje informację na temat boków i kątów trójkąta
"""
import math
def obwod(a,b,c):
    return a+b+c

def pole(a,b,c):
    p=(obwod(a,b,c))/2
    return math.sqrt(p*(p-a)*(p-b)*(p-c))

def inf1(a,b,c):
    if a==b and b==c:
        print("Trójkąt jest równoboczny")
    elif a==b or a==c or b==c:
        print("Trójkąt jest równoramienny")
    else:
        print("Trójkąt jest różnoboczny")

def sprawdzenie(d,e,f):
    trojkat=[d,e,f]
    trojkat.sort()
    c= int(trojkat[2])
    a= int(trojkat[1])
    b= int(trojkat[0])
    if c < a+b:
        wykonanie(a,b,c)
    else:
        print("To nie jest trójkąt")
    
def inf2(a,b,c):
    if (a**2) + (b**2) < c**2:
        print("Trójkąt jest rozwartokątny")
    elif (a**2) + (b**2) == c**2:
        print("Trójkąt jest prostokątny")
    else:
        print("Trójkąt jest ostrokątny")

def wykonanie(a,b,c):
    print("Obwod wynosi: ",obwod(a,b,c))
    print("Pole wynosi: ",pole(a,b,c))
    inf1(a,b,c)
    inf2(a,b,c)

