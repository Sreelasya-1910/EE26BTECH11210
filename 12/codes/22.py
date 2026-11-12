import numpy as np

# Q22: A = [[2, 3], [-1, 2]]; verify A^2 - 4A + 7I = 0
A = np.array([[2, 3], [-1, 2]])
result = A @ A - 4 * A + 7 * np.eye(2)

print("A^2 - 4A + 7I =\n", result)
print("Verified:", bool(np.allclose(result, 0)))
