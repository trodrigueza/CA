import copy
map = []
for i in range(5):
    line = [str(x) for x in input().replace(' ', '')]
    map.append(line)

ans = []
new_line, max_ind, max_line = '-------', 8, 6
for i in range(5):
    line = 0
    map2 = copy.deepcopy(map)
    map2.insert(0, list(new_line))
    map2.append(list(new_line))
    map.insert(0, list(new_line))
    map.append(list(new_line))
    for i in map2:
        i.insert(0, '-')
        i.append('-')
    for i in map:
        i.insert(0, '-')
        i.append('-')
    for i in map:
        ind = 0
        for l in i:
            neigh = []
            if ind != 0:
                neigh.append(i[ind-1])
            if ind != max_ind:
                neigh.append(i[ind+1])
            if line != 0:
                neigh.append(map[line-1][ind])
                if ind != 0:
                    neigh.append(map[line-1][ind-1])
                if ind != max_ind:
                    neigh.append(map[line-1][ind+1])
            if line != max_line:
                neigh.append(map[line+1][ind])
                if ind != 0:
                    neigh.append(map[line+1][ind-1])
                if ind != max_ind:
                    neigh.append(map[line+1][ind+1])
            org = neigh.count('X')
            if l == 'X' and (org < 2 or org > 3):
                map2[line][ind] = '-'
            elif l =='X' and (org == 2 or org == 3):
                map2[line][ind] = 'X'
            elif l == '-' and org == 3:
                map2[line][ind] = 'X'
            ind += 1
        line += 1
    org_ = 0
    map = copy.deepcopy(map2)
    for i in map:
        print(*i)
        org_ += i.count('X')
    print(org_)
    print('==============')
    new_line = new_line + '--'
    max_ind += 2
    max_line += 2
    ans.append(org_)

print(*ans) 