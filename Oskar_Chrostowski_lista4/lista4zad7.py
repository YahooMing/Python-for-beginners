# Oskar Chrostowski gr.1 zad.7 lista 4
def paskal(n):
   wiersz = [1]
   y = [0]
   for x in range(n):
      print(wiersz)
      wiersz=[l+r for l,r in zip(wiersz+y, y+wiersz)] #funckja zip łączy ze sobą elementy z różnych obiektów iterowalnych

n = int(input("Ile ma być wierszy trójkąta pascala? "))
paskal(n) 
