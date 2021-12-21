#SumLoop

values = input('Insert numbers you want to sum: ') #List of numbers

#str to int
valuesList=values.split()

for i in range(len(valuesList)):
    valuesList[i]=int(valuesList[i])

sum = 0

for i in valuesList:
    sum +=  i

print(sum)