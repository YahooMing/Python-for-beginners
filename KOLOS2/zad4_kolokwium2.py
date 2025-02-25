#Oskar Chrostowski gr.1 zad 4
import math

class FunkcjaKwadratowa:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        
    def discriminant(self):
        return ((self.b)**2) - (4 * self.a * self.c)

    def root1(self):
        if self.discriminant() < 0:
            return None
        else:
            return (-self.b + math.sqrt(self.discriminant())) / (2 * self.a)
    def root2(self):
        if self.discriminant() < 0:
            return None
        else:
            return (-self.b - math.sqrt(self.discriminant())) / (2 * self.a)

    def rozwiaz(self):
        krotka = (self.root1(), self.root2())
        return krotka
    
a = FunkcjaKwadratowa(2,3,-1)

if a.root1()==None and a.root2()==None:
    print("Brak rozwiązań")
else:
    print(a.rozwiaz())
