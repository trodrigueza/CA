def check(coo, x, y, long):
    io = coo.index((x,y))
    ii = n
    if io - ii < long and len(coo[io:]) - long < 0:
        return True
    return False
    
map = []
for x in range(13):
    line = [str(x) for x in input().replace(' ', '')]
    map.append(line)

steps = [str(x) for x in input().split()]
x, y, n, dir = 2, 0, 0, 'R'
x0 = int(steps[0])
stop = False
long = 3
coo = []

for i in range(x0):
    n += 1
    x += 1
    if map[y][x] == '$':
        long += 1
        map[y][x] = '-'
    if (x,y) not in coo:
        coo.append((x, y))

k = 1

while stop == False:
    dir, mov = steps[k], int(steps[k+1])
    if dir == 'R':
        for i in range(mov):
            x += 1
            n += 1
            if map[y][x] == '$':
                long += 1
                map[y][x] = '-'
            if (x,y) not in coo:
                coo.append((x, y))
            else:
                if check(coo, x, y, long) == True:
                    stop = True
                    break
    elif dir == 'L':
        for i in range(mov):
            x -= 1
            n += 1
            if map[y][x] == '$':
                long += 1
                map[y][x] = '-'
            if (x,y) not in coo:
                coo.append((x, y))
            else:
                if check(coo, x, y, long) == True:
                    stop = True
                    break
    elif dir == 'U':
        for i in range(mov):
            y -= 1
            n += 1
            if map[y][x] == '$':
                long += 1
                map[y][x] = '-'
            if (x,y) not in coo:
                coo.append((x, y))
            else:
                if check(coo, x, y, long) == True:
                    stop = True
                    break
    elif dir == 'D':
        for i in range(mov):
            y += 1
            n += 1
            if map[y][x] == '$':
                long += 1
                map[y][x] = '-'
            if (x,y) not in coo:
                coo.append((x, y))
            else:
                if check(coo, x, y, long) == True:
                    stop = True
                    break
    k += 2                
print(x, y, n)