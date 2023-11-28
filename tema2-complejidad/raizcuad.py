def raiz_cuadrada_muy_lenta(x):  # x >= 0
    y = x
    while y*y > x:
        y -= 1
    return y

def raiz_cuadrada_lenta(x):      # x >= 0
    y = 1
    while y*y <= x:
        y += 1
    return y-1

def raiz_cuadrada(x):            # x >= 0
    izq = 0
    der = x+1
    while izq < der-1:           # buscamos en [izq,der)
        med = (izq+der)//2
        if med*med <= x:
            izq = med
        else:
            der = med
    return izq
