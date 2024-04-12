#progrgrama de cambio de dinero
monedas=[1, 5, 10]#listado de monedas con la denominacion 1 , 5 y 10
monedasseleccionadas=[]#lista de monedas que necesitas
contadormonedas=0 #contador inicializado en cero para saber la cantidad de monedas que necesitas
dinerouser =int(input("dime un valor que necesitas: "))#pedimos el valor al usuario
usuer=len(monedas) - 1

while dinerouser > 0:# si el valor es mayor a cero se ejecuta el bucle 
    valor = dinerouser - monedas[usuer]
    if valor >= 0:
        dinerouser = valor
        monedasseleccionadas.append(monedas[usuer])
        contadormonedas += 1 #vamos contando la cantidad de monedas
        
    else:
        usuer -= 1
        
 #mostramos al usuario los valores la cantidad y la devolucion       
print("devolucion en monedas:",monedasseleccionadas)   
print("cantidad de monedas que necesitas: ",contadormonedas)

#Desarrollado por Gerard Mauricio Pacheco Sanchez
#TI:1125758533