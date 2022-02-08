n = int(input())
abc = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9, 'K':10, 'L':11, 'M':12, 'N':13, 'O':14, 'P':15, 'Q':16, 'R':17, 'S':18, 'T':19, 'U':20, 'V':21, 'W':22, 'X':23, 'Y':24, 'Z':25}
average = [8.1, 1.5, 2.8, 4.3, 13.0, 2.2, 2.0, 6.1, 7.0, 0.15, 0.77, 7.0, 2.4, 6.8, 7.5, 1.9, 0.095, 6.0, 6.3, 9.1, 2.8, 0.98, 2.4, 0.15, 2.0, 0.074]
for i in range(n):
    d = input()
    pa = [0 for i in range(26)]
    k, l = 1, 0
    for char in d:
        if char == ' ':
            continue
        ind = abc[char]
        pa[ind] += 1
        l += 1
    ind = 0
    for i in pa:
        pa[ind] = (i / l) * 100
        pa[ind] = pa[ind] - average[ind]
        ind += 1