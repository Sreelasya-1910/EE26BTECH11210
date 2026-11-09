import numpy as np

# Q15: mid-point M of P(a, 4) and Q(2, 2b) is (2, 6)
# 2M = P + Q = [2; 4] + [a; 2b],  [a; 2b] = D [a; b]  with  D = diag(1, 2)
M = np.array([[2.0], [6.0]])
C = np.array([[2.0], [4.0]])            # known parts of P + Q
D = np.array([[1.0, 0.0], [0.0, 2.0]])

rhs = 2 * M - C                          # D [a; b] = 2M - C
ab = np.linalg.inv(D) @ rhs              # [a; b] = D^{-1} (2M - C)
a, b = ab.ravel()

print("2M - C =", rhs.ravel())
print("a =", a, " b =", b)
print("a + b =", np.array([[1.0, 1.0]]) @ ab)      # (1 1) D^{-1} (2M - C)

# check: the mid-point of P and Q is M
P = np.array([[a], [4.0]])
Q = np.array([[2.0], [2 * b]])
print("(P + Q)/2 =", ((P + Q) / 2).ravel())
