# parte 1: obtenemos la representación binaria de 3^10000 y su longitud
n = 3 ** 10000
s = ""                # empezamos con una cadena de caracteres vacía
while n > 0:
    s = str(n%2) + s  # n%2 es el bit de las unidades de n
    n = n >> 1        # dividimos por 2 (ignorando los decimales)
print("representación binaria =", s)
print("número de bits =", len(s))

# parte 2: buscamos si la secuencia 101010101010 aparece en s o no
i = 0
encontrada = False
while i < len(s)-12 and not encontrada:
    if s[i:i+12] == "101010101010":
        encontrada = True
    i = i + 1
if encontrada:
    print("secuencia 101010101010 encontrada en la posición", i)
else:
    print("secuencia 101010101010 no encontrada")
