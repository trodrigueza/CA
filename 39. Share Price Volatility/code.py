n = int(input())
ans = []
for i in range(n):
    data = [str(x) for x in input().split()]
    m = sum([int(x) for x in data[1:]]) / (len(data) - 1)
    d = (sum([(m - int(x)) ** 2 for x in data[1:]]) / (len(data) - 1)) ** 0.5
    comission = m * 0.01
    if d > comission * 4:
        ans.append(data[0])

print(*ans)
