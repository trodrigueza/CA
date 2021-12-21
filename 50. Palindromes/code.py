id = list(open('50. Palindromes/data.txt'))

d, ans = [], []
for i in id[1:]:
    n = i.replace('\n', '').replace(' ', '').casefold()
    d.append(n)
for i in d:
    i = ''.join(x for x in i if x.isalpha())
    if i == i[::-1]:
        ans.append('Y')
    else:
        ans.append('N')

print(*ans)
