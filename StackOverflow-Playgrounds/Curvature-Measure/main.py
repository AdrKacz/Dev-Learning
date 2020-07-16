import matplotlib.pyplot as plt
import numpy as np 


lineA_x = [3, 1, 2, 4]
lineA_y = [6, 4, 2, 1]

lineB_x = [10, 8, 9, 8]
lineB_y = [6, 4, 2, 1]

plt.plot(lineA_x, lineA_y)
plt.plot(lineB_x, lineB_y)
plt.savefig("my_fig.png")

theta_A = 0
for i in range(1, len(lineA_x) - 1):
	a = np.array([lineA_x[i] - lineA_x[i - 1], lineA_y[i] - lineA_y[i - 1]])
	b = np.array([lineA_x[i + 1] - lineA_x[i], lineA_y[i + 1] - lineA_y[i]])


	# np.sum(a * b ): produit scalaire
	theta_A += np.abs(np.arccos(np.sum(a * b) / (np.linalg.norm(a) * np.linalg.norm(b))))

theta_B = 0
for i in range(1, len(lineB_x) - 1):
	a = np.array([lineB_x[i] - lineB_x[i - 1], lineB_y[i] - lineB_y[i - 1]])
	b = np.array([lineB_x[i + 1] - lineB_x[i], lineB_y[i + 1] - lineB_y[i]])


	# np.sum(a * b ): produit scalaire
	theta_B += np.abs(np.arccos(np.sum(a * b) / (np.linalg.norm(a) * np.linalg.norm(b))))

print("Theta A:", theta_A)
print("theta_B:", theta_B)

if (theta_A > theta_B):
	print("A > B")
elif (theta_B > theta_A):
	print("B > A")
else:
	print("A = B")