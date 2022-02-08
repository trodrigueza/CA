import math
d = [int(x) for x in input().split()]
n, rad = d[0], math.radians(d[1])
rotated = []
for i in range(n):
    d = [str(x) for x in input().split()]
    x_new = round(int(d[1]) * math.cos(rad) - int(d[2]) * math.sin(rad))
    y_new = round(int(d[2]) * math.cos(rad) + int(d[1]) * math.sin(rad))
    rotated.append([d[0], (x_new, y_new)])
sorted = []
sorted.append(rotated[0])
for i in rotated[1:]:
    coor = i[1]
    for c in sorted:
        if coor[1] == c[1][1]:
            if coor[0] < c[1][0]:
                sorted.insert(sorted.insert(c), i)
                break
        elif coor[1] < c[1][1]:
            sorted.insert(sorted.index(c), i)
            break
    if coor[1] == sorted[-1][1][1]:
        if coor[0] < sorted[-1][1][0]:
            sorted.insert(-1, i)
    elif coor[1] > sorted[-1][1][1]:
        sorted.append(i)
for i in sorted:
    print(i[0], end= ' ')
