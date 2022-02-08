import math
n = int(input())
ans = []
for i in range(n):
    case = [float(x) for x in input().split()]
    d, b = case[0], case[1]
    h = round(abs(d / math.tan(math.radians(b))))
    ans.append(h)

print(*ans)
