import numpy as np

np.set_printoptions(suppress=True)

# Q34: 0.10 x + 0.15 y = 1900,  0.15 x + 0.10 y = 2100
# Gaussian elimination on the augmented matrix [A | b]
A = np.array([[0.10, 0.15], [0.15, 0.10]])
b = np.array([[1900.0], [2100.0]])
M = np.hstack((A, b))

print("rank(A) =", np.linalg.matrix_rank(A),
      " rank([A|b]) =", np.linalg.matrix_rank(M))

M[0] = M[0] / M[0, 0]                  # R1 <- R1/0.10
M[1] = M[1] - M[1, 0] * M[0]           # R2 <- R2 - 0.15 R1
M[1] = M[1] / M[1, 1]                  # R2 <- R2/(-0.125)
M[0] = M[0] - M[0, 1] * M[1]           # R1 <- R1 - 1.5 R2
print((M + 0.0).round(4))

print("Amount at 10% = Rs.", round(M[0, 2], 2))
print("Amount at 15% = Rs.", round(M[1, 2], 2))
