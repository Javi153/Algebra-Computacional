# este programa es para mostrar la mutabilidad de las listas

# la siguiente función ordena una lista l de enteros de menor a mayor
def ordenar(l):
    n = len(l)
    i = 0                                 # bucle i = 0,1,...,n-1
    while i < n:
        j = i+1                           # bucle j = i+1,...,n-1
        while j < n:
            if l[i] > l[j]:               # si estan mal ordenados,
                l[i], l[j] = l[j], l[i]   # los cambiamos de lugar
            j += 1
        i += 1

# ahora creamos una lista lst1
lst1 = [2,5,-1,3,77,8,-3]
print(lst1)

# la lista lst2 es la MISMA que lst1 y no una simple copia de lst1
# las asignaciones en Python3 copian REFERENCIAS (direcciones de
# memoria) y no crean nuevos objetos
lst2 = lst1
print(lst2)

# agregamos un elemento a lst1
lst1.append(-17)
print(lst1)

# notar que lst2 TAMBIÉN CAMBIA!
print(lst2)

# del mismo modo, al invocar la función ordenar, la variable l será
# la MISMA lista lst1, y por eso, todas las acciones hechas sobre l
# están hechas sobre lst1 (y también sobre lst2):
ordenar(lst1)
print(lst1)
print(lst2)
