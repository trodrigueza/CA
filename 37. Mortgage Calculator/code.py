data = [int(x) for x in input().split()]
p_org, r, l = data[0], data[1], data[2]

rates = []
m, p = p_org / l, 1
while p > 0:
    p = p_org
    for i in range(l):
        int = p * (r/1200)
        p = p + int
        p = p - m
    m += 1
    print(p, m)
if p > -300:
    print(round(m - 1))
else:
    print(round(m - 2))
