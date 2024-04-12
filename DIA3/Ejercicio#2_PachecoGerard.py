##generardor de contraseñas 
import random #importamos random para que se genere aleatoriamente
NUMEROS = list(range(10))#lista de numeros con un rango de 10 numeros
ABECEDARIO = [chr(numero) for numero in iter(range(97,123))]#convertimos el numero entero que representa el codigo a representar un caracter correspondiente y iteramos es un rango de 97 a 123
ABECEDARIO_MAYUSCULA = [caracter.upper() for caracter in ABECEDARIO]#utilizamos upper para generar las letras en mayusculas y minusculas de acuerdo al caracter en el abecedario
CARACTERES_ESPECIALES = [chr(i) for i in range(32,48)]#convertimos enteros a caracteres correspondientes
def contra():#funcion para el menu
    print("=====Bienvenido al generador de contraseñas===")#damos la bienvenida
    contraseña=True#variable inicializada en verdadero
    while True: #ciclo repetitivo que culminara hasta que el usuario marque la opcion 2 de salir
        print("===NUESTRO MENU===")#opciones de nuestro menu
        print("1_Generar un contraseña nueva")
        print("2_salir")
        oopi=int(input("que quieres hacer: "))#preguntamos al usuario que quiere hacer 
        if oopi==1:#opcion 1 generamos una nueva contraseña
            print("Buena eleccion vamos a generar una nueva contraseña")
            listadeopcionesdelusuario = []#lista de opciones del usuario

            longitudclave = int(input("Ingrese la longitud de la clave: "))#preguntamos la longitud de la contraseña

            opcionusuario = input("Desea que la clave generada tenga numeros(si/no):") #preguntamos si la contraseña va a contener numeros

            if opcionusuario == 'si':#segun la opcion del usuario guardamos o no numeros
                listadeopcionesdelusuario.append(NUMEROS)

            opcionusuario = input("Desea que la clave generada tenga letras del abecedario en minuscula(si/no):")#preguntamos si va a tener letras en minusculas

            if opcionusuario == 'si':#segun la opcion del usuario agregamos a la lista 
                listadeopcionesdelusuario.append(ABECEDARIO)

            opcionusuario = input("Desea que la clave generada tenga letras del abecedario en mayuscula(si/no): ")#preguntamos si va a tener letras en mayusculas

            if opcionusuario == 'si':#segun la opcion del usuario agregamos a la lista 
                listadeopcionesdelusuario.append(ABECEDARIO_MAYUSCULA)

            opcionusuario = input("Desea que la clave generada tenga caracteres especiales(si/no):")#preguntamos si la contraseña tendra caracteres especiiales

            if opcionusuario == 'si':#segun la opcion del usuario agregamos a la lista
                listadeopcionesdelusuario.append(CARACTERES_ESPECIALES)

            if len(listadeopcionesdelusuario) > 0:#devolvemos la longitud de los objetos
                clave = ""

                for i in range(longitudclave):#para i hasta el rango de lalongitud de la clave

                    elemento_de_la_lista = random.choice(listadeopcionesdelusuario)#devolvemos elementos seleccionados aleatoriamente de la lista

                    caracter = random.choice(elemento_de_la_lista)#devolvemos elementos seleccionados aleatoriamente de la lista

                    clave += str(caracter)#clave es igual a la cantidad de caracteres definidos en la lista 

                print(f"Tu claves es:{clave}")#damos el resultado de la contraseña
            else:
                print("no se puede generar su clave porque no introducistes una opcion")#si el usuario no selecciono ninguna opcion 
        elif oopi==2:#salir del programa
            print("Gracias por utilizar el programa")
            break#cerramos el programa
        else:
            print("instrucciones no validas")#si es diferente a 1 o 2 mostramos instrucciones no validas
contra()

    #Desarrolado por Gerard Mauricio Pacheco Sanchez TI=1125758533