# Oskar Chrostowski gr.1 zad.7 lista 3
j=0
i=1
n=int(input("Podaj N: "))
if n<0:
    print("Brak indeksu ujemnego")
print(0)
for x in range(0,n):
    i,j = j,i+j
    print(j)
    
