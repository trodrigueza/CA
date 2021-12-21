#Maximum of array
listNumbersStr = input('List your numbers separated by space: ')

#str to int
listNumbersInt = listNumbersStr.split()

for i in range(len(listNumbersInt)):
    listNumbersInt[i] = int(listNumbersInt[i])

#Compare
k1 = 0
min = listNumbersInt[k1]
max = listNumbersInt[k1]

while k1 < len(listNumbersInt):
    if listNumbersInt[k1] <= min:
        min = (listNumbersInt[k1])
    if listNumbersInt[k1] >= max:
        max = listNumbersInt[k1]
    k1 += 1

print(str(max)+" "+str(min))
