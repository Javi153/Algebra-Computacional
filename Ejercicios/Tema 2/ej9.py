#Javier Jimenez Arenas
import random
def min_suma_casilla(n, m, a):
    for i in range(n):
        for j in range(m):
            if i != 0 and j != 0:
                a[i][j] = min(a[i - 1][j] + a[i][j], a[i][j - 1] + a[i][j])
            elif i != 0:
                a[i][j] = a[i - 1][j] + a[i][j]
            elif j != 0:
                a[i][j] = a[i][j-1] + a[i][j]
    return a[n-1][m-1]

mat = [[0 for i in range(1000)] for j in range(1000)]
for i in range(1000):
    for j in range(1000):
        mat[i][j] = random.randint(0, 1348451384315384351834)

print(min_suma_casilla(1000, 1000, mat))