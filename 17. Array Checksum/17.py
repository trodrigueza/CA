data = open('17. Array Checksum/data.txt')

# ordering data
o_data = []
for i in data:
    new_i = [int(x) for x in i.replace('\n','').split()]
    o_data.append(new_i)

# checksum algorithm
result = 0
k = 0
print(o_data[1][k])

while k < o_data[0][0]:
    result = (result + o_data[1][k]) * 113
    # result += o_data[1][k] * seed
    if result >= 10000007:
        result %= 10000007
    k += 1

print(result)
