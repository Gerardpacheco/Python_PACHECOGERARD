def numeros_Primos(nume):#funcion de numeros primos
    if nume <= 2:#si el numero es menor que dos el programa no se ejecuta ya que 1 y 0 son numeros primos
        return False
    for i in range(2,nume):#para i empezando en un rango de dos hasta el numero elegido por el usuario
        if nume % i == 0:#si el residuo de la divicion es cero, eso quiere decir que no es un numero primo
            return False
    return True#si el resultado de la divicion es 1 o el mismo numero decimos que es un numero primo

def MimenuGerard():#funcion de Menu
    print("===========BIENVENIDO===========")  
    while True:#ciclo repetitivo hasta que se cumpla una condicion el cual es la opcion 3 con la finalizacion del programa
        print("==========NUESTRO MENU DE OPCIONES======") #opciones de nuestro Menu
        print("1_verificar si un numero es primo")
        print("2_Informacion sobre los numeros primos")
        print("3_finalizar")
        opc = input("Que quieres hacer ")#preguntamos al usuario que quiere hacer
        
        
        if opc =="1":#si la opcion es igual a 1 le preguntamos el numero que quire saber si es primo
            print("verificar un numero: ")
            nu=int(input("ingresa el numero para verificar "))
            
            if numeros_Primos(nu):#segun el resultado de la funcion damos la respuesta al usuario, si el numero es primo o no
                print("el  numero ",nu, " es un numero primo ")
            else:
                print("el  numero ",nu, "no es un numero primo ")
        elif opc =="2":#opcion 2 informacion sobre los numeros primos y el nombre del autor del aplicativo
            print("infomacion sobre los numeros primos:")
            print("Un número primo es aquel que solo tiene dos divisores que dan otro número natural, sin decimales: el 1 y él mismo. Si se divide por cualquier otro número, obtendríamos un número fraccionario, es decir, una cifra con decimales. ")
            print("Desarrollado por Gerard Mauricio Pacheco sanchez")
        elif opc=="3":#opcion 3 finaliza el programa y da un mensaje de vuelve pronto
            print("programa finalizado")
            print("Vuelve pronto")
            break
        else:
             print("Selecciona una opcion valida")#si marca una opccion invalida le pedimos que por favor marque una opccion valida
MimenuGerard()
#Desarrollado por Gerard Mauricio Pacheco Sancchez TI:1125758533