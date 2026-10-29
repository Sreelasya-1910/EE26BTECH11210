from pathlib import Path
import sys
import numpy as np
import matplotlib.pyplot as plt

from CoordGeo.line.funcs import line_gen
from CoordGeo.plotting.funcs import label_pts

# Given endpoints and section-formula point, stored as 2x1 columns for CoordGeo.
P = np.array([[-1.0], [5.0]])
Q = np.array([[5.0], [2.0]])
m, n = 2.0, 1.0
S = (m * Q + n * P) / (m + n)

# Generate PQ using CoordGeo's line_gen function.
PQ = line_gen(P, Q)

fig, ax = plt.subplots(figsize=(7, 5.5))
ax.plot(PQ[0, :], PQ[1, :], linewidth=2, label="PQ (CoordGeo line_gen)")

# Plot and label P, S, Q. CoordGeo label_pts uses pyplot's current axes.
points = np.hstack((P, S, Q))
ax.scatter(points[0, :], points[1, :], zorder=3)
plt.sca(ax)
label_pts(points, ["P(-1, 5)", "S(3, 3)", "Q(5, 2)"])

ax.axhline(0, linewidth=0.8)
ax.axvline(0, linewidth=0.8)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Section formula: PS : SQ = 2 : 1")
ax.grid(True, linestyle=":")
ax.set_aspect("equal", adjustable="datalim")
ax.legend()


plt.tight_layout()
plt.savefig("q4.png", dpi=300, bbox_inches="tight")

