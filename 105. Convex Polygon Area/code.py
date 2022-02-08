n = int(input())
v = []
for i in range(n):
    d = [int(x) for x in input().split()]
    v.append(d[0])
    v.append(d[1])
x, y = 0, 3
sums = []
for i in range(n-1):
    s = v[x] * v[y] - v[x+1] * v[y-1]
    sums.append(s)
    x += 2
    y += 2
sums.append(v[-2] * v[1] - v[-1] * v[0])
print(abs(sum(sums)/2))