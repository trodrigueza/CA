def f(l):
    if l == 0:
        return 1
    for i in range(1, l):
        l *= i
    return l

n = int(input())
ans = []
for i in range(n):
    data = [int(x) for x in input().split()]
    n, k = data[0], data[1]
    c = f(n) / (f(k) * f((n - k)))
    ans.append(int(c))

print(*ans)
