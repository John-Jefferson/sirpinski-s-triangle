import matplotlib.pyplot as plt
import random

last_x = [0]
last_y = [0]

def nextpoint(x, y, n):
    if n == 0:
        last_x.append(x / 2.0)
        last_y.append(y / 2.0)
    elif n == 1:
        last_x.append((x + 1) / 2.0)
        last_y.append(y / 2.0)
    else:
        last_x.append((x + 0.5) / 2.0)
        last_y.append((y + (3 ** 0.5)) / 2.0)

for t in range(500000):
    n = random.randint(0, 2)
    nextpoint(last_x[-1], last_y[-1], n)
plt.plot(last_x, last_y, "b+", markersize = 0.1)
plt.axis('equal')
plt.show()