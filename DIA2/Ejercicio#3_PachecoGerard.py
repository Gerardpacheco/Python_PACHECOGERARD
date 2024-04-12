#numeros al aleatorios del (1 al 100) con 10 intentos
import random
#Creamos numeros aleatorios entre 1 y 100
numeroo=random.randint(1,100)
#contador de intentos empieza desde 1
intentos=1
print("adivina el numero entre 0 y 100 con 10 intentos") # imprimimos: adivina el numero entre 0 y 100 con 10 intentos
#mientras que el contador sea menor o igual a 10, imprimimos el numero de intento y le pedimos que ingrese un nuevo numero
while <= 10:
    print(f"intento N° {intentos}")
    n=int(input("ingresa un numero "))
    intentos += 1 

    if n < numeroo: #si el numero ingresado es menor que el numero secreto, le decimos que es un numero demasiado bajo
        print("numero demasiado bajo")
    elif n > numeroo: #si el numero ingresado es mayor al numero secreto, le decimos que su numero es muy alto
        print("numero demasiado alto")
    else:
        break 
if n == numeroo: #si el numero ingresado es igual al numero secreto le decimos que adivinastes el numero y en cuantos intentos
    print(f"Adivinastes el numero secreto en ", intentos-1, " intentos")
else: # si se le acaban los intentos, y no logro adivinar  le decimos el numero secreto 
    print(f"No adivinastes, el numero secreto era {numeroo}")
    


#Desarrolado por Gerard Mauricio Pacheco Sanchez
#TI: 1125758533
