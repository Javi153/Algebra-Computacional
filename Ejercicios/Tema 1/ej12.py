def primoPos(n):
    primos = []
    i = 2
    while len(primos) < n:
        j = 0
        add = True
        while add and j < len(primos) and primos[j] <= i / 2:
            if i % primos[j] == 0:
                add = False
            j += 1
        if add:
            primos.append(i)
        i += 1
    return primos

def factorizar(n):
    primos = primoPos(n//2)
    mult = {}
    aux = n
    for i in primos:
        if aux % i == 0:
            mult[i] = 0
        while aux % i == 0:
            aux //= i
            mult[i] += 1
    res = []
    for w in mult.keys():
        res.append((w, mult[w]))
    return res


print(factorizar(363468))