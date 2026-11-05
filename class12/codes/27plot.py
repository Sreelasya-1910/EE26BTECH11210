import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Import custom modules
from CoordGeo.line.funcs import line_gen
from CoordGeo.plotting.funcs import label_pts

# 2x + 5y = 1  and  3x + 2y = 7  written as  n^T x = c
n1, c1 = np.array([2.0, 5.0]), 1.0
n2, c2 = np.array([3.0, 2.0]), 7.0
M = np.vstack((n1, n2))
P = np.linalg.solve(M, np.array([c1, c2])).reshape(-1, 1)   # common point

# two points on each line
def two_pts(n, c, x0, x1):
    y0, y1 = (c - n[0] * x0) / n[1], (c - n[0] * x1) / n[1]
    return np.array([[x0], [y0]]), np.array([[x1], [y1]])

A1, B1 = two_pts(n1, c1, -2.0, 6.0)
A2, B2 = two_pts(n2, c2, -2.0, 6.0)

fig, ax = plt.subplots(figsize=(6, 5))
l1 = line_gen(A1, B1); l2 = line_gen(A2, B2)
ax.plot(l1[0, :], l1[1, :], 'b-', label='2x + 5y - 1 = 0')
ax.plot(l2[0, :], l2[1, :], 'g-', label='3x + 2y - 7 = 0')
ax.plot(P[0, :], P[1, :], 'ro')
label_pts(P, ['(3,-1)'])
ax.axhline(0, color='gray'); ax.axvline(0, color='gray')
ax.set_xlabel('x'); ax.set_ylabel('y')
ax.grid(True); ax.legend(); ax.axis('equal')
plt.savefig('../figs/c12_q27.png', dpi=200, bbox_inches='tight')
