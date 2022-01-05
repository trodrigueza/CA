n = int(input())
v = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
ans = []
for i in range(n):
    d = [str(x) for x in input().split()]
    k, q = d[0], d[1]
    if k[0] == q[0] or k[1] == q[1]:
        ans.append('Y')
    elif abs(v[k[0]] - v[q[0]]) == abs(int(k[1]) - int(q[1])):
        ans.append('Y')
    else:
        ans.append('N')

print(*ans)
