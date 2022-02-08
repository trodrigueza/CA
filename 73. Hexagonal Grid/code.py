n = int(input())
ans = []
for i in range(n):
    d = [str(x) for x in input()]
    x, y = 0, 0
    for i in d:
        if i == 'A':
            x += 1
        elif i == 'B':
            x += 1/2
            y += (3/4) ** (0.5)
        elif i == 'C':
            x -= 1/2
            y += (3/4) ** (0.5)
        elif i == 'D':
            x -= 1
        elif i == 'E':
            x -= 1/2
            y -= (3/4) ** (0.5)
        elif i == 'F':
            x += 1/2
            y -= (3/4) ** (0.5)

    d = (x**2 + y**2) ** 0.5
    ans.append(d)
print(*ans)
