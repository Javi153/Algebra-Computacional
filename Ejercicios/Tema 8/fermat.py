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
            
def points(p: int) -> set[tuple[int, int, int]]:
    return points_exh(p)

def ast(P: tuple[int, int, int], Q: tuple[int, int, int], p: int) -> tuple[int, int, int]:
    if P == Q:
        return P
    elif P[2] == 0 and Q[2] == 0:
        t = ((P[1] * pow(Q[1], 2, p) - 3 * pow(Q[1], 3, p)) * pow(P[1] * pow(Q[1], 2, p) - pow(P[1], 2, p) * Q[1], -1, p)) % p
    elif Q[2] == 0:
        t = (-1 * (P[0] + P[1] * pow(Q[1], 2, p)) * pow(pow(P[0], 2, p) - P[0] + pow(P[1], 2, p) * Q[1] - P[1] * pow(Q[1], 2, p), -1, p)) % p
    elif P[2] == 0:
        t = (1 - (-1 * (Q[0] + Q[1] * pow(P[1], 2, p)) * pow(pow(Q[0], 2, p) - Q[0] + pow(Q[1], 2, p) * P[1] - Q[1] * pow(P[1], 2, p), -1, p))) % p
    else:
        suma1 = P[0] * pow(Q[0], 2, p) + P[1] * pow(Q[1], 2, p)
        suma2 = pow(P[0], 2, p) * Q[0] + pow(P[1], 2, p) * Q[1]
        t = (suma1 - 1) * pow(suma1 - suma2, -1, p)
    return ((P[0] * t + Q[0] * (1 - t)) % p, (P[1] * t + Q[1] * (1 - t)) % p, (P[2] * t + Q[2] * (1 - t)) % p)

def inv(P: tuple[int, int, int], p: int) -> tuple[int, int, int]:
    return ast(O, P, p)

def add(P: tuple[int, int, int], Q: tuple[int, int, int], p: int) -> tuple[int, int, int]:
    return ast(O, ast(P, Q, p), p)

def mul(k: int, P: tuple[int, int, int], p: int) -> tuple[int, int, int]:
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
        