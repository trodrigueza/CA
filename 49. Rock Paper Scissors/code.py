id, d, ans = list(open('49. Rock Paper Scissors/data.txt')), [], []

for i in id:
    n = [str(x) for x in i.replace('\n', '').split()]
    d.append(n)

for i in d[1:]:
    p1, p2 = 0, 0
    for m in i:
        if m[0] == 'S' and m[1] == 'P':
            p1 += 1
        elif m[0] == 'S' and m[1] == 'R':
            p2 += 1
        if m[0] == 'P' and m[1] == 'R':
            p1 += 1
        elif m[0] == 'P' and m[1] == 'S':
            p2 += 1
        if m[0] == 'R' and m[1] == 'S':
            p1 += 1
        elif m[0] == 'R' and m[1] == 'P':
            p2 += 1

    if p1 > p2:
        ans.append('1')
    else:
        ans.append('2')

print(*ans)
