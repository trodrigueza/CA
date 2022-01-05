secret_n, guesses = [str(x) for x in input().split()], [(x) for x in input().split()]

for i in guesses:
    b, c = 0, 0
    for k in i:
        if k in secret_n[0] and i.index(k) == secret_n[0].index(k):
            b += 1
        elif k in secret_n[0] and i.index(k) != secret_n[0].index(k):
            c += 1
    print(f'{b}-{c}', end = ' ')
    