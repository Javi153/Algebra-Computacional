# este programa obtiene la lista de puntos (x,y)
# que satisfacen 0<=x,y<13 y 13|y^2-x^3-7.
puntos = []                           # empezamos con la lista vacía
x = 0                                 # bucle con x=0,1,...,12
while x < 13:
    y = 0                             # bucle con y=0,1,...,12
    while y < 13:
        if (y**2-x**3-7)%13 == 0:     # si el punto cumple la condición
            puntos += [(x,y)]         # lo agregamos a la lista
        y += 1
    x += 1
print(puntos)
