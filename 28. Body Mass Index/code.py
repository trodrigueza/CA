input_data = open('28. Body Mass Index/data.txt')

# ordering data
data = []
for i in input_data:
    new_i = [float(x) for x in i.replace('\n', '').split()]
    data.append(new_i)

# comparing
ans = []
for i in data[1:]:
    BMI = i[0]/i[1] ** 2
    if BMI < 18.5:
        ans.append('under')
    elif BMI >= 30.0:
        ans.append('obese')
    elif 18.5 <= BMI and BMI < 25.0:
        ans.append('normal')
    else:
        ans.append('over')

print(*ans)