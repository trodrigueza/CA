# Linear function
input_data = open('10. Linear Function/data.txt')

data_ordered = []

for i in input_data:
    new_i = i.replace('\n', '').split()
    data_ordered.append(new_i)

class LinearFunction():
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    
    def __str__(self):
        a = int((self.y2 - self. y1)/(self.x2 - self.x1))
        b = int(-(a * self.x1) + self.y1)
        return f'({a} {b})'

answer = []
k = 1

for i in range(int(data_ordered[0][0])):
    current_data = [int(x) for x in data_ordered[k]]
    x1 = current_data[0]
    y1 = current_data[1]
    x2 = current_data[2]
    y2 = current_data[3]
    ab = LinearFunction(x1, y1, x2, y2)
    answer.append(ab)
    k += 1

print(*answer)
