id, d, ans = list(open('55. Matching Words/data.txt')), [], []

for i in id:
    n = i.split()
    d.append(n)

k = 1
for i in d[0]:
    if i in d[0][k:] and i not in ans:
        ans.append(i)
    k += 1

ans.sort()
print(*ans)
