# Oskar Chrostowski gr.1 zad.3 lista 4
import math
def funkcja1(stopnie):
    radiany = stopnie*math.pi/180
    print(str(stopnie)," stopni to ",str(radiany)," radianów")
def funkcja2(radiany):
    stopnie = radiany*180/math.pi
    print(str(radiany)," radianów to ",str(stopnie)," stopni")


print('0-Stopnie na radiany')
print('1-Radiany na stopnie')
wybor=int(input('Wybór: '))

if wybor==0:
    stopnie=float(input('Podaj stopnie: '))
    funkcja1(stopnie)
elif wybor==1:
    radiany=float(input('Podaj radiany: '))
    funkcja2(radiany)
