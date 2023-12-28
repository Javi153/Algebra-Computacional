#Javier Jiménez Arenas
O = (1, 0, 1) #neutro

def points_exh(p: int) -> set[tuple[int, int, int]]: #Calculo de los puntos de la curva de manera exhaustiva con complejidad cuadrática
    res = set()
    for i in range(p):
        for j in range(i, p): #Miramos solo las coordenadas y mayores o iguales que x pues por simetria de x e y sabemos que si (x,y,z) pertenece también lo hará (y,x,z)
            if (pow(i, 3, p) + pow(j, 3, p) - 1) % p == 0:
                res.add((i, j, 1))
                res.add((j, i, 1))
    res.add((1, p-1, 0)) #Añadimos el punto (1,-1,0)
    if p % 3 == 1: #Si existen elementos de orden 3 los calculamos. Sabemos que solo habrá dos elementos de orden 3 y uno es el cuadrado del otro
        for i in range(2, p-1):
            if((pow(i, 3, p) + 1) % p == 0):
                res.add((1, i, 0))
                res.add((1, -pow(i, 2, p) % p, 0))
                return res
    else:
        return res
    
def points_lineal(p: int) -> set[tuple[int, int, int]]: #Calculo de los puntos de la curva con complejidad lineal 
    res = set() #Conjunto resultado
    f_x = {} #Diccionario donde asociamos a cada valor x^3 sus preimagenes
    for i in range(p): #Inicializamos como listas vacias
        f_x[i] = []
    for i in range(p):
        f_x[pow(i, 3, p)].append(i) #Calculamos los valores de f(x)
    for i in range(p): #Para cada valor 1 - c^3 buscamos las x que satisfacen el valor de c^3 y añadimos el punto correspondiente 
        for j in f_x[(1 - pow(i, 3, p)) % p]:
            res.add((j, i, 1))
    res.add((1, p-1, 0)) #Añadimos el punto (1, -1, 0)
    if p % 3 == 1: #Si hay elementos de orden 3 los calculamos
        for i in range(2, p-1):
            if((pow(i, 3, p) + 1) % p == 0):
                res.add((1, i, 0))
                res.add((1, -pow(i, 2, p) % p, 0))
                return res
    else:
        return res
    
            
def points(p: int) -> set[tuple[int, int, int]]: #Funcion que devuelve el conjunto de puntos de la curva
    return points_lineal(p)

