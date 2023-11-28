# este programa determina de cuántas formas se puede escribir el
# número 10000 como suma de dos primos

def es_primo(n):
    for d in range(2,n):
        if n%d == 0:
            return False
    return True

# obtenemos el conjunto de primos <= 10000
primos = set()                          # conjunto vacío
for p in range(2,10001):                # p = 2,3,...,10000
    if es_primo(p):                     # si p es primo
        primos |= {p}                   # lo agregamos al conjunto

# obtenemos el conjunto de numeros de la forma 10000-p con p primo
restas = set()
for p in primos:
    restas |= {10000-p}

print(len(primos & restas))  # el & es la intersección de conjuntos
