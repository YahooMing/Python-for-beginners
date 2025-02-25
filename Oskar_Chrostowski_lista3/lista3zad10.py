# Oskar Chrostowski gr.1 zad.10 lista 3
lista = []
for x in range(100, 401):
    strink=str(x)
    a = int(strink[0])
    b = int(strink[1])
    c = int(strink[2])
    if a%2 == 0 and b%2 == 0 and c%2 == 0 :
       lista.append(x)
print(lista) #elementy naturalnie są oddzielone przecinkami
