def atbash(w):
    res = ""
    for i in range(0, len(w)):
        res += chr(ord('z') - ord(w[i]) + ord('a'))
    return res

def caesar(w, k):
    res = ""
    for i in range(0, len(w)):
        intaux = ord(w[i]) + k
        if intaux > ord('z'):
            chraux = chr(intaux - ord('z') + ord('a') - 1)
        res += chraux
    return res

def rot13(w):
    return caesar(w, 13)

w = str(input())
print(caesar(w, 5))