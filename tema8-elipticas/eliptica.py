def points(p):
    L = [(0,1,0)]
    for x in range(p):
        for y in range(p):
            if (y**2-x**3-1)%p == 0:
                L.append((x,y,1))
    return L

O = (0,1,0) # neutro

def ast(P, Q, p):
    if P == O and Q == O:
        return (0,1,0)
    if Q == O:
        return (P[0], (-P[1])%p, 1)
    if P == O:
        return (Q[0], (-Q[1])%p, 1)
    if P[0] != Q[0]:
        m = ((P[1]-Q[1]) * pow(P[0]-Q[0],-1,p)) % p
        x = (m**2-P[0]-Q[0]) % p
        y = (m*(x-P[0])+P[1]) % p
        return (x,y,1)
    if (P[1] + Q[1]) % p == 0:
        return O
    m = (3 * (P[0]**2) * pow(2*P[1],-1,p)) % p
    x = (m**2 - 2*P[0]) % p
    y = (m*(x-P[0])+P[1]) % p
    return (x,y,1)
        
def add(P, Q, p):
    return ast(O, ast(P,Q,p), p)

def inv(P, p):
    return ast(ast(O,O,p), P, p)

def mul(k, P, p):
    if k < 0:
        return mul(-k, inv(P, p), p)
    if k == 0:
        return O
    if k % 2 == 0:
        Q = mul(k//2, P, p)
        return add(Q, Q, p)
    Q = mul(k-1, P, p)
    return add(P, Q, p)

def ord(P, p):
    k = 1
    Q = P
    while Q != O:
        Q = add(Q, P, p)
        k += 1
    return k

