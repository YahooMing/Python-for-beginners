#Oskar Chrostowski gr.1 zad 4
#MODUŁ

def WordScore(example):
    count=0
    for i in range(len(example)):
        if (
            (example[i] == "a")
            or (example[i] == "e")
            or (example[i] == "i")
            or (example[i] == "o")
            or (example[i] == "u")
            or (example[i] == "y")
            or (example[i] == "ą")
            or (example[i] == "ó")
            or (example[i] == "ę")
        ):
            count += 1
    if count%2==0:
        return 2
    else:
        return 1


def TotalWordScore(zdanie):
    slowa=zdanie.split(" ")
    pkt=0
    for i in range(len(slowa)):
        pkt = pkt+ WordScore(slowa[i])
    return pkt
        
