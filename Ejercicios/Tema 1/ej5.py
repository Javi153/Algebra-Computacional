def consChamp(n):
    c = ""
    i = 1
    while len(c) < n:
        c += str(i)
        i += 1
    return c

c = consChamp(1000000)
print(int(c[0])*int(c[9])*int(c[99])*int(c[999])*int(c[9999])*int(c[99999])*int(c[999999]))