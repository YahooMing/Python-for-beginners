#Oskar Chrostowski gr.1 zad 1 lista 10
import math


class Kolo:
    def __init__(self, r):
        self.r = r
    def pole(self):
        return math.pi * self.r * self.r
    def obwod(self):
        return 2* math.pi * self.r

r = int(input("Podaj promień koła: "))
noweKolo = Kolo(r)
print("Pole koła wynosi: ",noweKolo.pole())
print("Obwód koła wynosi: ",noweKolo.obwod())
