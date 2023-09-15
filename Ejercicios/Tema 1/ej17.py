def eratostenes(n):
    p = [1] * (n + 1)
    p[0] = p[1] = 0

    primos = []

    for i in range(2, n+1):
        if p[i] == 1:
            primos.append(i)
            j = 2
            while i * j <= n:
                p[i*j] = 0
                j += 1
        return p, primos

criba, primos = eratostenes(100)
print("Números primos: ", primos)
print("Criba de Eratostenes: ", p)
