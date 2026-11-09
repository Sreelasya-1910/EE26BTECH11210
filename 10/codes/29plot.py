from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

from CoordGeo.line.funcs import line_gen
from CoordGeo.conics.funcs import circ_gen_num
from CoordGeo.plotting.funcs import label_pts


def arc(V, rad, t1, t2, num=30):
    t = np.linspace(t1, t2, num)
    return V + rad * np.vstack((np.cos(t), np.sin(t)))


# angle CAB = 20 degrees  =>  angle COB = 40 degrees
r = 2.0
th = np.deg2rad(40.0)
O = np.array([[0.0], [0.0]])
A = np.array([[-r], [0.0]])
B = np.array([[r], [0.0]])
C = r * np.array([[np.cos(th)], [np.sin(th)]])
P = np.array([[r / np.cos(th)], [0.0]])        # tangent at C meets AB at P

# PC is a tangent: OC perpendicular to PC;  angle PCA = 110 degrees
assert abs(((C - O).T @ (C - P)).item()) < 1e-9
u, w = P - C, A - C
assert abs(np.degrees(np.arccos((u.T @ w).item() / (np.linalg.norm(u) * np.linalg.norm(w)))) - 110.0) < 1e-9

fig, ax = plt.subplots(figsize=(7, 5))
plt.sca(ax)

circle = circ_gen_num(O, r, 200)
ax.plot(circle[0, :], circle[1, :], 'b-')
for X, Y in [(A, P), (P, C), (A, C), (C, B)]:
    pts = line_gen(X, Y)
    ax.plot(pts[0, :], pts[1, :], 'b-')
pts = line_gen(O, C)
ax.plot(pts[0, :], pts[1, :], 'r--')

# Angle PCA = 110 degrees at C
t1 = np.arctan2(*(w[::-1, 0]))
t2 = np.arctan2(*(u[::-1, 0]))
if t2 - t1 > np.pi:
    t1 += 2 * np.pi
lo, hi = min(t1, t2), max(t1, t2)
a = arc(C, 0.45, lo, hi)
ax.plot(a[0, :], a[1, :], 'k-', linewidth=0.8)
ax.text(C[0, 0] - 0.1, C[1, 0] - 0.65, r'$110^\circ$', ha='center')

# Right-angle marks at C: angle ACB (angle in a semicircle) and angle OCP (radius perpendicular to tangent)
def square(V, u, w, s=0.18):
    u, w = u / np.linalg.norm(u), w / np.linalg.norm(w)
    sq = np.hstack((V + s * u, V + s * u + s * w, V + s * w))
    ax.plot(sq[0, :], sq[1, :], 'k-', linewidth=0.8)

square(C, A - C, B - C)
square(C, O - C, P - C, s=0.12)

vertices = np.hstack((O, A, B, C, P))
ax.scatter(vertices[0, :], vertices[1, :], color='k', zorder=3)
label_pts(vertices[:, :4], ['$O$', '$A(-2,0)$', '$B(2,0)$', '$C(1.53,1.29)$'])
ax.annotate('$P(2.61,0)$', (P[0, 0], P[1, 0]), textcoords='offset points',
            xytext=(10, 12), ha='center')

ax.set_xlim(-2.4, 3.4)
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.grid(True)
ax.set_aspect('equal', adjustable='box')
fig.tight_layout()
fig.savefig(Path(__file__).resolve().parent.parent / 'figs' / 'q29.png', dpi=200)
