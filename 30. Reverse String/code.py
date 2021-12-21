input_data = list(open('30. Reverse String/data.txt'))
d = input_data[0]

k, l = len(d), -1

for i in range(k):
    d += d[l]
    d = d[0:k] + d[l:]
    l -= 2
    k -= 1
d = d[(int(len(d)/2)):]
print(d)
