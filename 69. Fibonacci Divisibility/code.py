n = int(input())
cases = [int(x) for x in input().split()]
ans = []
for i in cases:
    fibo = [0, 1]
    c, k = fibo[-1], 0
    while c % i != 0:
        c = fibo[-1]
        c += fibo[k] 
        k += 1
        fibo.append(c)
    ans.append(fibo.index(c))

print(*ans)
