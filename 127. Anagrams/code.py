d = list(open('127. Anagrams/words.txt'))
dictionary = []
for i in d:
    n = i.replace('\n', '').split()
    w = ''.join(sorted(n[0]))
    dictionary.append(w)

n = int(input())
ans = []
for i in range(n):
    case = [str(x) for x in input().split()]
    w = ''.join(sorted(case[0]))
    a = 0
    for i in dictionary:
        if w == i:
            a += 1
    ans.append(a - 1)

print(*ans)
