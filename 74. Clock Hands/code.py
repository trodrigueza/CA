import math
n, hlen, mlen = int(input()), 6, 9
d = [str(x) for x in input().split()]
ans = []
for i in d:
    h, m = int(i[:2]), int(i[3:])
    if h > 12:
        h %= 12
    h, m, conh, conm = (h + (m * 1/60)) * (360/12), m * (360/60), False, False
    if h >= 360:
        h -= 360
    if h >= 270:
        fxh, fyh = -1, 1
    elif h >= 180:
        fxh, fyh = -1, -1
        conh = True
    elif h >= 90:
        fxh, fyh = 1, -1
    else: 
        fxh, fyh = 1, 1
        conh = True
    if m >= 360:
        m -= 360
    if m >= 270:
        fxm, fym = -1, 1
    elif m >= 180:
        fxm, fym = -1, -1
        conm = True
    elif m >= 90:
        fxm, fym = 1, -1
    else:
        fxm, fym = 1, 1
        conm =  True
    if h >= 90:
        h %= 90
    if conh == True:
        h = 90 - h
    if m >= 90:
        m %= 90
    if conm == True:
        m = 90 - m
    xh, yh = (math.cos(math.radians(h)) * 6 * fxh) + 10, (math.sin(math.radians(h)) * 6 * fyh) + 10
    xm, ym = (math.cos(math.radians(m)) * 9 * fxm) + 10, (math.sin(math.radians(m)) * 9 * fym) + 10
    ans.append('{0:.8}'.format(xh))
    ans.append('{0:.8}'.format(yh))
    ans.append('{0:.8}'.format(xm))
    ans.append('{0:.8}'.format(ym))
print(*ans)