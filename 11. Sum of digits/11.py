# sum of digits
str_list = list(open('11. Sum of digits/data.txt'))

str_sep_list = []

# Eliminar '\n' del inputData

for string in str_list:
    new_str = string.replace('\n','').split()
    str_sep_list.append(new_str)

print('str_sep_list=', str_sep_list)

# Pasar a ints todos los datos (para hacer le algoritmo)
int_list = []
k = 0

for i in range(len(str_sep_list)):
    for string in str_sep_list[k]:
        new_str = int(string)
        int_list.append(new_str)
    k += 1

print('int_list=', int_list)

# indicación del ejercicio
final_nums = []
j=0

for i in range(len(str_sep_list)):
    result = int_list[j] * int_list[j+1] + int_list[j+2]
    j += 3
    final_nums.append(result)

print('final_nums=', final_nums)

# lista con x número de listas adentro
digits = [[] for x in range(len(str_sep_list))]
l = 0

# algoritmo
for i in range(len(str_sep_list)):
    while final_nums[l] > 1:
        digit = final_nums[l] % 10
        final_nums[l] = final_nums[l] // 10
        digits[l].append(digit)
    digits[l].append(final_nums[l])
    l += 1

print('digits=', digits)

digits_sum = []
j = 0

# sumar los dígitos de cada número
for i in digits:
    digits_sum.append(str(sum(digits[j])))
    j += 1

print('digits_sum=', digits_sum)

# output en str
digits_sum_str = ' '.join(digits_sum)

print(digits_sum_str)
