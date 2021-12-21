id = open('48. Collatz Sequence/data.txt')

# ordering data
d = []
for i in id:
    n  = [int(x) for x in i.replace('\n', '').split()]
    d.append(n)

# algorithm
ans = []
for i in d[1]:
    t = 0
    while i != 1:
        if i % 2 == 0:
            i /= 2
            t += 1
        else:
            i = 3 * i + 1
            t+=1
    ans.append(t)

print(*ans)
