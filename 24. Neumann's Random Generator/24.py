data = open("24. Neumann's Random Generator/data.txt")

# ordering data
odata = []
for i in data:
    new_i = [int(x) for x in i.replace('\n', '').split()]
    odata.append(new_i)

# Neumann's algorithm
loops = []
for num in odata[1]:
    l = 0
    current = [num]
    while num not in current[:-1]:
        # power of 2
        num *= num
        # truncating the number
        num = int((num/100) % 10000)
        current.append(num)
        l += 1
    loops.append(l)

print(*loops)
