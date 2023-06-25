import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

lambda_values = [1,3,5]

k_values = np.arange(0,30)

for i in lambda_values:
  poisson_dist = stats.poisson(mu = i)
  pmf_values = poisson_dist.pmf(k_values)
  plt.plot(k_values,pmf_values, label = f"lambda = {i}")

plt.title("Poisson PMFs for different lambda values")
plt.xlabel("k")
plt.ylabel("Probability")
plt.legend()
plt.show()
