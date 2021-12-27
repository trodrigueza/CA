n, k, r = int(input('N = ')), int(input('K = ')), []
ko = k
while n != 0:
    r.insert(0, n)
    n -= 1

l = 1
while len(r) != 1:
    if k-l > len(r) - 1:
        k = k - l - len(r)
        r.remove(r[k])
        l = 0
    else:
        r.remove(r[k-l])
    l += 1
    k += ko

print(*r)
