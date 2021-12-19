data = open('22. Two Printers/data.txt')

#ordering data
o_data = []
for i in data:
    new_i = [int(x) for x in i.replace('\n','').split()]
    o_data.append(new_i)

ans = []
k = 1
for i in range(o_data[0][0]):
    x ,y, n = o_data[k][0], o_data[k][1], o_data[k][2]
    counter, l, j = 0, 0, 0
    print(ans)
    while n > 0:
        counter += 1
        if counter == x + l * x:
            n -= 1
            l += 1
            if n == 0:
                ans.append(counter)
                break
        if counter == y + j * y:
            n -= 1
            j += 1
            if n == 0:
                ans.append(counter)
                break
    k += 1
print(*ans)
