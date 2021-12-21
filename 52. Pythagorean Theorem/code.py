id, d, ans = open('52. Pythagorean Theorem/data.txt'), [], []

# ordering
for i in id:
    n = [int(x) for x in i.replace('\n', '').split()]
    d.append(n)

for i in d[1:]:
    if i[2] ** 2 ==  i[0] ** 2 + i[1] ** 2:
        ans.append('R')
    elif i[2] ** 2 <  i[0] ** 2 + i[1] ** 2:
        ans.append('A')
    else:
        ans.append('O')

print(*ans)
