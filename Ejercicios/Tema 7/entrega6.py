#Javier Jimenez Arenas
#fft modificada para cuerpos finitos
def fft(p, rot, q):
    n = len(p)
    if n == 1:
        return p
    p_even = [0] * (n//2) #Dividimos el polinomio en terminos de grado par e impar
    p_odd  = [0] * (n//2)
    for i in range(n//2):
        p_even[i] = p[2*i]
        p_odd[i]  = p[2*i+1]
    a_even = fft(p_even, 2 * rot, q)  #Aplicamos recursivamente la fft sobre cada uno con una raiz n//2-esima
    a_odd  = fft(p_odd,  2 * rot, q)
    a = [0] * n
    for i in range(n//2):
        aux = rotar_lista(a_odd[i], rot * i, q) #Multiplicamos el polinomio de terminos impares por las raices correspondientes segun el algoritmo
                                                #En este caso la multiplicacion por raices corresponde a giros una lista que simboliza un polinomio
        a[i]      = [(a_even[i][j] + aux[j]) % q for j in range(len(a_even[i]))] #Recomponemos el polinomio completo con las operaciones del algoritmo original de la fft
        a[i+n//2] = [(a_even[i][j] - aux[j]) % q for j in range(len(a_even[i]))]
    return a

# esta función calcula la transformada inversa
def ifft(a, rot, k2, q):
    n = len(a)
    p = fft(a, -rot, q) #Al igual que en el algoritmo original, usamos la raiz inversa. En este caso corresponde a una rotacion en sentido contrario
    for i in range(n): #En este caso nuestro n sera de la forma 2 ** k2. Por tanto, 1/n en el cuerpo finito será otra cierta potencia de 2, 2 ** s.
                        #Sabiendo que 2 ** (q-1) == 1 mod q y que el orden de 2 es k2+s, entonces (q-1) = (k2+s) + l*(k2+s).
                        #Se tiene entonces que 2 ** (q - 1 - k2) == 2 ** (s + l * (k2 + s)) == 2 ** s mod q. Por tanto es equivalente a multiplicar por el inverso.
        p[i] = [(p[i][j] * (1 << (q - 1 - k2))) % q for j in range(len(p[i]))]
    return p

#Funcion para realizar la rotacion de listas que sustituye a la multiplicacion por raices de la unidad, pues en este caso las raices de la unidad son potencias de u
#Al multiplicar por potencias de u solo se aumenta el grado de los coeficientes
def rotar_lista(l: list, n: int, p: int) -> list:
    if n > 0:
        if n > len(l) and (n // len(l)) % 2 == 1: #Por cada rotacion completa se mantienen los mismos coeficientes pero se cambia el signo
            l = [(l[i] * (p - 1)) % p for i in range(len(p))] #Si el numero de rotaciones completas es par no se hace nada, sino se cambia el signo
        n = n % len(l) #Ahora se rotan los coeficientes segun el resto y se cambia el signo solo de los coeficientes que "se salen" por la derecha
        return [(l[i] * (p - 1)) % p for i in range(len(l) - n, len(l))] + l[0 : len(l) - n]
    elif n < 0: #Si la rotacion es hacia la izquierda hacemos lo mismo en direccion contraria
        if -n > len(l) and (-n // len(l)) % 2 == 1:
            l = [(l[i] * (p - 1)) % p for i in range(len(p))]
        n = -(-n % len(l))
        return l[-n : len(l)] + [(l[i] * (p - 1)) % p for i in range(-n)]
    else: #Si n vale 0 se devuelve la misma lista de entrada
        return l
    
def producto_por_rotaciones(f: list[list], rot: int, p: int): #Dado un polinomio de polinomios, realizamos i rotaciones de rot posiciones para el polinomio en la posicion i
    for i in range(1,len(f)):
        f[i] = rotar_lista(f[i], rot * i, p)
    return f

#Funcion para multiplicar polinomios sin que haya problema de "overflow" del grado
def mult_pol_mod(f: list, g: list, p: int) -> list:
    k = 0
    while (1 << k) < len(f) + len(g) - 1: #Calculamos el grado maximo que puede tener el polinomio resultante
        k += 1
    l = 1 << k
    f_ext = f + [0] * (l - len(f)) #Extendemos los polinomios originales hasta que tengan dicho grado
    g_ext = g + [0] * (l - len(g))
    return mult_ss_mod(f_ext, g_ext, k, p)[0:len(f) + len(g) - 1] #Usamos la funcion de multiplicacion de polinomios modular, pues con el tamaño extendido nos dara el resultado esperado

#Multiplicacion de polinomios de grado <= 2 ** k y resultado mod x ** 2 ** k + 1
def mult_ss_mod(f: list, g: list, k: int, p:int) -> list:
    n = 1 << k
    if k == 0: #Casos base k = 0,1,2
        return [(f[0] * g[0]) % p]
    elif k == 1:
        return [(f[0] * g[0] + (p-1) * f[1] * g[1]) % p, (f[1] * g[0] + f[0] * g[1]) % p]
    elif k == 2:
        return [(f[0]*g[0] + (f[1]*g[3] + f[2]*g[2] + f[3] * g[1]) * (p-1)) % p, (f[0]*g[1]+f[1]*g[0]+(f[2]*g[3]+f[3]*g[2])*(p-1)) % p, (f[0]*g[2]+f[1]*g[1]+f[2]*g[0]+(f[3]*g[3])*(p-1)) % p, (f[0]*g[3]+f[1]*g[2]+f[2]*g[1]+f[3]*g[0]) % p]
    if k % 2 == 0: #Dividimos k en k1 y k2 como se indica en el algoritmo y tomamos la raiz dependiendo de la paridad. 
                    #En este caso solo nos interesa el exponente asociado a u pues será el número de rotaciones
        k1 = (k // 2)
        k2 = (k // 2)
        rot = 2
    else:
        k1 = ((k - 1) // 2) 
        k2 = ((k + 1) // 2)
        rot = 1 
    n1 = 1 << k1 #Calculamos n1 y n2 a partir de k1 y k2
    n2 = 1 << k2
    f_gorro = [0] * n2
    g_gorro = [0] * n2
    for i in range(n2): #Dividimos f y g en n2 polinomios de tamaño 2 * n1 para hacer la transformacion del algoritmo
        f_gorro[i] = f[i * n1 : (i + 1) * n1] + [0] * n1
        g_gorro[i] = g[i * n1 : (i + 1) * n1] + [0] * n1
    f_gorro = fft(producto_por_rotaciones(f_gorro, rot, p), 2 * rot, p) #Calculamos el producto por la tupla de raices y la dft de acuerdo al algoritmo
    g_gorro = fft(producto_por_rotaciones(g_gorro, rot, p), 2 * rot, p)
    h_gorro = [0] * n2
    for i in range(n2): #Para cada componente de tamaño 2 * n1 realizamos la multiplicacion recursivamente
        h_gorro[i] = mult_ss_mod(f_gorro[i], g_gorro[i], k1+1, p)
    h_gorro = producto_por_rotaciones(ifft(h_gorro, 2 * rot, k2, p), -rot, p) #Finalmente realizamos la transformacion inversa y multiplicamos por las raices
    res = [0] * n
    res[0: n1] = [(h_gorro[0][j] + (p-1)*h_gorro[n2-1][n1+j]) % p for j in range(n1)] #Calculamos los coeficientes resultantes aplicando modulo x ** 2 ** k + 1
    for i in range(1, n2):
        res[i * n1 : (i + 1) * n1] = [(h_gorro[i-1][n1 + j] + h_gorro[i][j]) % p for j in range(n1)]
    return res