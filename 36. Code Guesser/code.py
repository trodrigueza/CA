# it's not good
n = int(input())
not_poss = [[] for x in range(4)]
poss = [[] for x in range(4)]
for i in range(n):
    guess = [int(x) for x in input().split()]
    p, a = guess[0], guess[1]
    k = 0
    if a == 0:
        for i in str(p):
            not_poss[k].append(int(i))
            k += 1
    else:
        for i in str(p):
            poss[k].append(int(i))
            k += 1

k = 0
ans = []
for i in range(len(poss)):
    for i in poss[k]:
        if i in not_poss[k]:
            while i in poss[k]:
                poss[k].remove(i)
    k += 1

print(poss)
print(not_poss)
