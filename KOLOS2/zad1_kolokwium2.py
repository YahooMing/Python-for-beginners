#Oskar Chrostowski gr.1 zad 1
import numpy as np
import sys

if len(sys.argv) == 2:
    m = sys.argv[1]
elif len(sys.argv) > 2:
    print("ERROR: Nie można podawać więcej niż jeden argument")
    sys.exit()
else:
    print("ERROR: Zabrakło argumentów, prosze spróbować bez znaku <")
    sys.exit()


try:
    n=int(m)
    matrix=[] 
    row=[] 
    for i in range(n): 
        row=[] 
        for j in range(n): 
            row.append(i*j)
        matrix.append(row)
    for i in range(n):
        print()
        for j in range(n):
            print(matrix[i][j],end=" ")
            
        
except:
    print("Dane są niepoprawne")
    sys.exit()
