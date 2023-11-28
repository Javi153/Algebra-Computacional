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

def multiplicar(a, b):           # a,b son listas de digitos "reducidas"
    n = len(a)
    m = len(b)
    c = [0] * (n+m)
    for i in range(n):                                # i = 0,1,...,n-1
        x = 0
        for j in range(m):                            # j = 0,1,...,m-1
            x = c[i+j] + a[i] * b[j] + x
            c[i+j] = x % 10
            x //= 10
        c[i+m] = x
    remover_ceros(c)
    return c

def multiplicar_karatsuba(a, b):
    n = len(a)
    m = len(b)
    if n < m:
        a, b = b, a
        n, m = m, n
    if m <= 10:
        prod = multiplicar(a, b)
    elif m <= n//2:
        c0 = multiplicar_karatsuba(a[:n//2], b)
        c1 = multiplicar_karatsuba(a[n//2:], b)
        c1 = sumar(c1, c0[n//2:])
        if len(c0) < n//2:
            c0 += [0] * (n//2 - len(c0))
        prod = c0[:n//2] + c1
    else:
        c0 = multiplicar_karatsuba(a[:n//2], b[:n//2])
        c2 = multiplicar_karatsuba(a[n//2:], b[n//2:])
        s1 = sumar(a[:n//2], a[n//2:])
        s2 = sumar(b[:n//2], b[n//2:])
        c1 = multiplicar_karatsuba(s1, s2)
        s3 = sumar(c0, c2)
        c1 = restar(c1, s3)
        c1 = sumar(c1, c0[n//2:])
        c2 = sumar(c2, c1[n//2:])
        if len(c0) < n//2:
            c0 += [0] * (n//2 - len(c0))
        if len(c1) < n//2:
            c1 += [0] * (n//2 - len(c1))
        prod = c0[:n//2] + c1[:n//2] + c2
    remover_ceros(prod)
    return prod

def division_y_resto(a, b):  # a,b son listas de digitos "reducidas"
   n = len(a)
   m = len(b)
   if n < m:
      return [], a           # cociente = 0, resto = a
   q = [0] * (n-m+1)         # crear una lista de ceros para el cociente
   while comparar(a, b) >= 0:
      c = 9
      # la siguiente condicion es equivalente a a<b*c*10^(n-m)
      while comparar(a[n-m:], multiplicar(b,[c])) < 0:
         c = c - 1
      if c != 0:
         q[n-m] = c
         a = a[:n-m] + restar(a[n-m:], multiplicar(b,[c]))
         remover_ceros(a)
      elif n > m:
         c = 9
         # la siguiente condicion es equivalente a a<b*c*10^(n-m-1)
         while comparar(a[n-m-1:], multiplicar(b,[c])) < 0:
            c = c - 1
         q[n-m-1] = c
         a = a[:n-m-1] + restar(a[n-m-1:], multiplicar(b,[c]))
         remover_ceros(a)
      n = len(a)
   remover_ceros(q)
   return q, a
