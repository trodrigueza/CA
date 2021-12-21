data = open('21. Array counters/data.txt')

# ordering the data
o_data = []
for i in data:
    new_i = [int(x) for x in i.replace('\n','').split()]
    o_data.append(new_i)

# counting
counters = [[] for i in range(o_data[0][1])]
numbers = []
k = 1
for x in range(o_data[0][1]):
    numbers.append(k)
    k += 1
for num in o_data[1]:
    index = numbers.index(num)
    counters[index].append(num)

answer = []
l = 1
for x in counters:
    len = x.count(l)
    answer.append(len)
    l += 1
print(*answer)
