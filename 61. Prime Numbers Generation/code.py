amount, n, primes = int(input()), 2760000, []
indices = [int(x) for x in input().split()]
integers = list(range(n))

i = 2
while len(primes) < 200001:
    if integers[i] != False:
        primes.append(integers[i])
        for k in range(i, n, i):
            integers[k] = False
    i += 1

for i in indices:
    print(primes[i - 1], end = ' ')
    