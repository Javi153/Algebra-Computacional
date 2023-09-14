def Collatz(n):
    verif = {1:1}
    num = 0
    maxlen = 0
    for i in range(1, n):
        aux = i
        j = 0
        while aux not in verif.keys():
            if aux % 2 == 0:
                aux //= 2
            else:
                aux = 3 * aux + 1
            j += 1
        verif[i] = verif[aux] + j
        #print("El número " + str(i) + " cumple la conjetura")
        if verif[i] > maxlen:
            maxlen = verif[i]
            num = i
    return num, maxlen

num, maxlen = Collatz(1000000)
print("El numero con cadena mas larga es el " + str(num) + " con " + str(maxlen) + " pasos")