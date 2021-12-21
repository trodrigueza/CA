#Minimum of Three

testsCases=int(input('How many triplets do you want to compare? '))

triplets=input('Insert your numbers, separated by spaces: ')

#Convert str to int
tripletsList=triplets.split()

for i in range(len(tripletsList)):
    tripletsList[i]=int(tripletsList[i])

#Compare
minOfEachTriplet=[]
min=0
k1=0
k2=1
k3=2

while k1<(testsCases*3):
    if (tripletsList[k1]<=tripletsList[k2]<=tripletsList[k3])|(tripletsList[k1]<=tripletsList[k3]<=tripletsList[k2]):
        min=str(tripletsList[k1])
    elif (tripletsList[k2]<=tripletsList[k3]<=tripletsList[k1])|(tripletsList[k2]<=tripletsList[k1]<=tripletsList[k3]):
        min=str(tripletsList[k2]) 
    else: 
        min=str(tripletsList[k3])

    minOfEachTriplet.append(min)
    del min
    k1+= 3
    k2+= 3
    k3+= 3

minOfEachTripletStr=" ".join(minOfEachTriplet)
print(minOfEachTripletStr)


