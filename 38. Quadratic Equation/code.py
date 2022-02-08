import cmath
n = int(input())
ans = []
for i in range(n):
    data = [int(x) for x in input().split()]
    a, b, c = data[0], data[1], data[2]
    x1 = (-b + cmath.sqrt((b ** 2) - (4 * a * c))) / (2 * a)
    x2 = (-b - cmath.sqrt((b ** 2) - (4 * a * c))) / (2 * a)   
    if '+0j' in str(x1):
        x1 = str(x1)[1:-4]
    elif '+0j' not in str(x1) and '-' in str(x1) and len(str(x2)) < 4:
        x1 = '0' + str(x1)
    elif str(x1)[-3:-1] != '+0j':
        x1 = str(x1)[1:-1]
    else:
        x1 = '0+' + str(x1)
    if '+0j' in str(x2):
        x2 = str(x2)[1:-4]
    elif '+0j' not in str(x2) and '-' in str(x2) and len(str(x2)) < 4:
        x2 = '0' + str(x2)
    elif str(x2)[-3:-1] != '+0j':
        x2 = str(x2)[1:-1] 
    else:
        x2 = '0+' + str(x2)
    ans.append(x1.replace('j', 'i') + ' ' + x2.replace('j', 'i') + ';')

print(*ans)