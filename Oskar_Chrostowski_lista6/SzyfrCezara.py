#Oskar Chrostowski gr.1 zad.2 lista 6
def szyfr(zdanie,klucz):
    zdanie=list(zdanie)
    for i in range(len(zdanie)):
        kod=ord(zdanie[i])
        if kod>64 and kod<91: #wielkie znaki
            if (kod+klucz)>90:  
                kod-=26
                zdanie[i]=chr(kod+klucz)    
            else: #ustalanie przesuniecia dla klucza
                zdanie[i]=chr(kod+klucz)        
        if kod>96 and kod<123: #małe znaki
            if (kod+klucz)>122:
                kod-=26
                zdanie[i]=chr(kod+klucz)    
            else: #ustalanie przesuniecia dla klucza
                zdanie[i]=chr(kod+klucz)
    for i in range(len(zdanie)):
        zdanie="".join(zdanie)
    return zdanie


def deszyfr(zdanie,klucz):
    zdanie=list(zdanie)
    for i in range(len(zdanie)):
        kod=ord(zdanie[i])
        if kod>64 and kod<91: #wielkie znaki   
            if (kod-klucz)<65:
                kod+=26
                zdanie[i]=chr(kod-klucz)    
            else: #ustalanie przesuniecia dla klucza
                zdanie[i]=chr(kod-klucz) 
        if kod>96 and kod<123:  #małe znaki   
            if (kod-klucz)<97:
                kod+=26
                zdanie[i]=chr(kod-klucz)    
            else: #ustalanie przesuniecia dla klucza
                zdanie[i]=chr(kod-klucz)
    for i in range(len(zdanie)):
        zdanie="".join(zdanie)   
    return zdanie
