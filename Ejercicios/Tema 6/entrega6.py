#Javier Jimenez Arenas
def mult_pol_mod(f: list, g: list, p: int) -> list:
    return

def mult_ss_mod(f: list, g: list, k: int, p:int) -> list:
    if k == 0:
        return [f[0] * g[0]]
    n = 1 << k
    if k % 2 == 0:
        k1 = (k // 2) + 1
        k2 = (k // 2) - 1
    else:
        k1 = (k // 2) + 1
        k2 = (k // 2)
    return