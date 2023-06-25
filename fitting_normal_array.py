import numpy as np
from scipy.stats import binom

x = [0,1,2,3]
f = [36,40,22,2]
n = 3
sumfx = 0
sumf = 0
for i in range(4):
  sumfx = sumfx + f[i]*x[i]
  sumf = sumf + f[i]

mean = sumfx/sumf
p = mean/n
var = n*p*(1-p)

pmfvalues = binom.pmf(x,n,p)
print("variance:",var)
print("mean:",mean)

print("X      PMF Values")
for i in range(4):
  print(x[i],"      ",sumf*pmfvalues[i])
