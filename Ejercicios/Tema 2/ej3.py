def es_suma_de_k_potencias(x, k, n):
    if k == 0:
        return False
    elif x <= k:
        return True
    m = 2
    sePuede = False
    aux = m ** n
    while not sePuede and aux <= x:
        if x - aux == 0:
            return True
        sePuede = es_suma_de_k_potencias(x - aux, k - 1, n)
        m += 1
        aux = m ** n
    return sePuede

print(es_suma_de_k_potencias(925, 7, 6))