#Este algoritmo es de orden cuadrático o cúbico, bastante feo
def max_abs_sum_sublst(lista):
    suma = 0
    for elemento in lista:
        suma += elemento
    suma = abs(suma)
    a = 0
    b = len(lista) - 1
    for i in range(len(lista) - 1):
        for j in range(i + 1, len(lista) - 1):
            suma_aux = 0
            for p in range(i, j + 1):
                suma_aux += lista[p]
            suma_aux = abs(suma_aux)
            if suma_aux > suma:
                suma = suma_aux
                a = i
                b = j

    return suma, a, b

#Enric ha hecho un algoritmo tremendamente largo que no voy a copiar
