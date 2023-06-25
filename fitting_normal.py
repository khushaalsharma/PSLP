import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

x_axis = np.arange(20,-20,0.01)

mean_array = [1,2,3]
sd_array = [10,7,8]

for i in range(3):
  mean = mean_array[i]
  sd = sd_array[i]
  plt.plot(x_axis,norm.pdf(x_axis,mean,sd), label = f"mean = {mean}, sigma = {sd}")

plt.title("Normal Distribution")
plt.legend()
plt.show()
