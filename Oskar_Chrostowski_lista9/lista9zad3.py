#Oskar Chrostowski gr.1 zad 3 lista 9
import numpy as np
import matplotlib.pyplot as plt
import math

v0=float(input("Podaj prędkość początkową: "))
alfa=float(input("Podaj kąt rzutu: "))

alfa = math.radians(alfa)
Hmax= v0 * v0 * math.sin(alfa) * math.sin(alfa) / 2*9.81
Z = v0 * v0 *2* math.sin(alfa) * math.cos(alfa) / 9.81
T= 2*v0 *math.sin(alfa) / 9.81
print("Wysokość maksymalna: ",Hmax)
print("Zasięg rzutu: ",Z)
print("Czas lotu: ",T)


#Predkosc chwilowa w kierunku pionowym i poziomym po czasie
czas= np.linspace(0,T,100)
vy0 = math.sin(alfa) * v0
vx = math.sin(alfa) * v0
vx2 = np.linspace(vx,vx,100)
vy = np.abs(vy0 - 9.81*czas)

plt.subplot(1, 3, 1)
plt.title("Wykres predkosci od czasu")
plt.plot(czas,vy, label="Vy(t)")
plt.plot(czas,vx2, label="Vx(t)")
plt.legend()
#Aby tytuły wykresów na siebie nie najeżdżały trzeba zmaksymalizować okno wykresów.
plt.subplot(1,3,2)
plt.title("Wykres położenia od czasu")
X = vx*czas
Y = vy0*czas - (9.81*czas**2)/2
plt.plot(czas,X, label="x(t)")
plt.plot(czas,Y, label="y(t)")
plt.legend()

plt.subplot(1,3,3)
plt.title("Tor rzutu ukośnego")
plt.plot(X,Y, label="y(x)")
plt.legend()
plt.show()
