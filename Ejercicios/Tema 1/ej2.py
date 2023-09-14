def sumFib(n):
    sum = 0
    fibAnt = 0
    fib = 1
    while fib < n:
        if fib % 2 == 0:
            sum += fib
        fibAnt, fib = fib, fib + fibAnt
    return sum

print(sumFib(4000000))