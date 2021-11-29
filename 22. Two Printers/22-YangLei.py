data = open('22. Two Printers/data.txt')

#ordering data
o_data = []
for i in data:
    new_i = [int(x) for x in i.replace('\n','').split()]
    o_data.append(new_i)

j = o_data[0][0]
result = [int] * j
k = 1
for i in range(j):
    x, y, n = o_data[k][0], o_data[k][1], o_data[k][2]
    t = n / (1.0 / x + 1.0 / y)
    r0, r1 =  t % x, t % y
    if r0 and r1:
        result[i] = int(t + min(x - r0, y - r1))
    else:
        result[i] = int(t)
    k += 1
print (*result)
