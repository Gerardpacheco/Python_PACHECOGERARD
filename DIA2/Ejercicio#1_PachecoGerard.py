#serie de fibonacci
print("breve explicacion de la secuencia fibonacci:")
print("En matemáticas, la sucesión de Fibonacci (a veces  llamada serie de Fibonacci) es la sucesión infinita de números naturales.La sucesión comienza con los números 0 y 1, y a partir de estos, cada elemento es la suma de los dos anteriores.")

while True:
    n = int(input("Por favor ingresa el número hasta donde se generará la serie Fibonacci: "))
    a = 0
    b = 1
    c = 1
    while c <= n:
        if c % 2 == 1:
            print(a, end=",")
            a += b
        else:
            print(b, end=",")
            b += a 
        c += 1
    jugar_nuevamente = input("\n¿Quieres jugar de nuevo? (si/no): ")
    if jugar_nuevamente.lower() != "si":
        break
        #Desarrolado por Gerard Mauricio Pacheco Sanchez
        #TI 112575853