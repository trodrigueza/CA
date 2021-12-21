#Minimum of Two

testsCases=int(input('How many pairs do you want to compare? '))

pairs=input('Insert your numbers: ')

#Convert str to int
pairsList=pairs.split()

for i in range(len(pairsList)):
    pairsList[i]=int(pairsList[i])

#Compare
minOfEachPair=[]
min=0
k1=0
k2=1

while k1<(testsCases*2):
    if pairsList[k1]<=pairsList[k2]:
        min=str(pairsList[k1])
    else:
        min=str(pairsList[k2])

    minOfEachPair.append(min)
    del min
    k1+= 2
    k2+= 2

minOfEachPairStr=" ".join(minOfEachPair)
print(minOfEachPairStr)

