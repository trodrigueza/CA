n, x0 = 900000, int(input())
letters, vowels = 'bcdfghjklmnprstvwxz', 'aeiou'
ans = []

# LCG
cases = [6 for x in range(900000)]
a, c, m = 445, 700001, 2097152
nth = x0
for i in cases:
    word = []
    k = 1
    for times in range(i):
        nth = ((a * nth + c) % m)
        if k % 2 == 0:
            word.append(vowels[nth % 5])
        else:
            word.append(letters[nth % 19])
        k += 1
    ans.append(''.join(word))
max = 0
for i in ans:
    n = 0
    print(len(ans))
    while i in ans:
        ans.remove(i)
        n += 1
    if n > max:
        max = n
        word = i
print(word)