def enc_vigenere(m, s):
    res = ""
    j = 0
    for i in range(0, len(m)):
        intaux = ord(m[i]) + ord(s[j]) - ord('a')
        if intaux > ord('z'):
            intaux = intaux - ord('z') + ord('a') - 1
        res += chr(intaux)
        j = (j + 1) % len(s)
    return res


def dec_vigenere(c, s):
    res = ""
    j = 0
    for i in range(0, len(c)):
        intaux = ord(c[i]) - ord(s[j]) + ord('a')
        if intaux < ord('a'):
            intaux = intaux + ord('z') - ord('a') + 1
        res += chr(intaux)
        j = (j + 1) % len(s)
    return res

print(enc_vigenere("attackatdawn", "lemon"))
print(dec_vigenere("lxfopvefrnhr", "lemon"))