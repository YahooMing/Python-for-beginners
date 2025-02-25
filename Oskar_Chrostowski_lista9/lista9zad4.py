#Oskar Chrostowski gr.1 zad.4 lista 9
import matplotlib.pyplot as plt

y = [16.36 , 16.25 , 12.91, 12.21 , 5.73, 4.64, 2.87, 2.50, 1.60, 1.39 ]
x= ["Python", "C", "C++", "Java", "C#", "Visual basic", "JavaScript", "SQL", "Assembly Language", "PHP"]
#Tutaj próbowwałem zrobić tak, aby wykresy nie nachodziły na siebie, aczkolwiek wygląda to jeszcze gorzej niż gdy nazwy na siebie nachodzą.
#z= [0,50,101,150,201,250,301,350,400,451]
#plt.bar(z,y)
#plt.xticks(z,x) 
plt.bar(x,y)
#Aby tytuły wykresów na siebie nie najeżdżały trzeba zmaksymalizować okno wykresów.
plt.title("Wykres słupkowy pokazujący popularność języków programowania")
plt.xlabel("Jezyk programowania")
plt.ylabel("Procent popularności")
plt.show()
