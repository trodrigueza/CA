n = int(input())
d = [int(x) for x in input().split()]
array = []
array.append(d[0])
ans = []
for i in d[1:]:
    t, s = i, 0
    for j in range(len(array)):
        if t < array[j]:
            array.insert(j, t)
            s = len(array) - (j + 1)
            break
    if t > array[-1]:
        array.append(t)
    ans.append(s)

print(*ans)
