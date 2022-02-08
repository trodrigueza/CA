n = int(input())
data = [[int(x) for x in input().split()]]
ans = []
while len(data[0]) != 1:
    m, j = 0, 1
    for i in data[0]:
        if i > m:
            m = i
        j += 1
    ind = data[0].index(m)
    ans.append(ind)
    data[0].insert(ind, data[0][-1])
    data[0].pop(-1)
    data[0].remove(m)

print(*ans)
