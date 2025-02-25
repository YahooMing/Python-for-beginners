# Oskar Chrostowski gr.1 zad.3 lista 3
print("Równanie kwadratowe ax^2 + bx + c = 0 ")
a = float(input("Podaj a: "))
while a == 0:
    a = float(input("Podaj a, które nie jest równe zeru: "))
b = float(input("Podaj b: "))
c = float(input("Podaj c: "))
delta=float(b**2-4*a*c)

if delta<0:
    print("(Delta ujemna) Równanie nie ma pierwiastka")
elif delta==0:
    skrt=float(delta**(1/2))
    pierwiastek=float((-b)/2*a)
    print("(Delta równa zero) Pierwiastek, równania wynosi: "+str(pierwiastek))
else:
    skrt=float(delta**(1/2))
    pierwiastek1=float((-b+skrt)/2*a)
    pierwiastek2=float((-b-skrt)/2*a)
    print("Pierwiastek pierwszy równania wynosi: "+str(pierwiastek1))
    print("Pierwiastek drugi równania wynosi: "+str(pierwiastek2))


