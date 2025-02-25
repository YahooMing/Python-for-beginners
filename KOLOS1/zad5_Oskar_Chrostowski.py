#Zad 5 Oskar Chrostowski
def funkcja(tekst):
    znaki = [",",".","!","?"] #znaki niedozwolone
    tekst=tekst.lower() 
    for x in tekst:
        if x in znaki:
            tekst=tekst.replace(x,"") #usuwanie znaków niedozwolonych
    slowko1= tekst.split(" ")
    slowko2 = list(dict.fromkeys(slowko1)) #usuwanie powtórek
    slowko2.sort()
    for i in range(0,len(slowko2)):
        licznik=0;
        for j in range(0,len(slowko1)):
            if slowko2[i]==slowko1[j]:
                licznik=licznik+1
                
        print(slowko2[i],": ",licznik)

tekst = input("Prosze podać zdanie: ")
funkcja(tekst)
