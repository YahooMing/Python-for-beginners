#Oskar Chrostowski gr.1 zad.3 lista 6
w = input("Podaj liczbe: ")
j = 1
a = ""
for i in range(len(w)):
    if i < len(w)-1:
        if w[i] == w[i+1]:
            j += 1
        else:
            a += str(j) + w[i]
            j = 1
    elif w[i-1] != w[i]:
        a += "1"+w[i]
    elif j >= 1:    # gdy są 2 liczby
        a += str(j) + w[i]
print("look-and-say: ",a)
