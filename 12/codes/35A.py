import numpy as np

# Q35(A): line x = A + k m with A = (-2,-1,3), m = (3,2,2); point P = (1,2,3).
# Points at distance 3 sqrt(2) from P:  |A + k m - P|^2 = 18
A = np.array([-2.0, -1.0, 3.0])
m = np.array([3.0, 2.0, 2.0])
P = np.array([1.0, 2.0, 3.0])
d = A - P

# (m^T m) k^2 + 2 (m^T d) k + (d^T d - 18) = 0
coeffs = [m @ m, 2 * (m @ d), d @ d - 18]
print("quadratic coefficients:", coeffs)

for k in np.roots(coeffs):
    Q = A + k * m
    print(f"k = {k:.6f}  Q = {Q.round(6)}  |Q - P| = {np.linalg.norm(Q - P):.6f}")
