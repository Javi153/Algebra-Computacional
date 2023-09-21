#Javier Jimenez Arenas
def min_suma_casillas(n, m, a): #Como solo podemos ir hacia abajo o hacia la derecha, la forma de llegar a una casilla
                                #con coste minimo sera precisamente el minimo entre llegar a la casilla de su izquierda y llegar a su casilla superior
    for i in range(n):
        for j in range(m):
            if i != 0 and j != 0: #Si ambas casillas estan disponibles, buscamos el minimo entre estas y lo guardamos sobre la propia matriz
                a[i][j] = min(a[i - 1][j] + a[i][j], a[i][j - 1] + a[i][j])
            elif i != 0: #Si no existe casilla izquierda la unica manera de llegar es ir siempre hacia abajo, asi que el coste sera el de su casilla superior mas el de la propia casilla objetivo
                a[i][j] = a[i - 1][j] + a[i][j]
            elif j != 0: #Un caso analogo al anterior pero esta vez en el caso en el que no existe casilla superior
                a[i][j] = a[i][j-1] + a[i][j]
    return a[n-1][m-1] #Devolvemos el coste minimo en la casilla de mas abajo a la derecha