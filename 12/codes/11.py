import numpy as np

# Q11: f(x) = 2x - sin(x), f'(x) = 2 - cos(x)
x = np.linspace(-20, 20, 40001)
derivative = 2 - np.cos(x)

print("minimum of f'(x) on the grid =", derivative.min())
print("f'(x) > 0 everywhere on the grid:", bool(np.all(derivative > 0)))
