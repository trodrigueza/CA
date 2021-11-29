from math import floor

#Fahrenheit to Celsius
fahrenheitValuesStr=(input('Insert your Fahrenheit values separated by space: '))

#str to int
fahrenheitValuesInt=fahrenheitValuesStr.split()

for i in range(len(fahrenheitValuesInt)):
    fahrenheitValuesInt[i]=float(fahrenheitValuesInt[i])

#conversion F to C
celsiusValuesInt=[]
k1=1
celsius=0

for i in range(1, int(len(fahrenheitValuesInt))):
    celsius=float((fahrenheitValuesInt[k1]-32)*(5/9))
    celsiusValuesInt.append(celsius)
    del celsius
    k1+=1

fahrenheitValuesInt.remove(fahrenheitValuesInt[0])

#Rounding
def round_half_up(n, decimals=0):
    multiplier = 10 ** decimals
    return floor((n*multiplier + 0.5) / multiplier)

for i in range(len(celsiusValuesInt)):
    celsiusValuesInt[i]=round_half_up(celsiusValuesInt[i])

#int to str
for i in range(len(celsiusValuesInt)):
    celsiusValuesInt[i]=str(celsiusValuesInt[i])

celsiusValuesStr=" ".join(celsiusValuesInt)

print(celsiusValuesStr)
