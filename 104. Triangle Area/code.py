id, d, ans = open('104. Triangle Area/data.txt'), [], []

for i in id:
    n = [int(x) for x in i.replace('\n', '').split()]
    d.append(n)

for i in d[1:]:
    a = 0.5 * abs((((i[0] * i[5]) + (i[2] * i[1]) + (i[4] * i[3])) - ((i[0] * i[3]) + (i[2] * i[5]) + (i[4] * i[1]))))
    if (a * 10) % 10 == 0:
        ans.append(int((a)))
    else:
        ans.append(float('{:.7f}'.format(a)))

print(*ans)
