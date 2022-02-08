import random, math
def normal_round(n):
    if n - math.floor(n) < 0.5:
        return math.floor(n)
    return math.ceil(n)

n = int(input())
ans = []
for i in range(n):
    d = [int(x) for x in input().split()]
    pA, pB = d[0]/100, d[1]/100
    a, b = 0, 0
    for i  in range(1000000):
        condition = False
        while condition == False:
            r = random.random()
            if r <= pA:
                condition = True
                a += 1
                break
            else:
                r2 = random.random()
                if r2 <= pB:
                    condition = True
                    b += 1
                    break
    ans.append(normal_round(((a/i) * 100)))

print(*ans)

# mathematically: pX = pA / (pA + pB - pA * pB)
