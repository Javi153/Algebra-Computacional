def cambia5por3(n):
    nstr = str(n)
    res = ""
    for i in range(0, len(nstr)):
        if nstr[i] == '5':
            res += '3'
        else:
            res += nstr[i]
    return res

print(cambia5por3(-5125))