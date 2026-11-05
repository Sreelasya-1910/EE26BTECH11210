from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

from CoordGeo.line.funcs import line_gen
from CoordGeo.plotting.funcs import label_pts


def arc(V, rad, t1, t2, num=30):
    t = np.linspace(t1, t2, num)
    return V + rad * np.vstack((np.cos(t), np.sin(t)))


def ground_point(B, m):
    """Point where B + lambda m meets the ground  e2^T x = 0."""
    e2 = np.array([[0.0], [1.0]])
    lam = -(e2.T @ B).item() / (e2.T @ m).item()
    return B + lam * m


A = np.array([[0.0], [0.0]])
B = np.array([[0.0], [50.0]])

thP, thQ = np.deg2rad(30.0), np.deg2rad(45.0)
mP = np.array([[np.cos(thP)], [-np.sin(thP)]])      # line of sight to P
mQ = np.array([[np.cos(thQ)], [-np.sin(thQ)]])      # line of sight to Q

P = ground_point(B, mP)
Q = ground_point(B, mQ)

fig, ax = plt.subplots(figsize=(8, 4.5))
plt.sca(ax)

for X, Y, style in [(A, B, 'b-'), (B, Q, 'b-'), (B, P, 'b-'),
                    (A, P, 'k-'), (B, B + np.array([[110.0], [0.0]]), 'k--')]:
    pts = line_gen(X, Y)
    ax.plot(pts[0, :], pts[1, :], style)

# Angles of depression measured from the horizontal through B
for rad, th, txt in [(25.0, thQ, r'$45^\circ$'), (45.0, thP, r'$30^\circ$')]:
    a = arc(B, rad, -th, 0.0)
    ax.plot(a[0, :], a[1, :], 'k-', linewidth=0.8)
    ax.text(rad + 2.0, 50.0 - rad * np.sin(th / 2) - 1.5, txt)

vertices = np.hstack((A, B, Q, P))
ax.scatter(vertices[0, :], vertices[1, :], color='k', zorder=3)
label_pts(vertices, ['$A(0,0)$', '$B(0,50)$', '$Q(50,0)$', '$P(86.6,0)$'])

ax.set_xlabel('$x$ (m)')
ax.set_ylabel('$y$ (m)')
ax.set_xlim(-15, 125)
ax.set_ylim(-10, 65)
ax.grid(True)
ax.set_aspect('equal', adjustable='box')
fig.tight_layout()
fig.savefig(Path(__file__).resolve().parent.parent / 'figs' / 'q38.png', dpi=200)
