import numpy as np
import numpy.linalg as LA

# Q31(B): x = A + k1 m1 and x = B + k2 m2
A = np.array([[2.0], [-1.0], [3.0]])
B = np.array([[1.0], [0.0], [4.0]])
m1 = np.array([[1.0], [-2.0], [3.0]])
m2 = np.array([[3.0], [-6.0], [9.0]])

M = np.hstack((m1, m2))
print("rank of [m1 m2] =", LA.matrix_rank(M), "(rank 1 means the lines are parallel)")

# Minimise |A + k m1 - B|^2: the normal equation m1^T m1 k = m1^T (B - A)
k = (m1.T @ (B - A)) / (m1.T @ m1)
foot = A + k * m1
print("k =", k.item(), " closest point on line 1 =", foot.ravel())
print("shortest distance =", LA.norm(foot - B), " sqrt(3) =", np.sqrt(3))

# the same result from the least squares solution of M k = B - A
x_ls, res, rank, sv = LA.lstsq(M, B - A, rcond=None)
print("distance from least squares =", LA.norm(M @ x_ls - (B - A)))
