#numero Aleatorio con limite de intentos de 3 minimos
import random
#Creamos numeros aleatorios entre 1 y 100
numaleatorio=random.randint(1,100)
#imprimimos adivida el numero escondido entre 1 y 100
print("adivina el numero escondidio entre 1 y 100 en 3 intentos")
#contador de intentos
intentoss= 1
#mientras intentos sea mayor o igual a tres, le preguntamos un nuevo numero 
while intentoss <= 3:
    print(f"intento N° {intentoss}")
    Nuser=int(input("ingresa un numero "))
    intentoss +=1

    if Nuser < numaleatorio: #si el numero ingresado es menor que el numero escondido, imprimimos que su numero es muy bajo
        print("numero muy bajo,el numero secreto es mayor")
    elif Nuser > numaleatorio: #si el numero ingresado por el usuario es mayor que el numero escondido, imprimimos que su numero es muy alto
        print("numero muy alto, el numero secreto es menor")
    else:
        break
if Nuser==numaleatorio: # si el numero ingresado por el usuario es igual al escondido, imprimimos que adivino y en cuantos intentos 
    print("ADIVINASTES. El numero secreto el cual era ", numaleatorio, " y lo adivinastes en ",intentoss-1, " intentos" )
else: # si se acaban los intentos mostramos el numero secreto
    print(f"NO ADIVINASTES , el numero secreto era {numaleatorio} ")

## Desaroolado por Gerard Mauricio Pacheco Sanchez
#TI 1125758533

    