map = []
for i in range(4):
    line = [int(x) for x in input().split()]
    map.append(line)

moves = [str(x) for x in input().split()]
for move in moves:
    if move == 'U':
        k, j = 0, 0
        for i in map[1:]:
            for i in map[k]:
                map[k][j] += i
                j += 1
            k += 1
2 2 4 2
4 2 2 4
2 2 2 2
2 4 2 2

2 4 4 2
4 2 4 4
2 4 2 2
2 - 