def ast(P: tuple[int, int, int], Q: tuple[int, int, int], p: int) -> tuple[int, int, int]: #Funcion que implementa la operacion * en la curva
    if Q == O and P != O: #Cada formula y cada caso se han deducido teóricamente sobre el papel, Se hace especial hincapié en los casos en que algun punto o ambos contiene un 0,
                          #pues son casos especiales a tratar aparte que se comportan de manera distinta al resto de punto por su relacion especial con los puntos (1, a, 0) 
        aux = P
        P = Q
        Q = aux
    if P == Q and (P[2] == 0 or P[1] == 0 or P[0] == 0): 
        return P
    elif P == Q:
        if pow(P[0], 3, p) == pow(P[1], 3, p):
            return (1,(-1 * pow(P[0], 2, p) * pow(P[1], -2, p)) % p,0)
        else:
            x = (-1 * (3 * pow(P[0], 4, p) * pow(pow(P[1], 3, p) - pow(P[0], 3, p), -1, p) + 2 * P[0])) % p
            return (x, ((1 - pow(P[0], 2, p) * x) * pow(P[1], -2, p)) % p, 1)
    elif p % 3 == 2: #Distinguimos el caso de que p = 2 mod 3 y p = 1 mod 3, pues en el segundo caso hay que tener mas cuidado por la mayor cantidad de puntos de inflexion que se comportan de manera especial
        if P[2] == 0:
            return (Q[1], Q[0], 1)
        elif Q[2] == 0:
            return (P[1], P[0], 1)
        elif P[0] == Q[1] and Q[0] == P[1]:
            return (1, p-1, 0)
        elif P == O:
            return (pow(Q[0], -1, p), (-Q[1] * pow(Q[0], -1, p)) % p, 1)
        else:
            suma1 = P[0] * pow(Q[0], 2, p) + P[1] * pow(Q[1], 2, p)
            suma2 = pow(P[0], 2, p) * Q[0] + pow(P[1], 2, p) * Q[1]
            if (suma1 - suma2) % p == 0:
                return (1, p-1, 0) 
            t = (suma1 - 1) * pow(suma1 - suma2, -1, p) #Formula general usando la tercera raiz de F(r(t)) donde r(t) = t * P + (1-t) * Q
            return ((P[0] * t + Q[0] * (1 - t)) % p, (P[1] * t + Q[1] * (1 - t)) % p, (P[2] * t + Q[2] * (1 - t)) % p)
    elif p % 3 == 1: #La mayoria de casos se dan por los 9 puntos de inflexion y su relacion entre ellos, pues no he hayado una formula que incluya todos sus comportamientos
        if P[2] == 0 and Q[2] == 0: #Se que el codigo con tantos casos no es nada bonito pero no he encontrado otra manera de hacerlo ni he hayado la transformacion en la forma de Weierstrass
            if P[1] == p - 1:
                return (1, -pow(Q[1], 2, p) % p, 0)
            elif Q[1] == p-1:
                return (1, -pow(P[1], 2, p) % p, 0)
            else:
                return (1, p-1, 0)
        elif P[1] == 0 and Q[1] == 0:
            if P[0] == 1:
                return (pow(Q[0], 2, p) % p, 0, 1)
            elif Q[0] == 1:
                return (pow(P[0], 2, p) % p, 0, 1)
            else:
                return (1, 0, 1)
        elif P[0] == 0 and Q[0] == 0:
            if P[1] == 1:
                return (0, pow(Q[1], 2, p) % p, 1)
            elif Q[1] == 1:
                return (0, pow(P[1], 2, p) % p, 1)
            else:
                return (1, 0, 1)
        elif P[0] == 0 and Q[2] == 0 or P[2] == 0 and Q[0] == 0:
            if P[1] == (-Q[1]) % p:
                return O
            elif P[1] == 1:
                return (pow(Q[1], 2, p), 0, 1)
            elif Q[1] == 1:
                return (pow(P[1], 2, p), 0, 1)
            elif P[2] == 0:
                return ((-P[1]) % p, 0, 1)
            else:
                return ((-Q[1]) % p, 0, 1)
        elif P[2] == 0 and Q[1] == 0 or P[1] == 0 and Q[2] == 0:
            if P == O:
                return (0, (-Q[1]) % p, 1)
            elif Q == O:
                return (0, (-P[1]) % p, 1)
            elif P[1] == p-1:
                return (Q[1], Q[0], 1)
            elif Q[1] == p-1:
                return (P[1], P[0], 1)
            elif P[0] == (-Q[1]) % p or P[1] == (-Q[0]) % p:
                if P[0] != 1:
                    return (P[1], P[0], P[2])
                else:
                    return (Q[1], Q[0], Q[2])
            else:
                return (0,1,1)
        elif P[0] == 0 and Q[1] == 0 or P[1] == 0 and Q[0] == 0:
            if P == O:
                return (1, (-Q[1]) % p, 0)
            elif Q == O:
                return (1, (-P[1]) % p, 0)
            elif P == (0,1,1):
                return (1, -pow(Q[0], 2, p) % p, 0)
            elif Q == (0,1,1):
                return (1, -pow(P[0], 2, p) % p, 0)
            elif P[0] == Q[1] and Q[1] == P[0]:
                return (1, p-1, 0)
            elif P[0] != 0:
                return (1, (-P[0]) % p, 0)
            else:
                return (1, (-Q[0]) % p, 0)
        elif P[2] == 0 or Q[2] == 0:
            if P[2] == 0:
                aux = P
                P = Q
                Q = aux
            tmp = pow(P[0], 2, p) - P[0] + pow(P[1], 2, p) * Q[1] - P[1] * pow(Q[1], 2, p)
            if tmp % p == 0:
                return ((P[0] - Q[0]) % p, (P[1] - Q[1]) % p, 1)
            t = (-1 * ((P[0] + P[1] * pow(Q[1], 2, p)) * pow(tmp, -1, p))) % p #Formula general usada para los casos en los que hay puntos de la recta del infinito (z = 0)
            x = (P[0] * t + 1 - t) * pow(t, -1, p) % p
            y = (P[1] * t + Q[1] * (1-t)) * pow(t, -1, p) % p
            return (x, y, 1)
        elif P[0] == Q[1] and Q[0] == P[1] and P[2] == 1 and Q[2] == 1:
            return (1, p-1, 0)
        else:
            suma1 = P[0] * pow(Q[0], 2, p) + P[1] * pow(Q[1], 2, p)
            suma2 = pow(P[0], 2, p) * Q[0] + pow(P[1], 2, p) * Q[1]
            if (suma1 - suma2) % p == 0:
                return (1, ((P[1] - Q[1]) * pow(P[0] - Q[0], -1, p)) % p, 0) #Formula general usando la tercera raiz de F(r(t)) donde r(t) = t * P + (1-t) * Q
            t = (suma1 - 1) * pow(suma1 - suma2, -1, p)
            return ((P[0] * t + Q[0] * (1 - t)) % p, (P[1] * t + Q[1] * (1 - t)) % p, (P[2] * t + Q[2] * (1 - t)) % p)

def inv(P: tuple[int, int, int], p: int) -> tuple[int, int, int]: #Como O es punto de inflexion, (O * O) = O, asi que la formula del inverso queda (O * O) * P = O * P
    return ast(O, P, p)

def add(P: tuple[int, int, int], Q: tuple[int, int, int], p: int) -> tuple[int, int, int]: #Usamos la formula de la adicion P + Q = O * (P * Q)
    return ast(O, ast(P, Q, p), p)

def mul(k: int, P: tuple[int, int, int], p: int) -> tuple[int, int, int]: #Multiplicacion al estilo de la exponenciacion binaria mul(k, P, p) = 2 * mul(k//2, P, p) con un factor mas o no dependiendo de la paridad de k
    if k == 0:
        return O
    elif k == 1:
        return P
    else:
        mitad = mul(k//2, P, p)
        if k % 2 == 0:
            return add(mitad, mitad, p)
        else:
            return add(add(mitad, P, p), mitad, p)
        