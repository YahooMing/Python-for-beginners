#Oskar Chrostowski gr.1 zad.2 lista 6
import SzyfrCezara  
zdanie=input('Podaj tekst, który ma zostać zaszyfrowany: ')
klucz=int(input('Podaj klucz: '))
klucz=klucz%26
zaszyfr=SzyfrCezara.szyfr(zdanie,klucz)
print("Po zaszyfrowaniu: ",zaszyfr)
odszyfr=SzyfrCezara.deszyfr(zaszyfr,klucz)
print("Po odszyfrowaniu: ",odszyfr)
