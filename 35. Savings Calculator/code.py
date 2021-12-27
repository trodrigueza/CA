import math
id, d, ans = open('35. Savings Calculator/data.txt'), [], []

# ordering
for i in id:
    n = [int(x) for x in i.replace('\n', '').split()]
    d.append(n)

for i in d[1:]:
    k = 1
    s, y = [i[0]], 0
    while s[-1] < i[1]:
        c = math.floor(((s[-1] + (s[-1] * (i[2]/100)))*100))/100
        s.append(c)
        y += 1
        k += 1
    ans.append(y)

print(*ans)
