ans = []
for i in [int(x) for x in input().split()]:
    b = '{:8b}'.format(i)
    if b.count('1') % 2 == 0:
        b = b[1:]
        c = chr(int(b, 2))
        ans.append(c)

msg = ''.join(ans)
print(msg)
