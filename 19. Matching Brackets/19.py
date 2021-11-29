data = open('19. Matching Brackets/data.txt')

# ordering data
o_data = []
for i in data:
    new_i = i.replace('\n', '')
    o_data.append(new_i)

# get rid of non brackets characters
just_brackets = [[] for i in range(int(o_data[0]))]
k, l, j = 1, 0, 0 
for str in o_data[1:]:
    spl_str = str.split()
    for str in spl_str:
        ns_str, l = [str.replace(' ','')], 0
        for str in ns_str[l]:
            current = []
            if str in ('(', ')', '[', ']', '{', '}', '<', '>'):
                just_brackets[j].append(str)
            else:
                pass
            l += 1
    j += 1
    k += 1

# join all brackets into one str per testcase
joined_brackets, t = [], 0
for i in just_brackets:
    new_i = [''.join(i)]
    joined_brackets.append(new_i)
    t += 1

# matching brackets function
results, pb = [], {"(" : ")", "[" : "]", "{" : "}", "<" : ">"}
def output():
    stack = []
    for str in i[0]:
        if str in pb:
            stack.insert(0, str)
        elif len(stack) == 0:
            return results.append(0) 
        else:
            for b, bb in pb.items():
                if str == bb and b == stack[0]:
                    stack.pop(stack.index(b))
                elif str == bb and b != stack[0]:
                    return results.append(0)
                else: 
                    pass
    if len(stack) == 0:
        return results.append(1)
    else:
        return results.append(0) 

for i in joined_brackets:
    output()

print(*results)
