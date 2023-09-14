def gcd_euclides(x, y):
    if x == 0:
        return y
    elif y == 0:
        return x
    else:
        return gcd_euclides(y, x % y)
    
print(gcd_euclides(15, 45))