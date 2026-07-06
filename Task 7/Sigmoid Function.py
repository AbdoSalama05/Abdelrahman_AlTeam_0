import numpy as np
import matplotlib.pyplot as plt


x =np.linspace(-10, 10, 1000)
y =1 / (1 + np.exp(-x))

plt.plot(x, y, color='blue', linewidth=2, label='Sigmoid Function')
plt.title("Sigmoid Function")
plt.xlabel("input")
plt.ylabel("sigmoid")
plt.legend()
plt.show()