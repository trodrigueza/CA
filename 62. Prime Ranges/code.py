def isPrime(n):
    for i in range(2, round((n) ** 0.5) + 1):
        if n == 2:
            return True
        if n % i == 0:
            return False
    return True
    
n = int(input())
ans = []
for i in range(n):
    pair = [int(x) for x in input().split()]
    c = 0
    for i in range(pair[0], pair[1] + 1):
        if isPrime(i):
            c += 1
    ans.append(c)

print(*ans)
