# triangles
input_data = open('9. Triangles/data.txt')

ordered_data = []

for string in input_data:
    new_str = string.replace('\n', '').split()
    ordered_data.append(new_str)

k = 1

values = []

for i in range(int(ordered_data[0][0])):
    current_data = [int(x) for x in ordered_data[k]]
    if current_data[0] + current_data[1] > current_data [2] and \
    current_data[0] + current_data[2] > current_data [1] and \
    current_data[1] + current_data[2] > current_data [0]:
        value = 1
        values.append(value)
    else:
        value = 0
        values.append(value)
    k += 1

print(*values)
