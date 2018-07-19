 ## Text menu in Python
      
def print_menu():       
    print( 30 * "-" , "MENU" , 30 * "-")
    print ("1. Transformar numeros decimales a otras bases")
    print ("2. Transformar de una base a decimales")
    print ("3. Operaciones Binarias")
    print ("4. Operaciones Octales")
    print ("5. Operaciones Hexadecimales")
    print ("6. Exit")
    print (67 * "-")
  
loop=True

while loop:          
    print_menu()   
    choice = int(input("Enter your choice [1-6]: "))
    def sumar(pbin,sbin):
        suma=pbin+sbin
        return suma
    def restar(pbin,sbin):
        resta=pbin-sbin
        return resta
    def multiplicar(pbin,sbin):
         mult=pbin*sbin
         return mult
    def dividir(pbin,sbin):
        division=pbin//sbin
        return division
    
    if choice==1:     
        print ("Menu 1 ha sido seleccionado : Transformar de decimales a otras bases")
        def decimalabase(decimal,base):
            numero = " "
            sigue = True

            while sigue:
                   cociente = decimal // base
                   residuo = decimal % base
                   #print (" Residuo ", residuo)
                   if residuo>=10 or cociente>=10:
                       decimales = [10, 11, 12, 13, 14, 15]
                       hexadecimal = ["A", "B", "C", "D", "E", "F"]
                       for c in range(7):
                           if residuo == decimales[c - 1]:
                              residuo = hexadecimal[c - 1]

                           if cociente == decimales[c-1]:
                             cociente2 = hexadecimal[c-1]
                   #print("cociente", cociente)
                   decimal = cociente
                   numero = str(residuo) + numero
                   if cociente < base:
                       sigue = False
                       numero = str(cociente) + numero
                       if cociente>=10:
                         numero = str(cociente2) + numero
                   
            return numero
        
        decimal =int ( input ("Digite un numero decimal"))
        base = int(input ("Digite la base"))
        answer = decimalabase(decimal, base)
        print (" El numero decimal : ", str(decimal) + " Pasado a base  " + str(base) + " Es igual a : ", answer)
      

    elif choice==2:
        print ("Menu 2 ha sido seleccionado: Transformar de una base a decimales ")
        def todec():
    
          b = list(a)
          s = 0
          x = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
          for pos, digit in enumerate(b[-1::-1]):
           y = x.index(digit)
           if int(y)/c >= 1:
                  print('Invalid input!!!')
                  break
          s =  (int(y) * (c**pos))+ s
          
          return (s)
        c = int(input('Ingrese la BASE del numero que desea transformar:\t')) 
        a = (input('Then enter the number:\t ')).upper()
        answer=todec()
        print(" respuesta", answer)
        
    elif choice==3:
        print ("Menu 3 ha sido seleccionado: Operaciones Binarias")
        def Decimal(numeroBin):
          numeroBin = str(numeroBin)
          decimal = 0
          exp = len (numeroBin) -1
          for i in numeroBin:
              decimal += (int(i) * 2**(exp))
              exp = exp - 1
          return decimal

        def binarizar(number):
            numero = " "
            sigue = True

            while sigue:
                cociente = number // 2
                residuo = number % 2
                number = cociente
                numero = str(residuo) + numero
                if cociente < 2:
                    sigue = False
                    numero = str(cociente) + numero

            return numero

        def validarbinario1():
            digito=""
    
            while digito != '0' and digito !='1':
              binario =input('Ingrese el primer binario:')
              for digito in binario:
                  if digito != '0' and digito !='1':
 
                      print('error, ingrese de nuevo')
                      break
            return binario 
            print('correcto')
    
        def validarbinario2():
            digito=""
    
            while digito != '0' and digito !='1':
              binario =input('Ingrese el segundo binario:')
              for digito in binario:
                  if digito != '0' and digito !='1':
 
                      print('error, ingrese de nuevo')
                      break
            return binario      
            print('correcto')
            
        numeroBin1=validarbinario1()
        print("bin", numeroBin1)
        numeroBin2=validarbinario2()
        print("bin2", numeroBin2)
        pbin=Decimal(numeroBin1)
        sbin=Decimal(numeroBin2)
        res1=sumar(pbin,sbin)
        res2=restar(pbin,sbin)
        res3=multiplicar(pbin,sbin)
        res4=dividir(pbin,sbin)
        print(Decimal(numeroBin1))
        print(Decimal(numeroBin2))


        print("La suma de los numeros binarios : ",str(numeroBin1)+" y ",str( numeroBin2), " Es :", binarizar(res1))
        print("La resta de los numeros binarios : ",str(numeroBin1)+" y ",str( numeroBin2), " Es :", binarizar(res2))
        print("La multiplicacion de los numeros binarios : ",str(numeroBin1)+" y ",str( numeroBin2), " Es :", binarizar(res3))
        print("La division de los numeros binarios : ",str(numeroBin1)+" y ",str( numeroBin2), " Es :", binarizar(res4))
    elif choice==4:
        print ("Menu 4 ha sido seleccionado: Operaciones Octales ")
        
        def octal_to_decimal(number):
    
            i = 1
            decimal = 0
            while (number != 0):
                remainder = number % 10
                number //= 10
                decimal += remainder * i
                i *= 8  
            return decimal
    
        def octalizar(number):
            numero = " "
            sigue = True

            while sigue:
                cociente = number // 8
                residuo = number % 8
                number = cociente
                numero = str(residuo) + numero
                if cociente < 8:
                     sigue = False
                     numero = str(cociente) + numero

            return numero

        number1=int(input(" Ingrese el primer numero  en notacion octal  "))
        number2=int(input(" Ingrese el segundo numero en notacion octal  "))
        pbin=octal_to_decimal(number1)
        sbin=octal_to_decimal(number2)
        res1=sumar(pbin,sbin)
        res2=restar(pbin,sbin)
        res3=multiplicar(pbin,sbin)
        res4=dividir(pbin,sbin)
        print (" El resultado es : " , octal_to_decimal(number1))
        print (" El resultado es : " , octal_to_decimal(number2))

        print("La suma de los numeros octales : ",str(number1)+" y ",str(number2), " Es :", octalizar(res1))
        print("La resta de los numeros octales : ",str(number1)+" y ",str(number2), " Es :", octalizar(res2))
        print("La multiplicacion de los numeros octales : ",str(number1)+" y ",str( number2), " Es :", octalizar(res3))
        print("La division de los numeros octales : ",str(number1)+" y ",str( number2), " Es :", octalizar(res4))


        
    elif choice==5:
        print ("Menu 5 ha sido seleccionado, Operaciones Hexadecimales")
        def hex2dec(hexa1):
            alist=[]
            n=len(hexa1)
            cont=0
            resultado=0
            valores = {"A" : "10","B" : "11","C" : "12","D" : "13","E" : "14","F" : "15"}
    
            while cont<len(hexa1):
                alist.append(16**(n-1))
                n-=1
                k=int(alist[cont])
        
                if hexa1[cont] in valores:
                    l=hexa1[cont]
                    numero=int(valores.get(l))
                else:
                    numero=int(hexa1[cont])
                resultado+=k*numero
                cont+=1
            return resultado


        def decimalabase(decimal):
            numero = " "
            sigue = True
            i=16
            while sigue:
                cociente = decimal // i
                residuo = decimal % i
                if residuo>=10:
                    decimales = [10, 11, 12, 13, 14, 15]
                    hexadecimal = ["A", "B", "C", "D", "E", "F"]
                    for c in range(7):
                        if residuo == decimales[c - 1]:
                            residuo = hexadecimal[c - 1]
                        if cociente == decimales[c-1]:
                           cociente2 = hexadecimal[c-1]
                #print("cociente", cociente)           
                decimal = cociente
                numero = str(residuo) + numero
                if cociente < i:
                    sigue = False
                    numero = str(cociente) + numero
                    if cociente>=10:
                       numero = str(cociente2) + numero
               
            return numero

        hexa1=input("ingrese un numero en notacion hexadecimal").upper()
        hexa2=input("ingrese un numero en notacion hexadecimal").upper()
        pbin=hex2dec(hexa1)
        sbin=hex2dec(hexa2)
        res1=sumar(pbin,sbin)
        res2=restar(pbin,sbin)
        res3=multiplicar(pbin,sbin)
        res4=dividir(pbin,sbin)
        #print (" el numero : ", hexa1 + " pasado a decimal es : ", resp1)

        print("La suma de los numeros Hexadecimales : ",str(hexa1)+" y ",str(hexa2), " Es :", decimalabase(res1))
        print("La resta de los numeros Hexadecimales : ",str(hexa1)+" y ",str(hexa2), " Es :", decimalabase(res2))
        print("La multiplicacion de los numeros Hexadecimales : ",str(hexa1)+" y ",str(hexa2), " Es :", decimalabase(res3))
        print("La division de los numeros Hexadecimales : ",str(hexa1)+" y ",str( hexa2), " Es :", decimalabase(res4))


        #print (" El numero decimal : ", str(decimal) + " Pasado a base 16 igual a : ", answer)

        
    elif choice==6:
        print (" SALIR   ")
        loop=False 
    else:
        
        print("Wrong option selection. Enter any key to try again..")
