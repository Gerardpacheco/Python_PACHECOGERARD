#Ejercicio del banco de monedas
#monedas didponibles en el banco
monedas = [1, 5, 10]
#monto de monedas que necesita el usuario
montoNecesitado = int(input("dime el monto valor que necesitas que te entreguemos "))
#funcion para determinar el monto necesitado en monedas
def valormonedas(montoNecesitado):
    resultado = []#arreglo para guardar el resultado
    for i in monedas:
        if i == montoNecesitado:
            print("Necesitas una moneda de: ",i) #si el monto necesitado por el cliente es igual a alguna moneda le decimo que necesita una moneda de (valor de la moneda)
            exit()     
        cantmonedas_adar = montoNecesitado// i #calculamos la cantida de cada moneda que le vamos a dar 
        if cantmonedas_adar<0:#si la cantidad de monedas que devemos darle es menor a cero salimos del programa
            break
        if cantmonedas_adar !=0: #si la cantida de monedas a dar es diferente de cero guardamos en el arreglo de resultado y mostramos la cantidad de monedas necesitadas y la el valor de la moneda
            resultado.append([cantmonedas_adar, i])

        ordendemonedas = sorted(resultado) #funcion para ordenar el arreglo de menor a mayor 
    for o in ordendemonedas: #bucle para ordenar cada moneda segun la cantidad
        cant = o[0]#cantidad de monedas
        moneda = o[1]#valor de cada moneda
        print("necesitas ",cant," monedas de ",moneda)
        monedasfaltantes = montoNecesitado-(cant*moneda)#calculamos el dinero que falta para lograr el objetivo de llegar al monto necesitado
        if monedasfaltantes>0:#si las monedas que falta es mayor a cero 
            valormonedas(monedasfaltantes)#repetimos el valor monedas hasta monedas faltantes
        else:
            exit()#salimos del programa
valormonedas(montoNecesitado)


#Desarrollado por Gerard Mauricio Pacheco Sanchez
#TI 1125758533