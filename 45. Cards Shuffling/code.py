data = [int(x) for x in input().split()]
deck = []
for i in 'CDHS':
    for j in 'A23456789TJQK':
        deck.append(i + j)

k, ans = 0, []
for i in data:
    if i > 52:
        i %= 52
    deck[k], deck[i] = deck[i], deck[k]
    k += 1

print(*deck)
