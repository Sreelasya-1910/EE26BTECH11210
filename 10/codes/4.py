import numpy as np

# Q4: R divides PQ internally in the ratio m:n.
# Section formula: R = (m Q + n P)/(m + n)
P = np.array([-1.0, 5.0])
Q = np.array([5.0, 2.0])
m, n = 2, 1

R = (m * Q + n * P) / (m + n)
print("R =", R)

# check: PR : RQ = m : n
PR, RQ = np.linalg.norm(R - P), np.linalg.norm(Q - R)
print("PR : RQ =", PR / RQ, "(expected", m / n, ")")
