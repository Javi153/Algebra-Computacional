# este programa imprime todos los números primos entre 2 y 100
def es_primo(n):          # esta función determina si un n >= 2 es primo
    d = 2                 # buscando un divisor d entre 2 y n-1
    while d < n:
        if n%d == 0:      # resto = 0 significa que d divide a n
            return False  # y por lo tanto n no es primo
        d = d + 1
    return True

n = 2
while n <= 100:
    if es_primo(n):
        print(n)
    n = n + 1
