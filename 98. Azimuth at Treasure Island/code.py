import math
def x(d, h):
    exe = math.cos(math.radians(d)) * h
    return exe
def y(d, h):
    eye = math.sin(math.radians(d)) * h
    return eye
def aprox(n):
    if n - int(n) >= 0.5:
        if n < 0:
            return math.floor(n)
        return math.ceil(n)
    if n < 0:
        return math.ceil(n)
    return math.floor(n)

d = []
for i in range(17): # # of input lines
    l = [str(x) for x in input().split()]
    d.append(l)

exes, eyes = [], []
for i in d[1:-1]:
    mag , deg = int(i[1]), int(i[5])
    if deg > 270 or (deg < 90):
        xn = y(deg, mag)
        yn = x(deg, mag)
    else:
        xn = x(deg, mag)
        yn = y(deg, mag)
    exes.append(xn)
    eyes.append(yn)

print(aprox(sum(exes)), aprox(sum(eyes)))
