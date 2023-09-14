import random
def max_gold_rec(l, i, j):
    if i == j:
        return l[i]
    elif i + 1 == j:
        return max(l[i], l[j])
    else:
        return max(l[i] + min(max_gold_rec(l, i + 2, j), max_gold_rec(l, i + 1, j - 1)), l[j] + min(max_gold_rec(l, i, j - 2), max_gold_rec(l, i + 1, j - 1)))

def max_gold(l):
    return max_gold_rec(l, 0, len(l) - 1)

l = []
for i in range(7):
    l.append(random.randint(1, 20))
print(l)
print(max_gold(l))