def g(n):
    lista = [1,2,2]
    k = 3
    while len(lista) < n:
        for i in range(lista[k - 1]):
            lista.append(k)
        k += 1
    return lista[n-1]
