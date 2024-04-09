#--------------------------------
#--------Dia1 CHEAT SHEET PYTHON-------
#---------------------------------
#imprinir hola mundo
print("hola mundoooooooo !!!!")

#datos primitivos
#numero
numero=10 #definimos
print(numero)#imprimir variable
print(type(numero))

#Decimal
numeritoDecimal = 1.1
print(numeritoDecimal)
print(type(numeritoDecimal))

#Booleano
miBooleanito = True
print(miBooleanito)
print(type(miBooleanito))

#Cadena de texto
texto = "MI TIBU"
print(texto)
print(type(texto))

#ingresa por teclado la informacion(input)
edad=input("ingresa tu edad")
edad=(int (edad))
print("tu edad es: ",edad, "años")

numero=input("ingresa un numero")
numero=(int (numero))
print("tu numero ingresado es ",numero,)


#============conversion de datos primitivos ===
# De string a entero
num1="5"
num2=10
resultado=int(num1)*num2
print(type(resultado))
print(resultado)
#de entero a string
n=5
n=str(n)
print(type(n))
print(n)

#de entero a float
n=5
n=float(n)
print(type(n))
print(n)

#flotante a entero
n=5.0
n=int(n)
print(type(n))
print(n)

# De entero a boolean
n=5
n=bool(n)
print(type(n))
print(n)
# de boolean a entero
Booleano=True
Booleano=int(Booleano)
print(type(Booleano))
print(Booleano)

#========= bucles for y while

#bucle while
contador=0
while contador <5:
    print(contador)
    contador+=1
    print("el contador llego a su numero maximo")

#bucle for 
for i in range(5):
    print(i)
    print("el rango de numeros se ha igualado")

#  ============  funciones 4 tipos ======#
#De parametros con retorno
def multiplicacion(nume1,nume2):
    return nume1*nume2
    multiplicacion(3,5)

#De parametros sin retorno
def multiplicacioon(v1,v2):
    multiplicacioon=(4*5)
    print(multiplicacioon)

#sin parametros ni retorno
def dibienvenido()
print("Bienvenido")
#sin parametros pero con retorno
def saludar():
    return "hola buenos dias"
    saludo=saludar()
    print(saludo)


# Desarrollado pr Gerard Mauricio Pacheco Sanchez TI 1125758533
