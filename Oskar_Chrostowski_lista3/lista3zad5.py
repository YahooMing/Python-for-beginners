# Oskar Chrostowski gr.1 zad.5 lista 3
import re
hasełko= input("Wpisz hasło: ")

x = True


while x:  
    if (len(hasełko)<6 or len(hasełko)>16):
        break
    elif not re.search("[a-z]",hasełko):
        break
    elif not re.search("[0-9]",hasełko):
        break
    elif not re.search("[A-Z]",hasełko):
        break
    elif not re.search("[$#@]",hasełko):
        break
    elif re.search("\s",hasełko):
        break
    else:
        print("Dobre hasło")
        x=False
        break

if x:
    print("Niedobre hasło")
