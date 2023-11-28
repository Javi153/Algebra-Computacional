# este es un ejemplo de librería en la que se definen cuatro funciones:
# raiz_cuadrada, es_primo, primo_siguiente y k_esimo_primo_siguiente.

# esta función calcula la parte entera de la raíz cuadrada de un entero
# x >= 0, utilizando una búsqueda binaria.
def raiz_cuadrada(x):
    izq = 0
    der = x+1
    while izq < der-1:               # buscamos en [izq,der)
        med = (izq+der)//2
        if med*med <= x:
            izq = med
        else:
            der = med
    return izq

# esta función determina la primalidad de n >= 2 comprobando si tiene
# o no divisores en el intervalo [2, raiz_cuadrada(n)].
def es_primo(n):
    r = raiz_cuadrada(n)
    d = 2
    while d <= r:
        if n%d == 0:
            return False
        d += 1
    return True

# esta función devuelve el menor primo mayor que un n >= 1 dado.
def menor_primo_mayor_que(n):
    n += 1
    while not es_primo(n):
        n += 1
    return n

# esta función devuelve el k-ésimo primo mayor que un n >= 1 dado
# para cualquier k >= 1.
def k_esimo_primo_mayor_que(n, k):
    for i in range(k):
        n = menor_primo_mayor_que(n)
    return n
