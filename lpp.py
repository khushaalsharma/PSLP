from scipy.optimize import linprog

C = [-4,-3,-6]

A =[[2,3,2],[4,0,3],[2,5,0]]

B = [440,470,430]

x_bounds = (0, None)
y_bounds = (0, None)
z_bounds = (0, None)

result = linprog(c, A_ub = A, B_ub = B, bounds[x_bounds, y_bounds, z_bounds], method = 'simplex')

if result.success:
  print("Optimal Solution found")
  print("X = ",result.x[0])
  print("Y = ",result.x[1])
  print("Z = ",result.x[2])
  print("Optimal Value =", result.fun)
else:
  print("Optimization failed")
  
