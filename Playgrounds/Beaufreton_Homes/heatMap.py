# Hit Map LivingRoom BeaufreSTR

import csv

import matplotlib.pyplot as plt
import numpy as np
from math import inf


data = list()
X = list()
Y = list()
X_min, X_max = inf, -inf
Y_min, Y_max = inf, -inf
with open('data-network.csv', 'r') as data_file:
    reader = csv.reader(data_file)
    for r in reader:
        if len(r) > 0:
            data.append(r)
            x, y = int(r[0]), int(r[1])
            X.append(x)
            Y.append(y)
            if x < X_min:
                X_min = x
            if x > X_max:
                X_max = x

            if y < Y_min:
                Y_min = y
            if y > Y_max:
                Y_max = y
X, Y = set(X), set(Y)
Z_a = [[0 for i in range(X_min, X_max + 1)] for j in range(Y_min, Y_max + 1)]
Z_b = [[0 for i in range(X_min, X_max + 1)] for j in range(Y_min, Y_max + 1)]
for d in data:
    x, y, z_a, z_b = map(float, d)
    # Reverse
    y = (Y_max - Y_min) - y + Y_min
    Z_a[int(y)][int(x)] = z_a
    Z_b[int(y)][int(x)] = z_b


X, Y = np.array(list(X)), np.array(list(Y))
Z_a, Z_b = np.array(Z_a), np.array(Z_b)

fig, ax = plt.subplots()
cs = ax.contourf(X, Y, Z_a)
cbar = fig.colorbar(cs)

plt.axis('scaled')
plt.show()
