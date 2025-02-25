# Oskar Chrostowski gr.1 zad.9 lista 4
n = int(input("N: "))
silnia = 1
lista = [*range(0,n+1)] #tutaj tworzymy listę zawierającą elementy od 0 do n
for x in lista:
    if x==0:
        silnia=1
    else:
        silnia*=x
print("Silnia wynosi: ",silnia)
