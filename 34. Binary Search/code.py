import math
n = int(input())

def f(x):
    l = a * x + b * math.sqrt(x ** 3) - c * math.exp(-x / 50) - d
    return l

ans = []
for i in range(n):
    d = [float(x) for x in input().split()]
    a, b, c, d, k, j = d[0], d[1], d[2], d[3], 0, 100
    for i in range(20):
        m = (k + j) / 2
        i1, i2, im = f(k), f(j), f(m)
        if 0 < im:
            j = m
        elif 0 > im:
            k = m
    ans.append(im)

print(*ans)
