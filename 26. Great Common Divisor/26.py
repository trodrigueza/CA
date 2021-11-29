data =  open('26. Great Common Divisor/data.txt')

#ordering data
odata = []
for i in data:
    new_i = [int(x) for x in i.replace('\n', '').split()]
    odata.append(new_i)

#GCD
ans = []
k = 1
for i in range(odata[0][0]):
    x1, x2 = odata[k][0], odata[k][1]
    r = abs(x1-x2)
    while x1 % r != 0 or x2 % r != 0:
        if x1 > x2:
            r = abs(x2 - r)
        else:
            r = abs(x1 - r)
    #LCM
    l = int((x1 * x2) / r)
    ans.append(f'({r} {l})')
    k += 1

print(*ans)
