n = int(input())
d = {'T': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11,
     '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
ans = []
for i in range(n):
    data = [d[str(x)] for x in input().split()]
    points, a = sum(data), data.count(11)
    if points <= 21:
        ans.append(points)
    elif points > 21 and 11 not in data:
        ans.append('Bust')
    elif points > 21 and 11 in data:
        for i in range(a):
            points -= 10
            if points <= 21:
                ans.append(points)
                break
        if points > 21:
            ans.append('Bust')
    
print(*ans)
