from math import floor
#Rounding

test_cases=int(input('How many fractions do you want to round? '))
numbers_srt=input('List your numbers separated by space: ')

#Srt to Float
numbers_float=numbers_srt.split()

for i in range(len(numbers_float)):
    numbers_float[i]=float(numbers_float[i])


#Fractions
fractions_round=[]
fraction=0
k1=0
k2=1

for i in range(0,test_cases):
    fraction=numbers_float[k1]/numbers_float[k2]
    fractions_round.append(fraction)
    fraction=0
    k1+=2
    k2+=2

#Rounding
def round_half_up(n, decimals=0):
    multiplier = 10 ** decimals
    return floor(n*multiplier + 0.5) / multiplier

for i in range(len(fractions_round)):
    fractions_round[i]=round_half_up(fractions_round[i])

#int to str
for i in range(len(fractions_round)):
    fractions_round[i]=str(int(fractions_round[i]))

fractions_round_str=' '.join(fractions_round)


print(fractions_round_str)