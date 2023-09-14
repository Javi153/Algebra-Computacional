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
    return primos[n-1]

print(primoPos(1001))
