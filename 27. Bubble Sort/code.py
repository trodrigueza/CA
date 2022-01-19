id = open('27. Bubble Sort/data.txt')

# ordering data
d = []
for i in id:
    n = [int(x) for x in i.replace('\n', '').split()]
    d.append(n)

# d = [[18], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]] (input data)
c, p, s = False, 0, 0
while c == False:
    n, t = 0, 0
    for i in range(d[0][0]-1):
        if d[1][n] <= d[1][n+1]:
            n += 1
        else:
            d[1][n+1], d[1][n] = d[1][n], d[1][n+1]
            n, s, t = n + 1, s + 1, t + 1
    p += 1
    if t == 0:
        c = True

print(p, s)
