def checksum(d):
    k = 0
    sums = []
    for i in d[::-1]:
        if i == '?':
            k += 1
            continue
        if k % 2 == 0:
            sums.append(int(i))
        else:
            i = int(i) * 2
            if len(str(i)) > 1:
                i -= 9
            sums.append(i)
        k += 1
    return sum(sums)

n =  int(input())
ans = []
for i in range(n):
    d = input()
    cs = checksum(d)
    if cs % 10 == 0  and '?' not in d:
        ans.append(d)
        continue
    if '?' in d:
        ind = d.index('?')
        summ = cs
        for i in range(10):
            if ind % 2 == 0:
                ii = i * 2
                if len(str(ii)) > 1:
                    ii -= 9
                sum_ = cs + ii
            else:
                sum_ = cs + i
            if sum_ % 10 == 0:
                break
        d = d[:ind] + str(i) + d[ind + 1:]
        ans.append(d)
        continue
    k = 0
    for i in range(len(d)):
        l = list(d)
        l[k], l[k+1] = l[k+1], l[k]
        dc = ''.join(l)
        sum_ = checksum(dc)
        if sum_ % 10 == 0:
            ans.append(dc)
            break
        k += 1
print(*ans)
