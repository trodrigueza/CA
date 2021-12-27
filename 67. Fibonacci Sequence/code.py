id, d, fs, ans = open('67. Fibonacci Sequence/data.txt'), [], [0, 1], []

# ordering
for i in id:
    n = [int(x) for x in i.splitlines()]
    d.append(n)

k = 0
for i in d[1:]:
    t = 0
    if i[0] in fs:
        ans.append(fs.index(i[0]))
    else:
        while i[0] not in fs:
            f = fs[k] + fs[k+1]
            fs.append(f)
            k += 1
        ans.append(fs.index(i[0]))

print(*ans)
