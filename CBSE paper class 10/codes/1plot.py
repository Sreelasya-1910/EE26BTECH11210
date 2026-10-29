import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

# Circle and geometry
O = np.array([0.0, 0.0])
P = np.array([3.0, 0.0])
radius = 2.0

# Calculate tangent points A and B
d = np.linalg.norm(P - O)
theta = np.arccos(radius / d)

A = np.array([
    radius * np.cos(theta),
    radius * np.sin(theta)
])

B = np.array([
    radius * np.cos(theta),
    -radius * np.sin(theta)
])

# Create figure
fig, ax = plt.subplots(figsize=(8, 6))
from pathlib import Path
import sys
import numpy as np
import matplotlib.pyplot as plt


# Functions imported from your CoordGeo repository
from CoordGeo.conics.funcs import circ_gen
from CoordGeo.line.funcs import line_gen
from CoordGeo.plotting.funcs import label_pts

# Circle parameters
r = 2.0
O = np.array([[0.0], [0.0]])

# The angle between the two tangents is 80 degrees.
# By symmetry, angle OPA = 40 degrees.
angle_half = np.deg2rad(40.0)

# Position of external point P
P = np.array([[r / np.sin(angle_half)], [0.0]])
d = float(P[0, 0])

# Coordinates of tangent points A and B
x_t = r**2 / d
y_t = r * np.sqrt(d**2 - r**2) / d

A = np.array([[x_t], [y_t]])
B = np.array([[x_t], [-y_t]])

# Generate circle using CoordGeo
circle_points = circ_gen(O, r)

fig, ax = plt.subplots(figsize=(8, 6))

ax.plot(
    circle_points[0, :],
    circle_points[1, :],
    linewidth=2
)

# Generate line segments using CoordGeo
segments = [
    (P, A, "-"),
    (P, B, "-"),
    (O, P, "--"),
    (O, A, "-"),
    (O, B, "-")
]

for X, Y, style in segments:
    points = line_gen(X, Y)
    ax.plot(
        points[0, :],
        points[1, :],
        style,
        linewidth=1.6
    )

# Label points using the repository's label_pts()
vertices = np.hstack((O, P, A, B))
label_pts(vertices, ["O", "P", "A", "B"])

# Mark the angle between the tangents
ax.text(P[0, 0] - 0.55, 0.12, r"$80^\circ$", fontsize=12)

# Plot formatting
ax.set_title("Tangents PA and PB to a Circle")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_aspect("equal", adjustable="box")
ax.grid(True, linestyle=":", alpha=0.45)

ax.set_xlim(-2.5, d + 0.8)
ax.set_ylim(-2.7, 2.7)

plt.tight_layout()
plt.savefig("q1.png", dpi=300, bbox_inches="tight")

