import numpy as np
import matplotlib.pyplot as plt
delta = 0.025
x = y = np.arange(-3.0, 3.0, delta)
X, Y = np.meshgrid(x, y)
Z    = Y/3

plt.contour(X,Y,Z)
plt.colorbar()
plt.title("contour")
plt.show()