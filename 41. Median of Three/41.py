inputData = open('41. Median of Three/data.txt')

# orderingData
data = []
for i in inputData:
    new_i = [int(x) for x in i.replace('\n', '').split()]
    data.append(new_i)

# comparing
ans = []
for i in data[1:]:
    m = 0
    if (i[0] < i[1] and i[1] < i[2]) or (i[0] > i[1] and i[1] > i[2]):
        m = i[1]
    if (i[1] < i[0] and i[0] < i[2]) or (i[1] > i[0] and i[0] > i[2]):
        m = i[0]
    if (i[0] < i[2] and i[2] < i[1]) or (i[0] > i[2] and i[2] > i[1]):
        m =  i[2]

    ans.append(m)

print(*ans)