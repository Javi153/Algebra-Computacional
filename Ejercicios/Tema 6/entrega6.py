#Javier Jimenez Arenas
# algoritmo de Cooley-Tuckey para calcular DFT_n(p)
# n = len(p) debe ser una potencia de 2 y xi debe ser
# una raíz n-ésima primitiva de la unidad
def fft(p, rot, q):
    n = len(p)
    if n == 1:
        return p
    p_even = [0] * (n//2)
    p_odd  = [0] * (n//2)
    for i in range(n//2):
        p_even[i] = p[2*i]
        p_odd[i]  = p[2*i+1]
    a_even = fft(p_even, 2 * rot, q)
    a_odd  = fft(p_odd,  2 * rot, q)
    a = [0] * n
    for i in range(n//2):
        aux = rotar_lista(a_odd[i], rot * i, q)
        a[i]      = [(a_even[i][j] + aux[j]) % q for j in range(len(a_even[i]))]
        a[i+n//2] = [(a_even[i][j] - aux[j]) % q for j in range(len(a_even[i]))]
    return a

# esta función calcula la transformada inversa
# utilizando que D(xi)^(-1) = 1/n * D(1/xi)
def ifft(a, rot, k2, q):
    n = len(a)
    p = fft(a, -rot, q)
    for i in range(n):
        p[i] = [(p[i][j] * (1 << (q - 1 - k2))) % q for j in range(len(p[i]))]
    return p

def rotar_lista(l: list, n: int, p: int) -> list:
    if n > 0:
        if n > len(l) and (n // len(l)) % 2 == 1:
            l = [(l[i] * (p - 1)) % p for i in range(len(p))]
        n = n % len(l)
        return [(l[i] * (p - 1)) % p for i in range(len(l) - n, len(l))] + l[0 : len(l) - n]
    elif n < 0:
        if -n > len(l) and (-n // len(l)) % 2 == 1:
            l = [(l[i] * (p - 1)) % p for i in range(len(p))]
        n = -(-n % len(l))
        return l[-n : len(l)] + [(l[i] * (p - 1)) % p for i in range(-n)]
    else:
        return l
    
def producto_por_rotaciones(f: list[list], rot: int, p: int):
    for i in range(1,len(f)):
        f[i] = rotar_lista(f[i], rot * i, p)
    return f

def mult_pol_mod(f: list, g: list, p: int) -> list:
    l = max(len(f), len(g))
    k = 0
    while (1 << k) < len(f) + len(g) - 1:
        k += 1
    l = 1 << k
    f_ext = f + [0] * (l - len(f))
    g_ext = g + [0] * (l - len(g))
    return mult_ss_mod(f_ext, g_ext, k, p)[0:len(f) + len(g) - 1]

def mult_ss_mod(f: list, g: list, k: int, p:int) -> list:
    n = 1 << k
    if k == 0:
        return [(f[0] * g[0]) % p]
    elif k == 1:
        return [(f[0] * g[0] + (p-1) * f[1] * g[1]) % p, (f[1] * g[0] + f[0] * g[1]) % p]
    elif k == 2:
        return [(f[0]*g[0] + (f[1]*g[3] + f[2]*g[2] + f[3] * g[1]) * (p-1)) % p, (f[0]*g[1]+f[1]*g[0]+(f[2]*g[3]+f[3]*g[2])*(p-1)) % p, (f[0]*g[2]+f[1]*g[1]+f[2]*g[0]+(f[3]*g[3])*(p-1)) % p, (f[0]*g[3]+f[1]*g[2]+f[2]*g[1]+f[3]*g[0]) % p]
    if k % 2 == 0:
        k1 = (k // 2)
        k2 = (k // 2)
        rot = 2
    else:
        k1 = ((k - 1) // 2)
        k2 = ((k + 1) // 2)
        rot = 1
    n1 = 1 << k1
    n2 = 1 << k2
    f_gorro = [0] * n2
    g_gorro = [0] * n2
    for i in range(n2):
        f_gorro[i] = f[i * n1 : (i + 1) * n1] + [0] * n1
        g_gorro[i] = g[i * n1 : (i + 1) * n1] + [0] * n1
    f_gorro = fft(producto_por_rotaciones(f_gorro, rot, p), 2 * rot, p)
    g_gorro = fft(producto_por_rotaciones(g_gorro, rot, p), 2 * rot, p)
    h_gorro = [0] * n2
    for i in range(n2):
        h_gorro[i] = mult_ss_mod(f_gorro[i], g_gorro[i], k1+1, p)
    h_gorro = producto_por_rotaciones(ifft(h_gorro, 2 * rot, k2, p), -rot, p)
    res = [0] * n
    res[0: n1] = [(h_gorro[0][j] + (p-1)*h_gorro[n2-1][n1+j]) % p for j in range(n1)]
    for i in range(1, n2):
        res[i * n1 : (i + 1) * n1] = [(h_gorro[i-1][n1 + j] + h_gorro[i][j]) % p for j in range(n1)]
    return res