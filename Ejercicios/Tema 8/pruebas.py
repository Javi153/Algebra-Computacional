import fermat

import math

def primo(num):
    if (num<=1):
        return False
    for i in range(2, math.ceil(math.sqrt(num))+1):
        if(num%i==0 and i!=num):
            return False
    return True


def prueba(p = None):
    primos = []
    if p == None:
        for i in range(4, 5000):
            if primo(i):
                primos.append(i)
    else:
        primos = [p]
    num_casos = 0
    for i in primos:
        pts = fermat.points(i)
        for j in pts:
            for k in pts:
                num_casos += 1
                if num_casos % 10000 == 0:
                    print("Se han superado ", num_casos, " casos de prueba correctamente")
                res = fermat.ast(j, k, i)
                if (res[2] != 0 and res[2] != 1) or (res[2] == 0 and res[0] != 1) or ((pow(res[0], 3, i) + pow(res[1], 3, i) - pow(res[2], 3, i)) % i) != 0:
                    print("Se produjo un error en el cáculo")
                    print("Este es P: ", j, " y este es Q: ", k, " con primo ", i)
                    print("Haciendo ast sale: ", fermat.ast(j, k, i))
                    exit(1)