id, d, ans = open('44. Double Dice Roll/data.txt'), [], []

# ordering data
for i in id:
    n = [int(x) for x in i.replace('\n', '').split()]
    d.append(n)

for i in d[1:]:
    ans.append((i[0] % 6 + i[1] % 6 + 2))

print(*ans)
