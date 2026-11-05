from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

from CoordGeo.line.funcs import line_gen
from CoordGeo.conics.funcs import circ_gen_num
from CoordGeo.plotting.funcs import label_pts


def arc(V, rad, t1, t2, num=30):
    """Points of an arc of radius rad about V from angle t1 to t2 (radians)."""
    t = np.linspace(t1, t2, num)
    return V + rad * np.vstack((np.cos(t), np.sin(t)))


# Vectors from the solution:  r = d cos(phi), phi = angle POA = 50 degrees
r = 2.0
phi = np.deg2rad(50.0)
d = r / np.cos(phi)

O = np.array([[0.0], [0.0]])
P = np.array([[d], [0.0]])
A = r * np.array([[np.cos(phi)], [np.sin(phi)]])
B = r * np.array([[np.cos(phi)], [-np.sin(phi)]])

# Direction vectors of the tangents:  m1, m2
m1 = (A - P) / np.linalg.norm(A - P)
m2 = (B - P) / np.linalg.norm(B - P)
assert abs(((A - O).T @ (A - P)).item()) < 1e-9          # OA perpendicular to PA
assert abs(np.degrees(np.arccos((m1.T @ m2).item())) - 80.0) < 1e-9

fig, ax = plt.subplots(figsize=(7, 5.5))
plt.sca(ax)

# Circle and segments, all generated from coordinates
circle = circ_gen_num(O, r, 200)
ax.plot(circle[0, :], circle[1, :], 'b-')
for X, Y in [(P, A), (P, B), (O, A), (O, B)]:
    pts = line_gen(X, Y)
    ax.plot(pts[0, :], pts[1, :], 'b-')
pts = line_gen(O, P)
ax.plot(pts[0, :], pts[1, :], 'r--')

# Right-angle marks at A and B (OA perp PA, OB perp PB)
s = 0.25
for V, sgn in [(A, 1.0), (B, -1.0)]:
    u = (O - V) / np.linalg.norm(O - V)
    w = (P - V) / np.linalg.norm(P - V)
    sq = np.hstack((V + s * u, V + s * u + s * w, V + s * w))
    ax.plot(sq[0, :], sq[1, :], 'k-', linewidth=0.8)

# Angle APB = 80 degrees at P
ang = np.arctan2(m1[1, 0], m1[0, 0])
a = arc(P, 0.8, ang, 2 * np.pi - ang)
ax.plot(a[0, :], a[1, :], 'k-', linewidth=0.8)
ax.text(P[0, 0] - 0.7, 0.08, r'$80^\circ$')

# Angle POA = 50 degrees at O
a = arc(O, 0.6, 0.0, phi)
ax.plot(a[0, :], a[1, :], 'k-', linewidth=0.8)
ax.text(0.7, 0.2, r'$50^\circ$')

vertices = np.hstack((O, P, A, B))
ax.scatter(vertices[0, :], vertices[1, :], color='k', zorder=3)
label_pts(vertices[:, :3], ['$O(0,0)$', '$P(3.11,0)$', '$A(1.29,1.53)$'])
ax.annotate('$B(1.29,-1.53)$', (B[0, 0], B[1, 0]), textcoords='offset points',
            xytext=(0, -18), ha='center')

ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.grid(True)
ax.set_aspect('equal', adjustable='box')
fig.tight_layout()
fig.savefig(Path(__file__).resolve().parent.parent / 'figs' / 'q1.png', dpi=200)
