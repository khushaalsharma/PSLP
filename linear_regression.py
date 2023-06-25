import numpy as np
import matplotlib.pyplot as plt

x = np.array([8,3,2,10,11,3,6,5,8])
y = np.array([4,12,1,12,9,4,9,6,1,14])

m,c = np.polyfit(x,y,1)

regression_line = m*x+c

plt.scatter(X,Y,color = 'blue', label; = 'Data Points')
plt.plot(X,regression_line,color = "red" , label = 'Linear Regression Line')

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Linear Regression')
plt.legend()
plt.show()
