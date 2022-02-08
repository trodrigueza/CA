data = [int(x) for x in input().split()]
w, h, l = data[0], data[1], data[2]
ans = [0, 0]
inverse_x, inverse_y = False, False
x, y = 0, 0
for i in range(100):
    if inverse_x == True:
        x -= 1
    else:
        x += 1
    if inverse_y == True:
        y -= 1
    else:
        y += 1

    if x + l - 1 >= w:
        x -= 2
        if inverse_x == False:
            inverse_x = True
        else:
            inverse_x = False
    if y >= h:
        y -= 2
        if inverse_y == False:
            inverse_y = True
        else:
            inverse_y = False
            
    if x < 0:
        x += 2
        if inverse_x == False:
            inverse_x = True
        else:
            inverse_x = False
    if y < 0:
        y += 2
        if inverse_y == False:
            inverse_y = True
        else:
            inverse_y = False

    ans.append(x)
    ans.append(y)

print(*ans)
