import math
id, d, ans, suits, ranks = open('58. Card Names/data.txt'), [], [], ['Clubs', 'Spades', 'Diamonds', 'Hearts'], ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

for i in id:
    n = [int(x) for x in i.replace('\n', '').split()]
    d.append(n)

for i in d[1]:
    suit_value, rank_value = math.floor(i / 13), i % 13
    ans.append(f'{ranks[rank_value]}-of-{suits[suit_value]}')

print(*ans)
