import numpy as np
import scipy.stats as stats
import pandas as pd

mu = 79.945
sigma = 5.545
n = 1000

class_interval = [(60,65),(65,70),(70,75),(75,80),(80,85),(85,90),(90,95),(95,100)]
obs_freq = [3,21,150,335,326,135,26,4]

theo_freq = []
for interval in class_interval:
  lower_bound, upper_bound = interval
  z_lower = (lower_bound - mu)/sigma
  z_upper = (upper_bound-mu)/sigma
  freq = n*(stats.norm.cdf(z_upper) - stats.norm.cdf(z_lower))
  theo_freq.append(freq)

table_data = {
  'Class Interval' : class_intervals,
  'Observed Frequency' : obs_freq,
  'Theorectical Frequency' : theo_freq
}

df = pd.DataFrame(table_data)
print(df)
