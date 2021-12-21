input_data = open('14. Modular Calculator/data.txt')

# ordering data
ordered_data = []
for i in input_data:
    new_i = i.replace('\n','').split()
    ordered_data.append(new_i)

# data to int
for i in ordered_data[1:]:
    i[1] = int(i[1])

# operations and else case gives de module
int = int(ordered_data[0][0])
for i in ordered_data[1:]:
    if i[0] == '+':
        int += i[1]
    elif i[0] == '*':
        int *= i[1]
    else:
        int %= i[1]
print(int)