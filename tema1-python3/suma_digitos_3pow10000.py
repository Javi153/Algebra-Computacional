# este programa imprime la suma de los dígitos decimales de 3^10000
a = 3 ** 10000
s = 0
while a > 0:
    s = s + a % 10       # a % 10 es el dígito de las unidades de a
    a = a // 10          # división entera de a por 10
print(s)
