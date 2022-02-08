n = int(input())
ans = []
for i in range(n):
    integer = int(input())
    primes_product, j = [], 2
    while j <= integer:
        if integer % j == 0:
            primes_product.append(str(j) + '*')
            integer = integer / j
        else:
            j += 1
    primes_product[-1] = primes_product[-1][:-1]
    ans_str = ''.join(primes_product)
    ans.append(ans_str)

print(*ans)
