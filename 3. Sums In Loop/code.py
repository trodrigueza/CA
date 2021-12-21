#Sums in Loop

numPairs=int(input('How many pairs of numbers do you want to sum? '))
valuesStr=input('Insert your numbers separated by space: ')

#Split numbers
valuesList=valuesStr.split() 

#Convert each item to int
for i in range(len(valuesList)):
    valuesList[i]=int(valuesList[i])


pairsSumList=[]
sum=0
k1=0
k2=1


while k1<(numPairs*2):
    sum=str(valuesList[k1]+valuesList[k2])
    pairsSumList.append(sum)
    k1+=2
    k2+=2
    del sum



pairsSumStr= " ".join(pairsSumList)

print(pairsSumStr)



