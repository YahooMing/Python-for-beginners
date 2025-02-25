# Oskar Chrostowski gr.1 zad.10 lista 2
zakres=[]
for x in range(3,100,3):
    zakres.append(x)
print("Wszystkie wielokrotności liczby trzy: "+str(zakres))
del zakres[5::3]
print("Korzystając z del: "+str(zakres))
print("Średnia arytmetyczna: "+str(sum(zakres)/len(zakres)))
