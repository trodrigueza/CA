import math
def h_round(n):
    if n - int(n) < 0.5:
        return math.floor(n)
    return math.ceil(n)

n = int(input())
ans = []
for i in range(n):
    d = [float(x) for x in input().split()]
    d1, A, B = d[0], d[1], d[2]
    b = (math.sin(math.radians(180-B))*d1) / (math.sin(math.radians(180-A-(180-B))))
    H = math.sin(math.radians(A)) * b
    ans.append(h_round(H))

print(*ans)
