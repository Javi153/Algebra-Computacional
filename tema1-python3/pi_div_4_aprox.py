# aproximación del área de un cuarto de círculo de radio 1 haciendo la
# suma de Riemann correspondiente a la integral de raiz(1-x^2) entre 0
# y 1, dividiendo al intervalo de integración en 100000 subintervalos.
area = 0.0
i = 0
while i < 100000:
   x = i/100000               # extremo izquierdo del intervalo
   y = (1 - x**2) ** 0.5      # altura del rectangulo
   area += y/100000           # acumulamos el área
   i += 1
print(area)                   # el valor exacto debería ser pi/4
