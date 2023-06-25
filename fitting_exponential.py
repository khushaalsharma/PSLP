import numpy as np
import matplotlib.pyplot as plt 
from scipy.stats import expon

x_axis = np.arange(0,1,0.01)

scale_array = [1,0.5,0.33]

for i in range(3):
  scale = scale_array[i]
  plt.plot(x_axis,expon.pdf(x_axis,0,scale), label = f" lambda = {int(1/scale)}")

plt.title("Exponential Distribution")
plt.legend()
plt.show()
