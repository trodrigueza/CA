id, d, ans = open('81. Bit Count/data.txt'), [], []

for i in id:
    n = [int(x) for x in i.replace('\n', '').split()]
    d.append(n)

for i in d[1]:
    b = '{:032b}'.format(i & 0xffffffff)
    ans.append(b.count('1'))

print(*ans)
