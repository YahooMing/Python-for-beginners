# Oskar Chrostowski gr.1 zad.8 lista 4
n = int(input("Liczba pierwszych elementów ciągu harmonicznego: "))
suma = 0
if (n==1 or n==0):
    print("Suma wynosi ",n)
else:
    for x in range(1,n+1):
        suma = suma + 1/x
    print("Suma ",n," elementów wynosi ",suma)
