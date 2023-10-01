#Javier Jimenez Arenas
#Para este problema usamos la representacion por digitos decimales que vimos en clase en la que los digitos mas significativos estan mas a la derecha
import natural
import random

def mul2(x):
    acarreo = 0
    for i in range(len(x)): #Recorremos los digitos del manos al mas significativo
        x[i] = 2 * x[i] + acarreo #Multiplicamos el digito por 2 y sumamos el acarreo que haya, que al principio sera 0
        if x[i] >= 10: #Si al multiplicar el digito pasara a valer mas de 10 le restamos 10 y sumamos 1 al acarreo. Como maximo tendremos 2 * 9 + 1 = 19 por tanto el acarreo nunca valdra mas de 1
            x[i] -= 10
            acarreo = 1
        else: #En caso contrario el acarreo sera 0
            acarreo = 0
    if acarreo > 0: #Al salir del bucle añadimos un digito mas si hubiese acarreo en el simbolo mas significativo
        x.append(acarreo)
    natural.remover_ceros(x) #Si hubiese 0 en x los eliminamos
    return x 

def div2(x):
    acarreo = 0
    for i in range(len(x) - 1, -1, -1): #Recorremos los digitos del mas al menos significativo
        aux = x[i] + acarreo #Sumamos al digito el acarreo derivado de la division del digito inmediatamente mas significativo que el
        x[i] = aux // 2 #Dividimos el digito entre 2, quedandonos con su floor
        if aux % 2 == 0: #Si la division no fuese exacta tendra resto 1, pues es la unica posibilidad dividiendo por 2, asi que al proximo digito le sumamos 10
            acarreo = 0
        else:
            acarreo = 10
    natural.remover_ceros(x) #Eliminamos los posibles 0
    return x

def gcd_binario(x: list,y: list) -> list:
    natural.remover_ceros(x) #Eliminamos los 0 redundantes
    if x: #Suponiendo que la lista no es vacia, truncamos el signo del digito mas significativo, aunque en general podriamos suponer que los numeros dados son positivos
        x[len(x) - 1] = abs(x[len(x) - 1])
    natural.remover_ceros(y) #Eliminamos los 0 redundantes
    if y: #Suponiendo que la lista no es vacia, truncamos el signo del digito mas significativo, aunque en general podriamos suponer que los numeros dados son positivos
        y[len(y) - 1] = abs(y[len(y) - 1])
    s = 0 #Este sera el acumulador de potencias de 2, el numero de veces que llamaremos a la funcion mul2
    while x and y: #Mientras x e y no sean 0
        xespar = not x or x[0]&1 == 0 #Seran pares si son listas vacias o si el ultimo digito es par
        yespar = not y or y[0]&1 == 0
        if xespar and yespar:
            s += 1                #Si ambos son pares el gcd es 2 * el gcd de dividir ambos entre 2
            x = div2(x)
            y = div2(y)
        elif xespar:              #Si solo uno es par lo dividimos entre 2 y el gcd no cambia
            x = div2(x)
        elif yespar:
            y = div2(y)
        elif natural.comparar(x, y) == 1: #Si ninguno es par, restamos al mas grande el mas pequeño y calculamos el gcd del resultado con el mas pequeño
            x = div2(natural.restar(x, y))
        else:
            y = div2(natural.restar(y, x))
    if not x:                    # caso base: gcd(0,y)=y
        m = y
        for _ in range(s): #Multiplicamos por 2 tantas veces como lo indique el acumulador s
            m = mul2(m)
    else:                         # caso base: gcd(x,0)=x
        m = x
        for _ in range(s):
            m = mul2(m)
    return m

x = [0, 0, 0]
y = [0, 3, 7, 6, -2, 0, 0]
print(gcd_binario(x, y))