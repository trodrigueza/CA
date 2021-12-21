data = open('23. Bubble in Array/data.txt')

# ordering data
odata = []
for i in data:
    new_i = [int(x) for x in i.replace('\n', '').replace('-1', '').split()]
    odata.append(new_i)
odata = odata[0]

# sorting
n, k = 0, 0
for i in range(len(odata)-1):
    if odata[k] > odata[k+1]:
        odata.insert(k+2, odata[k])
        odata.pop(k)
        n += 1
    else:
        pass
    k += 1

# checksum
csum, k = 0, 0
print(csum + odata[k])
while k < len(odata):
    csum = (csum + odata[k]) * 113
    if csum >= 10000007:
        csum %= 10000007
    k += 1

print(n, csum)
