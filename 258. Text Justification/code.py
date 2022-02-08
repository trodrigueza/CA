w = int(input())
lines = []

for i in range(11):
    l = input()
    lines.append(l)
phrase = ' '.join(lines)
le = len(phrase)
c, cr = 0, int(le/w)
n, n2, separated_lines, k = int(le/cr), cr, [], 0
for i in range(cr + 3):
    new_line = []
    for char in phrase:
        new_line.append(char)
        if len(new_line) > w:
            ind = len(new_line) - new_line[::-1].index(' ')
            new_line, phrase = new_line[:ind-1], phrase[ind:]
            separated_lines.append(''.join(new_line))
            break
 
justified = []
for i in separated_lines:
    line, ll, jus_line, j, blank = i, len(i), [], 1, ' '
    while ll != w:
        k = 0
        for char in line:
            char = line[k:k+j]
            jus_line.append(char[0])
            if char == blank and ll != w:
                jus_line.append(' ')
                ll += 1
            k += 1
        j += 1
        blank = blank + ' '
        line, jus_line = ''.join(jus_line), []
    justified.append(line)
justified.append(phrase)

for i in justified:
    print(i)
