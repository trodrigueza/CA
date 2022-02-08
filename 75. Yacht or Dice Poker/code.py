n = int(input())
ans = []
for i in range(n):
    case = [int(x) for x in input().split()]
    case.sort()
    nums = [case.count(1), case.count(2), case.count(3), case.count(4), case.count(5), case.count(6)]
    if case == [i for i in range(1,6)]:
        ans.append('small-straight')
    elif case == [i for i in range(2,7)]:
        ans.append('big-straight')
    elif 3 in nums and 2 in nums:
        ans.append('full-house')
    elif nums.count(2) == 2:
        ans.append('two-pairs')
    elif nums.count(2) == 1:
        ans.append('pair')
    elif 5 in nums:
        ans.append('yacht')
    elif 4 in nums:
        ans.append('four')    
    elif 3 in nums:
        ans.append('three')

print(*ans)
