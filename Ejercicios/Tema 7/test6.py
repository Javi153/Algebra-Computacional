# Daniel Martín Gómez
from entrega6 import *
import random

p=7
k=0
n=2 ** k

def mult_pol_mod_cuad(f, g, p):
    n = len(f) + len(g) - 1
    aux1 = len(f)
    aux2 = len(g)
    f = f + [0] * (len(g) - 1)
    g = g + [0] * (len(f) - 1)
    res = [0] * n
    for i in range(aux1):
        for j in range(aux2):
            res[i+j] += f[i]*g[j]

    for i in range(n):
        res[i] %= p

    return res

def check_array(a1, a2):
    n = len(a1)
    if n != len(a2):
        return False

    for i in range(n):
        if a1[i] != a2[i]:
            return False

    return True

while k <= 10:
    p1 = [0] * n
    p2 = [0] * n
    for i in range(500):
        for j in range(n):
            p1[j] = random.randint(0, p-1)
            p2[j] = random.randint(0, p-1)

        h1 = mult_pol_mod_cuad(p1, p2, p)
        h2 = mult_pol_mod(p1, p2, p)
                
        if not check_array(h1, h2):
            print("Failed")
            print('p1: ' + str(p1) + ' p2: ' + str(p2))
            print(str(h1) + ' != ' + str(h2))
            exit()
    k += 1
    n *= 2
print("Se pasaron todos los casos de prueba")
