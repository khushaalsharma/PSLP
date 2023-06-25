import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

n = 10
p = 0.5
x = np.arange(0,n+1)

binomial_pmf = binom.pmf(x,n,f)

print(binomial_pmf)

plt.plot(x,binomial_pmf,color = "blue")
plt.title(f"Binomial Distribution(n = {n},p = {p})")
plt.show()
