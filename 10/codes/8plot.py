from pathlib import Path
import sys
import numpy as np
import matplotlib.pyplot as plt

from CoordGeo.line.funcs import line_gen
from CoordGeo.plotting.funcs import label_pts

# Vertices as 2x1 column vectors (the format expected by CoordGeo).
O = np.array([[0.0], [0.0]])
A = np.array([[0.0], [2.0]])
B = np.array([[4.0], [0.0]])
C = np.array([[4.0], [2.0]])

fig, ax = plt.subplots(figsize=(7, 5))

# Use CoordGeo line_gen for every side and the diagonal AB.
for P, Q in [(O, A), (A, C), (C, B), (B, O)]:
    pts = line_gen(P, Q)
    ax.plot(pts[0, :], pts[1, :], 'b-')

diagonal = line_gen(A, B)
ax.plot(diagonal[0, :], diagonal[1, :], 'r--', label=r'Diagonal $AB$')

# Use CoordGeo's label_pts; it labels columns of a 2xN coordinate matrix.
vertices = np.hstack((O, A, B, C))
label_pts(vertices, ['O', 'A', 'B', 'C'])
ax.scatter(vertices[0, :], vertices[1, :])

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title(r'Rectangle $AOBC$ and diagonal $AB$')
ax.set_xticks(range(-1, 6))
ax.set_yticks(range(-1, 4))
ax.grid(True)
ax.set_aspect('equal', adjustable='box')
ax.legend()
fig.tight_layout()
fig.savefig(Path(__file__).resolve().parent / 'q8.png', dpi=200)

