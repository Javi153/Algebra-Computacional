#Javier Jimenez Arenas
import random
def calcula_t(p: int, s: int) -> int: #Funcion para calcular la t del algoritmo de Tonelli-Shanks
    while True:
        g = random.randint(2, p-1) #Probamos g al azar
        if pow(g, (p - 1) // 2, p) == p - 1: #Hasta obtener un resto no cuadrático
            return pow(g, (p - 1) // pow(2, s+1), p) #Una vez encontrado tenemos por el algoritmo que t = g^((p-1)/2^(s+1))

def egcd(a: int, b: int) -> (int, int, int): #Implementamos el algoritmo extendido de euclides para sacar la l de la demostracion de la prop 5.8
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)
    
def sqrt_mod(a: int, p: int, n: int) -> int:
    if a == 0: #Si la entrada es 0 la salida tambien sera 0
        return 0
    pot_p = 0
    k = 0
    while a % p == 0: #Primero sacamos los factores p
        a //= p
        pot_p += 1
    if pot_p % 2 != 0 or pow(a, (p-1)//2, p) != 1: 
        #Si hay un numero par de factores p entonces se puede calcular sqrt(p^2k) = p^k
        #Si es impar entonces no habra solucion
        return None
    r = p - 1
    while r % 2 == 0: #Siguiendo el algoritmo de Tonelli-Shanks quitamos los factores 2 de r
        k += 1
        r //= 2
    x = pow(a, (r+1)//2, p) #Calculamos el primer candidato del algoritmo 
    z = pow(a, r, p) #Calculamos el z del algoritmo
    s = k
    while z != 1: #Aqui entramos en la iteracion del algoritmo de Tonelli-Shanks
        s -= 1
        aux = pow(2, s-1) 
        if pow(z, aux, p) != 1: #El caso para seguir iterando era que z^2^s-1 = -1
            t = calcula_t(p, s) #Buscamos un t que cumpla la condición
            z = (z * pow(t,2,p)) % p #Actualizamos z y x usando el t calculado
            x = (x * t) % p
    pow_p = 1
    for k in range(1, n): #Aqui, implementamos la demostracion de la proposicion 5.8 para extender la solucion para modulo p con exponente mas alto
        pow_p *= p #Aumentamos el grado de p en 1
        t = (x * x - a) // pow_p #Calculamos t sabiendo que x^2 = a (mod p^k), con lo que x^2 - a es divisible por p^k 
        coef = (-2 * x) % p 
        gcd, bez_x, _ = egcd(coef, p) #Usamos el algoritmo extendido de euclides para resolver -2x*l = t (mod p)
        l = (bez_x * t // gcd) % p
        x = (x + pow_p * l) % (pow_p * p) #Actualizamos la solucion para p^(k+1)
    return (x * pow(p, pot_p//2, pow(p, n))) % pow(p, n)
