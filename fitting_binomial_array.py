import numpy as np
import scipy.stats as stats

x = [0,1,2,3,4,5]
f = [142,156,69,27,5,1]

sumfx = 0
sumf = 0

for i in range(6):
  sumfx = sumfx + f[i]*x[i]
  sumf = sumf + f[i]

mean = sumfx/sumf
poisson_dist = stats.poisson(mu = mean)
pmfvalues = poisson_dist.pmf(x)

print("X        PMF Value")
for i in range(6):
  print(x[i],"        ",sumf*pmfvalues[i])
