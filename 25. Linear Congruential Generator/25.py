data = open('25. Linear Congruential Generator/data.txt')

# ordering data 
odata = []
for i in data:
    new_i = [int(x) for x in i.replace('\n', '').split()]
    odata.append(new_i)

# algorithm
ans = []
k = 1
for i in range(odata[0][0]):
    nth = odata[k][3]
    for times in range(odata[k][4]):
        nth = ((odata[k][0] * nth + odata[k][1]) % odata[k][2])
    ans.append(nth)
    k += 1

print(*ans)
