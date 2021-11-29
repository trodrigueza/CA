n = int(input())

result = []

for i in range(n):
    nums = [int(num) for num in input().split()]
    a = nums[0] * nums[1] + nums[2]

    sum = 0
    
    while a > 0:
        r = a % 10
        sum += r
        a = a // 10
        
    result.append(sum)
        
print(*result)