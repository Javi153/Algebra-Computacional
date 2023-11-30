#Javier Jimenez Arenas
# algoritmo de Cooley-Tuckey para calcular DFT_n(p)
# n = len(p) debe ser una potencia de 2 y xi debe ser
# una raíz n-ésima primitiva de la unidad
def fft(p, rot):
    n = len(p)
    if n == 1:
        return p
    p_even = [0] * (n//2)
    p_odd  = [0] * (n//2)
    for i in range(n//2):
        p_even[i] = p[2*i]
        p_odd[i]  = p[2*i+1]
    a_even = fft(p_even, (2 * rot) % n)
    a_odd  = fft(p_odd,  (2 * rot) % n)
    a = [0] * n
    for i in range(n//2):
        aux = rotar_lista(a_odd[i], (rot * i) % n)
        a[i]      = [a_even[i][j] + aux[j] for j in range(len(a_even[i]))]
        a[i+n//2] = [a_even[i][j] - aux[j] for j in range(len(a_even[i]))]
    return a

# esta función calcula la transformada inversa
# utilizando que D(xi)^(-1) = 1/n * D(1/xi)
def ifft(a, rot):
    n = len(a)
    p = fft(a, (rot * (len(a) - 1) % n))
    for i in range(n):
        p[i] = [p[i][j] / n for j in range(len(p[i]))]
    return p

def rotar_lista(l: list, n: int) -> list:
    if n > 0:
        return l[len(l) - n : len(l)] + l[0 : len(l) - n]
    else:
        n = -n
        return l[n : len(l)] + l[0 : n]
    
def producto_por_rotaciones(f: list[list], rot: int):
    for i in range(1,len(f)):
        f[i] = rotar_lista(f[i], (rot * i) % len(f))
    return f

def mult_pol_mod(f: list, g: list, p: int) -> list:
    return

def mult_ss_mod(f: list, g: list, k: int, p:int) -> list:
    n = 1 << k
    if k == 0:
        return [(f[0] * g[0]) % p] + ([0] * (n - 1))
    if k % 2 == 0:
        k1 = (k // 2)
        k2 = (k // 2)
        rot = 4
    else:
        k1 = ((k - 1) // 2)
        k2 = ((k + 1) // 2)
        rot = 2
    n1 = 1 << k1
    n2 = 1 << k2
    f_gorro = [0] * n2
    g_gorro = [0] * n2
    for i in range(n2):
        f_gorro[i] = f[i * n1 : (i + 1) * n1] + [0] * n1
        g_gorro[i] = g[i * n1 : (i + 1) * n1] + [0] * n1
    print("ANTES", f_gorro, g_gorro, producto_por_rotaciones(f_gorro, rot), producto_por_rotaciones(g_gorro, rot))
    f_gorro = fft(producto_por_rotaciones(f_gorro, rot), rot)
    g_gorro = fft(producto_por_rotaciones(g_gorro, rot), rot)
    print("DESPUES", f_gorro, g_gorro)
    h_gorro = [0] * n2
    for i in range(n2):
        h_gorro[i] = mult_ss_mod(f_gorro[i], g_gorro[i], k1, p)
    h_gorro = ifft(h_gorro, rot)
    res = [0] * n
    for i in range(n2):
        res[i * n1 : (i + 1) * n1] = h_gorro[i]
    return res