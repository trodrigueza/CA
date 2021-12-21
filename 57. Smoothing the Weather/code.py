id, d, ans, simp_ans = open('57. Smoothing the Weather/data.txt'), [], [], []

# ordering
for i in id:
    n = [float(x) for x in i.replace('\n', '').split()]
    d.append(n)

k = 0
if (d[1][0] * 10) % 10 == 0:
        ans.append(int(d[1][0]))
else:
    ans.append(float("{:.10f}".format(d[1][0])))

for i in d[1][:-2]:
    n = (d[1][k] + d[1][k+1] + d[1][k+2])/3
    if (n * 10) % 10 == 0:
        ans.append(int(n))
    else:
        ans.append(float("{:.10f}".format(n)))
    k += 1
    
if (d[1][-1] * 10) % 10 == 0:
        ans.append(int(d[1][-1]))
else:
    ans.append(float("{:.10f}".format(d[1][-1])))


print(*ans)
