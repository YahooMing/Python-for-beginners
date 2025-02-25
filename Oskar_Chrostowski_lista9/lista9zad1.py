#Oskar Chrostowski gr.1 zad.1 lista 9

import numpy as np

A=np.array([ [1,2,3,-2,-1],[3,5,5,-3,-9],[2,3,2,0,-8], [2,6,7,-5,1 ], [1,2,6,-4,-10] ])
B=np.array([ [6,2,-5,17,12] ]).T
ODP=np.linalg.solve(A,B)
#print(np.linalg.solve(A,B))
print("x= ",ODP[0])
print("z= ",ODP[1])
print("y= ",ODP[2])
print("t= ",ODP[3])
print("u= ",ODP[4])
