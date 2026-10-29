from pathlib import Path
import sys
import numpy as np
import matplotlib.pyplot as plt

from CoordGeo.line.funcs import line_gen
from CoordGeo.plotting.funcs import label_pts

A = np.array([[-2.0], [2.0]])
B = np.array([[2.0], [8.0]])

# Calculate the three division points
P = A + 0.25 * (B - A)
Q = A + 0.50 * (B - A)
R = A + 0.75 * (B - A)

fig, ax = plt.subplots(figsize=(7, 6))

segment = line_gen(A, B)
ax.plot(segment[0, :], segment[1, :], label="AB")

points = np.hstack((A, P, Q, R, B))
labels = ["A", "P", "Q", "R", "B"]

label_pts(points, labels)
ax.scatter(points[0, :], points[1, :])

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Q31(b): Four Equal Parts of a Line Segment")
ax.grid(True)
ax.set_aspect("equal", adjustable="box")
ax.legend()
fig.tight_layout()

output = Path(__file__).resolve().parent / "q31.png"
fig.savefig(output, dpi=200)

