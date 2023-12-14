O = (1, 0, 1)

def points_exh(p: int) -> set[tuple[int, int, int]]:
    res = set()
    for i in range(p):
        for j in range(i, p):
            if (pow(i, 3, p) + pow(j, 3, p) - 1) % p == 0:
                res.add((i, j, 1))
                res.add((j, i, 1))
    for i in range(p):
        if (1 + pow(i, 3, p)) % p == 0:
            res.add((1,i,0))
    return res
            
def points(p: int) -> set[tuple[int, int, int]]:
    return points_exh(p)

def ast(P: tuple[int, int, int], Q: tuple[int, int, int], p: int) -> tuple[int, int, int]:
    if P == O:
            