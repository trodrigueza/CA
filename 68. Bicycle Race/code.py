id, d, ans = open('68. Bicycle Race/data.txt'), [], []

# ordering
for i in id:
    n = [int(x) for x in i.replace('\n', '').split()]
    d.append(n)

for i in d[1:]:
    t = i[0] / (i[1] + i[2])
    x = i[1] * t
    ans.append(float("{:.7f}".format(x)))

print(*ans)
