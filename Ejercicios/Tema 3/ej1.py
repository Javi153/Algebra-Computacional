def remover_ceros(a):             # a = lista de digitos decimales
    n = len(a)
    while n >= 1 and a[n-1] == 0:
        n -= 1
    del a[n:]

def div2(x):
    acarreo = 0
    for i in range(len(x) - 1, -1, -1):
        aux = x[i] + acarreo
        x[i] = aux // 2
        if aux % 2 == 0:
            acarreo = 0
        else:
            acarreo = 10
    remover_ceros(x)
    return x

def decimal_a_base2(a):
    if not a:
        return []
    elif a[0] % 2 == 0:
        return [0] + decimal_a_base2(div2(a))
    else:
        return [1] + decimal_a_base2(div2(a))
    

print(decimal_a_base2([3,1,1]))