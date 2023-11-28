def gcd_lento(x,y):               # (x,y) != (0,0)
    m = min(abs(x), abs(y))
    while x%m != 0 or y%m != 0:
        m -= 1
    return m

def gcd_binario(x,y):             # (x,y) != (0,0)
    x = abs(x)
    y = abs(y)
    xespar = x%2 == 0
    yespar = y%2 == 0
    if x == 0:                    # caso base: gcd(0,y)=y
        m = y
    elif y == 0:                  # caso base: gcd(x,0)=x
        m = x
    elif xespar and yespar:
        m = 2 * gcd_binario(x//2, y//2)
    elif xespar:
        m = gcd_binario(x//2, y)
    elif yespar:
        m = gcd_binario(x, y//2)
    elif x > y:
        m = gcd_binario(y, (x-y)//2)
    else:
        m = gcd_binario(x, (y-x)//2)
    return m

def gcd_binario_tail_rec(x,y):    # (x,y) != (0,0)
    x = abs(x)
    y = abs(y)
    m = 1
    while x != 0 and y != 0:
        xespar = x%2 == 0
        yespar = y%2 == 0
        if xespar and yespar:
            m *= 2                # aquí acumulamos las potencias de 2
            x //= 2
            y //= 2
        elif xespar:
            x //= 2
        elif yespar:
            y //= 2
        elif x > y:
            x = (x-y)//2
        else:
            y = (y-x)//2
    if x == 0:                    # caso base: gcd(0,y)=y
        m *= y
    else:                         # caso base: gcd(x,0)=x
        m *= x
    return m

def gcd_binario_tail_rec_fancy(x,y):    # (x,y) != (0,0)
    x = abs(x)
    y = abs(y)
    s = 0
    while x != 0 and y != 0:
        xespar = x&1 == 0
        yespar = y&1 == 0
        if xespar and yespar:
            s += 1                #  m = 2**s = 1 << s
            x >>= 1
            y >>= 1
        elif xespar:
            x >>= 1
        elif yespar:
            y >>= 1
        elif x > y:
            x = (x-y) >> 1
        else:
            y = (y-x) >> 1
    if x == 0:                    # caso base: gcd(0,y)=y
        m = y << s
    else:                         # caso base: gcd(x,0)=x
        m = x << s
    return m
