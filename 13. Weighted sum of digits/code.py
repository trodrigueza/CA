input_data = open('13. Weighted sum of digits/data.txt')

# ordering the data
data_ordered = []
for i in input_data:
    new_i = i.replace('/n', '').split()
    data_ordered.append(new_i)

# data to integeers
data_int = []
for i in data_ordered[1]:
    data_int.append(int(i))

# algorithm for separating each number into its digits
k = 0
num_digits = []
for i in data_int:
    current_number = []
    while data_int[k] >= 1:
        digit = data_int[k] % 10
        data_int[k] = data_int[k] // 10
        current_number.insert(0, digit)
    num_digits.append(current_number)
    k += 1

#weighting the numbers
weighted = []
t = 0
for i in num_digits:
    current_weighted = []
    j = 0
    l = 1
    for number in num_digits[t]:
        num_dig_wei = num_digits[t][j] * l
        current_weighted.append(num_dig_wei)
        j += 1
        l += 1
    weighted.append(sum(current_weighted[:]))
    t += 1

print(*weighted)
