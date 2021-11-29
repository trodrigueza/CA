# vowel count

inputData = list(open("inputData9.txt"))
# print(''.join(inputData))
# inputDataStr = []

# for string in inputData:
#     new_string = string.replace('\n','')
#     inputDataStr.append(new_string)

# print(inputDataStr)
total = []

for string in inputData[1:]:
    vowel_count = sum(string.count(x) for x in 'aeiouy')
    total.append(str(vowel_count))

total_str = ' '.join(total)
print(total_str)
