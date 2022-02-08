n = int(input())
ans = []
for i in range(n):
    s = int(input())
    for a in range(1, int(s/2)):
        d, n = 2 * (s-a), 2 * a*a + s*s - 2 * s*a
        if n % d == 0:
            c = int(n / d)
            b = (c*c - a*a) ** (1/2)
            if b > a:
                ans.append(c * c)
                break
print(*ans)
