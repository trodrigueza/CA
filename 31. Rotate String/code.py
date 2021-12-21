id = list(open('31. Rotate String/data.txt'))

# ordering
d, ans = [], []
for i in id:
    n = i.replace('\n', '')
    d.append(n)

for i in d[1:]:
    if i[0] == '-':
        i = i[-int(i[1]):] + i[3:-int(i[1])]
        ans.append(i)
    else:
        i = i[int(i[0])+2:] + i[2:int(i[0])+2]
        ans.append(i)

print(*ans)
