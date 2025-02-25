# Oskar Chrostowski gr.1 zad.9 lista 3
n = int(input("Podaj liczbę całkowitą n: "))
m = int(input("Podaj liczbę całkowitą m: "))
tablica = []
#wiersz = []
for i in range(m):
    wiersz = [] #tablica "wiersz" została utworzona wewnątrz for ponieważ utworzona przed pętlą sprawiała iż do "tablicy" były dodawane powtórki wierszy
    for j in range(n):
        wiersz.append(i*j)
    tablica.append(wiersz)
    
print(tablica)
