id = open('29. Sort with Indexes/data.txt')

# ordering data
d, o = [], []
for i in id:
    l = [int(x) for x in i.replace('\n', '').split()]
    d.append(l)
for i in d[1]:
    o.append(i)

# passing
c, p, s, ans = False, 0, 0, []
while c == False:
    n, t = 0, 0
    for i in range(d[0][0]-1):
        if d[1][n] <= d[1][n+1]:
            n += 1
        else:
            d[1][n+1], d[1][n] = d[1][n], d[1][n+1]
            n, s, t = n + 1, s + 1, t + 1
    p += 1
    if t == 0:
        c = True

for i in d[1]:
    ans.append(int(o.index(i))+1)

print(*ans)
