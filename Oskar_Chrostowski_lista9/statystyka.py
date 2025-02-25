#Oskar Chrostowski gr.1 zad.2 lista 9

import numpy as np
import os
import sys


dane = []

#W treści zadania zostało napisane że, dane pomiarowe mają być wprowadzane tylko przez te dwie metody, dlatego zakomentowwałem poprzednią "wersje" mojej pracy
if len(sys.argv) == 1:
    plik = sys.stdin
    for line in plik:
        dane.append(int(line))
else:
    type(sys.argv)
    for i in sys.argv[1:]:
        dane.append(int(i))

#if len(sys.argv) == 2:
#    pliczke = sys.argv[1]
#    with open(pliczke, "r") as x:
#        tresc = x.readlines()
#    for arg in tresc:
#        dane.append(int(arg))
#elif len(sys.argv) > 2 and sys.argv[1] == "<":
#    print("Przekierwoanie z pliku")
#    pliczke = sys.argv[2]
#    with open(pliczke,"r") as y:
#        tresc=y.readlines()
#    for arg in tresc:
#        dane.append(int(arg))
#elif len(sys.argv)>2 and sys.argv[2]==",":
#    print("Z pliku po przecinku")
#    for x in range(len(sys.argv)):
#        if x != 0 and x != ",":
#            dane.append(int(sys.argb[x]))
#elif len(sys.argv) > 2:
#    print("Po spacji")
#    for y in range(len(sys.argv)):
#        if y !=0:
#            dane.append(int(sys.argv[i]))


srednia = np.average(dane)
wariacja=np.var(dane)
odchylenie=np.std(dane)
print("Średnia: ",srednia)
print("Wariacja: ",wariacja)
print("Odchylenie standardowe: ",odchylenie)

