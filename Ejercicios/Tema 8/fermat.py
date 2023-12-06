O = (1, 0, 1)

def points_exh(p: int) -> set[tuple[int, int, int]]:
    res = set()
    for i in range(p):
        for j in range(i, p):
            if (pow(i, 3, p) + pow(j, 3, p) - 1) % p == 0:
                res.add((i, j, 1))
                res.add((j, i, 1))
    for i in range(p):
        if (1 + pow(i, 3, p)) % p == 0:
            res.add((1,i,0))
    return res

def inv(P: tuple[int, int, int], p: int, puntos: set[tuple[int, int, int]] = None) -> tuple[int, int, int]:
    if P == O:
        return O
    if puntos == None:
        puntos = points(p)
    for (a, b, c) in puntos:
        if (a, b, c) != P and (a, b, c) != O and (P[1] * c - P[2] * b - P[1] * a + P[0] * b) % p == 0:
            return (a,b,c)
        
def add(P: tuple[int, int, int], Q: tuple[int, int, int], p: int, puntos: set[tuple[int, int, int]] = None) -> tuple[int, int, int]:
    if puntos == None:
        puntos = points(p)
    if P == Q:
        F_P = (3 * pow(P[0], 2, p), 3 * pow(P[1], 2, p), -3 * pow(P[2], 2, p))
        for (a, b, c) in puntos:
            if (a, b, c) != P and (F_P[0] * a + F_P[1] * b + F_P[2] * c) % p == 0:
                return inv((a, b, c), p, puntos)
        return inv(P, p, puntos)
    else:
        for (a, b, c) in puntos:
            if (a, b, c) != P and (a, b, c) != Q and (P[0] * Q[1] * c + P[2] * Q[0] * b + P[1] * Q[2] * a - P[2] * Q[1] * a - P[1] * Q[0] * c - P[0] * Q[2] * b) % p == 0:
                return inv((a,b,c), p, puntos)
        
def mul(k:int, P: tuple[int, int, int], p: int, puntos: set[tuple[int, int, int]] = None) -> tuple[int, int, int]:
    if k == 0:
        return O
    elif k == 1:
        return P
    if puntos == None:
        puntos = points(p)
    mul_mitad = mul(k // 2, P, p, puntos)
    suma = add(mul_mitad, mul_mitad, p, puntos)
    if k % 2 == 0:
        return suma
    else:
        return add(suma, P, p, puntos)
            
def points(p: int) -> set[tuple[int, int, int]]:
    return points_exh(p)