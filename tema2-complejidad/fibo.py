def fibonacci_rec(n):   # n >= 0
    if n == 0:
        return 0
    elif  n == 1:
        return 1
    else:
        return fibonacci_rec(n-1) + fibonacci_rec(n-2)

resultados_aprendidos = {}   # diccionario vacio

def fibonacci_mem(n):        # n >= 0
    if n in resultados_aprendidos:
        return resultados_aprendidos[n]
    else:
        if n == 0:
            resultado = 0
        elif n == 1:
            resultado = 1
        else:
            resultado = fibonacci_mem(n-1) + fibonacci_mem(n-2)
        resultados_aprendidos[n] = resultado
        return resultado

def fibonacci_ite(n):       # n >= 0
    fib = [0] * (n+1)       # reservamos espacio para f0,f1,...,fn
    fib[0] = 0
    fib[1] = 1
    for i in range(2,n+1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib[n]
