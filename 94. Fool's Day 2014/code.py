n, temp = int(input()), []

for i in range(n):
    test_cases = [int(x) ** 2 for x in input().split()]
    temp.append(test_cases)

for i in temp:
    print(sum(i), end = ' ')
