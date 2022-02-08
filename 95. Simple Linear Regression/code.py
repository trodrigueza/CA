import numpy as np
import scipy.optimize as op

data = []
years = [int(x) for x in input().split()]
n = years[1] - years[0]
for i in range(n + 1):
    d = [str(x) for x in input().split()]
    coor = [int(d[1]), int(d[2])]
    data.append(coor)

data_array = np.array(data)
rainy_days = data_array[:,0]
price = data_array[:,1]

def remainder(vars, price, rainy_days):
  k, b = vars
  y = k * rainy_days + b
  rem = price - y
  nrem = np.linalg.norm(rem)
  return nrem

op = op.minimize(remainder,[1,.1], args=(price,rainy_days))
for i in op.x:
    print(f'{i:.7f}'.format(i = i), end= ' ')

