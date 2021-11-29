data = open('26. Great Common Divisor/data.txt')

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
    if x1 > x2:
        r = x2
    else:
        r = x1
    for i in range(1, r+1):
        if x1 % i == 0 and x2 % i == 0:
            gcd = i
    #LCM
    lcm = int((x1 * x2) / gcd)
    ans.append(f'({gcd} {lcm})')
    k += 1

print(*ans)
