# Daniel Martín Gómez
from entrega6 import mult_ss_mod
import random

p=7
k=0
n=2 ** k

def mult_pol_mod(f, g, n, p):
    res = [0] * n
    for i in range(n):
        for j in range(n):
            if i+j < n:
                res[i+j] += f[i]*g[j]
            else:
                res[(i+j) % n] -= f[i]*g[j]

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

while k <= 14:
    p1 = [0] * n
    p2 = [0] * n
    for i in range(500):
        for j in range(n):
            p1[j] = random.randint(0, p-1)
            p2[j] = random.randint(0, p-1)

        h1 = mult_ss_mod(p1, p2, k, p)
        h2 = mult_pol_mod(p1, p2, n, p)
                
        if not check_array(h1, h2):
            print("Failed")
            print('p1: ' + str(p1) + ' p2: ' + str(p2))
            print(str(h1) + ' != ' + str(h2))
            exit()
        else:
            print("Check")
    k += 1
    n *= 2

