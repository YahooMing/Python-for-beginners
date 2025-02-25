# Oskar Chrostowski gr.1 zad.3 lista 5
def funkcja(r):
    suma = 0
    slownik = {
    "M" : 1000,
    "D" : 500,
    "C" : 100,
    "L" : 50,
    "X" : 10,
    "V" : 5,
    "I" : 1
    }
    
    for i in range(len(r)):
        if i == len(r)-1:
            suma = suma + slownik[r[i]]
            return suma
        if slownik[r[i]] < slownik[r[i+1]]:   # Sprawdzenie warunku czy następna cyfra rzymska nie zmniejsza liczby jak np w przypadku IV, czyli 4 a nie 1 i 5
            suma = suma - slownik[r[i]] 
        else:
            suma = suma + slownik[r[i]] 
    return suma

print('''Przypomnienie:
    "M" : 1000
    "D" : 500
    "C" : 100
    "L" : 50
    "X" : 10
    "V" : 5
    "I" : 1 ''')
r= str(input('Podaj liczbę po rzymsku:'))
print(funkcja(r))
