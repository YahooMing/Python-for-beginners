# Oskar Chrostowski gr.1 zad.4 lista 4
def funkcja(n,q=2,a=1):
    an = a*q**(n-1)
    return an

n = int(input('N: '))
q = int(input('Q: '))
a= int(input('A: '))
print(funkcja(n,q,a))
