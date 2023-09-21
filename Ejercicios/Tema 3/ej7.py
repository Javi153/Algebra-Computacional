#Javier Jimenez Arenas

#Funciones implementadas por el profesor
def remover_ceros(a):             # a = lista de digitos decimales
    n = len(a)
    while n >= 1 and a[n-1] == 0:
        n -= 1
    del a[n:]

def sumar(a, b):             # a,b son listas de digitos "reducidas"
    n = len(a)
    m = len(b)
    if n < m:                # nos aseguramos que a sea el mas largo
        b, a = a, b
        n, m = m, n
    c = [0] * (n+1)          # reservamos espacio suficiente para la suma
    x = 0                    # x es el acarreo, que inicialmente es 0
    i = 0
    while i < m:             # i=0,1,...,m-1
        x = a[i] + b[i] + x
        c[i] = x % 10
        x //= 10
        i += 1
    while i < n:             # i=m,m+1,...,n-1
        x = a[i] + x
        c[i] = x % 10
        x //= 10
        i += 1
    c[n] = x                 # guardamos el ultimo acarreo
    remover_ceros(c)         # eliminamos los ceros a la izquierda
    return c

def comparar(a, b):             # a,b son listas de digitos "reducidas"
    n = len(a)
    m = len(b)
    # si a y b son de distintas longitudes, la comparacion es inmediata,
    # ya que la representacion que usamos no tiene ceros a la izquierda
    if n > m:
        return 1
    if n < m:
        return -1
    # buscamos el menor indice n a partir del cual a y b coinciden
    while n >= 1 and a[n-1] == b[n-1]:
        n -= 1
    if n == 0:
        return 0
    elif a[n-1] > b[n-1]:
        return 1
    else:
        return -1

def restar(a, b):            # a,b son listas de digitos "reducidas"
    n = len(a)
    m = len(b)
    # si se nos asegura que la funcion es llamada con a >= b, las
    # siguientes dos lineas son innecesarias
    if n < m:
        return
    c = [0] * n              # crear c = lista de n ceros
    x = 0                    # inicializar el acarreo x a cero
    i = 0
    while i < m:             # i=0,1,...,m-1
        x = a[i] - b[i] + x
        c[i] = x % 10
        x //= 10
        i += 1
    while i < n:             # i=m,m+1,...,n-1
        x = a[i] + x
        c[i] = x % 10
        x //= 10
        i += 1
    # al igual que dijimos al principio, las siguientes dos lineas
    # son innecesarias si a >= b.
    if x != 0:
        return
    remover_ceros(c)
    return c

#Funciones implementadas por Javier Jimenez Arenas

def mul2(x):
    acarreo = 0
    for i in range(len(x)):
        x[i] = 2 * x[i] + acarreo
        if x[i] >= 10:
            x[i] -= 10
            acarreo = 1
        else:
            acarreo = 0
    if acarreo > 0:
        x.append(1)
    return x

def div2(x):
    acarreo = 0
    for i in range(len(x) - 1, -1, -1):
        aux = x[i] + acarreo
        x[i] = aux // 2
        if aux % 2 == 0:
            acarreo = 0
        else:
            acarreo = 10
    remover_ceros(x)
    return x

def gcd_binario(x,y):
    xespar = not x or x[0] % 2 == 0
    yespar = not y or y[0] % 2 == 0
    if not x:
        m = y
    elif not y:
        m = x
    elif xespar and yespar:
        m = mul2(gcd_binario(div2(x), div2(y)))
    elif xespar:
        m = gcd_binario(div2(x), y)
    elif yespar:
        m = gcd_binario(x, div2(y))
    elif comparar(x, y) == 1:
        m = gcd_binario(y, div2(restar(x, y)))
    else:
        m = gcd_binario(x, div2(restar(y, x)))
    return m


print(gcd_binario([2,5,4,3,2,5], [2,5,6,8]))