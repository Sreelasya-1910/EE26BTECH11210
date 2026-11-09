import numpy as np

np.set_printoptions(suppress=True)

# Q27(A): 2x + 5y = 1 and 3x + 2y = 7, Gaussian elimination on [A | b]
M = np.array([[2.0, 5.0, 1.0],
              [3.0, 2.0, 7.0]])

M[0] = M[0] / M[0, 0]               # R1 <- R1/2
M[1] = M[1] - M[1, 0] * M[0]        # R2 <- R2 - 3 R1
M[1] = M[1] / M[1, 1]               # R2 <- R2/(-11/2)
M[0] = M[0] - M[0, 1] * M[1]        # R1 <- R1 - (5/2) R2

print((M + 0.0).round(4))
print("Paths meet at (x, y) = (%.2f, %.2f)" % (M[0, 2] + 0.0, M[1, 2] + 0.0))
