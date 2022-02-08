n = int(input())
dic = { 1 : '11', 2 : '21', 3 : '31', 
        4 : '12', 5 : '22', 6 : '32', 
        7 : '13', 8 : '23', 9 : '33' }
ans = []
for i in range(n):
    data = [dic[int(x)] for x in input().split()]
    t = 0
    xa, xb, xc, oa, ob, oc = 0, 0, 0, 0, 0, 0
    x1, x2, x3, o1, o2, o3 = 0, 0, 0, 0, 0, 0
    for i in data:
        if (data.index(i) + 1) % 2 != 0:
            if i[0] == '1':
                xa += 1
            elif i[0] == '2':
                xb += 1
            else:
                xc += 1
            if i[1] == '1':
                x1 += 1
            elif i[1] == '2':
                x2 += 1
            else:
                x3 += 1
        else: 
            if i[0] == '1':
                oa += 1
            elif i[0] == '2':
                ob += 1
            else:
                oc += 1
            if i[1] == '1':
                o1 += 1
            elif i[1] == '2':
                o2 += 1
            else:
                o3 += 1
        t += 1
        if xa == 3 or xb == 3 or xc == 3 or x1 == 3 or x2 == 3 or x3 == 3:
            ans.append(t)
            break
        elif oa == 3 or ob == 3 or oc == 3 or o1 == 3 or o2 == 3 or o3 == 3:
            ans.append(t)
            break
    if xa != 3 and xb != 3 and xc != 3 and x1 != 3 and x2 != 3 and x3 != 3 and oa != 3 and ob != 3 and oc != 3 and o1 != 3 and o2 != 3 and o3 != 3:
        ans.append(0)

print(*ans)
