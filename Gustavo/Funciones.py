def ingresar_matriz():
    print("Ingrese los valores de su matriz")
    matriz = []
    for i in range (3):
        listas = []
        for x in range (3):
            n = int(input("Ingrese un numero de 0 al 9: "))
            listas.append(n)
        matriz.append(listas)
    return matriz

def mostrar_matriz(matriz):
    print("Matriz Ingresada:")
    for i in range (3):
        a = matriz[i]
        print(" ".join(map(str,a)))
    print("")
    for i in range (3):
        a = matriz[i]
        for x in range(3):
            print(a[x],end=" ")
        print("")

def suma_total(matriz):
    sumatoria = 0
    for i in range (3):
        sumatoria += sum(matriz[i])
    return sumatoria

def suma_filas_columnas(matriz):
    filas = []
    columnas = []
    for i in range(3):
        f = sum(matriz[i])
        filas.append(f)
    for i in range (3):
        otrasuma = 0
        for x in range(3):
            num = matriz[x][i]
            otrasuma += num 
        columnas.append(otrasuma)
    return filas, columnas

def maximo_minimo(matriz):
    listamax = []
    listamin = []
    for i in range (3):
        lmax = max(matriz[i])
        lmin = min(matriz[i])
        listamax.append(lmax)
        listamin.append(lmin)
    print("Número máximo: {}".format(max(listamax)))
    print("Número minimo: {}".format(min(listamin)))