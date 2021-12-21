input_data = open('12. Modulo and time difference/data.txt')

ordered_data = []
for i in input_data:
    new_i = i.replace('\n','').split()
    ordered_data.append(new_i)

seconds = []
differences = []
output = []

k = 1
l = 0
t = 0
j = 0

for i in range(int(ordered_data[0][0])):
    current_data = [int(x) for x in ordered_data[k]]
    # datas to seconds
    for i in range(2):
        day_second = current_data[l] * 24 * 60 * 60
        hour_second = current_data[l+1] * 60 * 60
        min_second = current_data[l+2] * 60
        second_second = current_data[l+3]
        total_seconds = day_second + hour_second + min_second + second_second
        seconds.append(total_seconds)
        l = 4
    k += 1
    l = 0
    # differences (in seconds)
    difference = seconds[t] - seconds[t+1]
    differences.append(abs(difference))
    t += 2
    # modulo
    sec = differences[j] % 60
    min = (differences[j] // 60) % 60
    hour = (((differences[j] // 60) // 60) % 24) 
    day = (((differences[j] // 60 ** 2) // 24) % 24)
    # add to output
    output.extend([f'({day} {hour} {min} {sec})'])
    j += 1

print(*output)
