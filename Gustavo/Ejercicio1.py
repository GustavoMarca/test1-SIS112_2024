import Funciones

while True:
    matriz = Funciones.ingresar_matriz()
    print("")
    Funciones.mostrar_matriz(matriz)
    print("")
    print("Suma total de los elementos: {}".format(Funciones.suma_total(matriz)))
    filas, columnas = Funciones.suma_filas_columnas(matriz)
    print("Suma de cada fila: {}".format(filas))
    print("Suma de cada columna: {}".format(columnas))
    print("")
    Funciones.maximo_minimo(matriz)


    opcion = int(input("Cerrar apreta 1, otra vez lo que sea"))
    if opcion == 1:
        break