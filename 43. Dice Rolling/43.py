input_data = open('43. Dice Rolling/data.txt')

# ordering data
data = []
for i in input_data:
    new_i = [float(x) for x in i.replace('\n', '').split()]
    data.append(new_i)

# algorithm
ans = []
for i in data[1:]:
    a = int(i[0] * 6) + 1
    ans.append(a)

print(*ans)
