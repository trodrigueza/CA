from math import floor

data = list(open('16. Average of an array/data.txt'))

# ordering data
ordered_data = []
for i in data:
    new_i = i.replace('\n','').split()
    ordered_data.append(new_i)

# calculating the average
averages = []
for i in ordered_data[1:]:
    average = sum([int(x) for x in i[:-1]]) / (len(i) - 1)
    averages.append(round(average))

print(*averages)