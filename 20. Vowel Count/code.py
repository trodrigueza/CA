# vowel count

inputData = list(open("20. Vowel Count/data.txt"))
total = []

for string in inputData[1:]:
    vowel_count = sum(string.count(x) for x in 'aeiouy')
    total.append(str(vowel_count))

total_str = ' '.join(total)
print(total_str)
