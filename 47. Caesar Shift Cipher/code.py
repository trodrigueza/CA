id, d, ans = list(open('47. Caesar Shift Cipher/data.txt')), [], []

for i in id:
    n = i.replace('\n', '')
    d.append(n)

k = int(d[0][2])
for i in d[1:]:
    t = []
    for char in i:
        if char.isalpha():
            c = chr(ord(char) - k)
            if c.isalpha() == False:
                c = chr(ord(char) + 26 - k)
            t.append(c)
        else:
            t.append(char)
    ans.append(''.join(t))

print(*ans)
