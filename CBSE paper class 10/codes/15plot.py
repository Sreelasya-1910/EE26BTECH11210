from pathlib import Path
import sys
import numpy as np
import matplotlib.pyplot as plt

from CoordGeo.line.funcs import line_gen
from CoordGeo.plotting.funcs import label_pts

# Q15: midpoint of P(a, 4) and Q(2, 2b) is M(2, 6).
# Hence a = 2, b = 4, so P = (2, 4), Q = (2, 8).
P = np.array([[2.0], [4.0]])
M = np.array([[2.0], [6.0]])
Q = np.array([[2.0], [8.0]])

fig, ax = plt.subplots(figsize=(7, 6))

# Draw segment PQ using CoordGeo's line generator.
segment = line_gen(P, Q)
ax.plot(segment[0, :], segment[1, :], linewidth=2, label=r"Segment $PQ$")

# Mark and label P, M, and Q using CoordGeo's point-labeling function.
points = np.hstack((P, M, Q))
ax.scatter(points[0, :], points[1, :], s=[65, 85, 65], zorder=3)
label_pts(points, [r"$P(2,4)$", r"$M(2,6)$", r"$Q(2,8)$"])

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Q15: Midpoint of a Line Segment")
ax.set_xlim(0, 4)
ax.set_ylim(3, 9)
ax.set_xticks(range(5))
ax.set_yticks(range(3, 10))
ax.grid(True, linestyle="--", alpha=0.5)
ax.set_aspect("equal", adjustable="box")
ax.legend()
fig.tight_layout()

output_path = Path(__file__).resolve().parent / "q15.png"
fig.savefig(output_path, dpi=200, bbox_inches="tight")

