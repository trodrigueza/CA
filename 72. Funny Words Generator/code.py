id = [int(x) for x in input().split()]
n, x0 = id[0], id[1]
letters, vowels = 'bcdfghjklmnprstvwxz', 'aeiou'
ans = []

# LCG
cases = [int(x) for x in input().split()]
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

print(*ans)
