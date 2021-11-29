# arithmetic progression

# def p (a, b, n):
#     k = 0
#     for i in range(n):
#         total_sum = sum(a * (1 + b * k))
#         k += 1
#     return total_sum

vars = open('8. Arithmetic Progression/data.txt')

vars_sep = []

for string in vars:
    new_str = string.replace('\n','')
    vars_sep.append(new_str)

vars_sep_sep = []
for string in vars_sep:
    new_str = string.split()
    vars_sep_sep.append(new_str)

total_sums = []
k = 0
t = 0
l = 1

for i in range(int(vars_sep[0])):
    current_data = [int(g) for g in vars_sep_sep[l]]
    sum_total = 0
    while t < current_data[2]:
        sum_total += (current_data[k] + (current_data[k+1] * t))
        t += 1
    total_sums.append(sum_total)
    k = 0
    t = 0
    l += 1
    
print(*total_sums)