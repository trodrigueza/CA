data = open('18. Square root/data.txt')

# ordering data
o_data = []
for i in data:
    new_i = [int(x) for x in i.replace('\n', '').split()]
    o_data.append(new_i)

# calculating square root
sr = []
k = 1
for i in range(len(o_data) - 1):
    r = 1
    x = o_data[k][0]
    for i in range(o_data[k][1]):
        r = round((r + x / r)/2, 7)
    if int(r) - r == 0:
        r = int(r)
    sr.append(r)
    k += 1
print(*sr)
