pase=1

def validarOctal(octal):
    
    #octalnum=['0','1','2','3','4','5','6','7']
    for c in octal:    
        if int(c) <=7:
           print ("correcto")
           octal=1
        else:
           print("numero incorrecto")
           octal=0
           break

    return octal

while pase==1:
    octal=input("ingrese un numero en notacion octal")
    if validarOctal(octal)==1:
        print("correcto")
        break
    else:
        print("Ingrese uno VALIDO")
        pase=1

print("",octal)
