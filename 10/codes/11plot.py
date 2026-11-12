from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

from CoordGeo.line.funcs import line_gen
from CoordGeo.plotting.funcs import label_pts

# Vertices from the solution: B = (0,0), C = (16,0), D = (12,0), A = (12,h), h^2 = 48
h = np.sqrt(48.0)
B = np.array([[0.0], [0.0]])
C = np.array([[16.0], [0.0]])
D = np.array([[12.0], [0.0]])
A = np.array([[12.0], [h]])

# (B-A)^T (C-A) = 0 confirms the right angle at A
assert abs(((B - A).T @ (C - A)).item()) < 1e-9
assert abs(np.linalg.norm(C - A) - 8.0) < 1e-9

fig, ax = plt.subplots(figsize=(7, 4.5))
plt.sca(ax)

for X, Y in [(B, C), (C, A), (A, B)]:
    pts = line_gen(X, Y)
    ax.plot(pts[0, :], pts[1, :], 'b-')
pts = line_gen(A, D)
ax.plot(pts[0, :], pts[1, :], 'r--')

# Right-angle marks at D and at A
s = 0.7
sq = np.hstack((D + np.array([[-s], [0.0]]),
                D + np.array([[-s], [s]]),
                D + np.array([[0.0], [s]])))
ax.plot(sq[0, :], sq[1, :], 'k-', linewidth=0.8)
u = (B - A) / np.linalg.norm(B - A)
w = (C - A) / np.linalg.norm(C - A)
sq = np.hstack((A + s * u, A + s * u + s * w, A + s * w))
ax.plot(sq[0, :], sq[1, :], 'k-', linewidth=0.8)

vertices = np.hstack((B, C, D, A))
ax.scatter(vertices[0, :], vertices[1, :], color='k', zorder=3)
label_pts(vertices[:, [0, 1, 3]], ['$B(0,0)$', '$C(16,0)$', '$A(12,6.93)$'])
ax.annotate('$D(12,0)$', (D[0, 0], D[1, 0]), textcoords='offset points',
            xytext=(0, -16), ha='center')

ax.text(14.0, -1.9, '$DC = 4$', ha='center')
ax.text(6.0, -1.9, '$BD = 12$', ha='center')
ax.text(14.4, 3.3, '$x$')

ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_ylim(-3.0, 9.0)
ax.grid(True)
ax.set_aspect('equal', adjustable='box')
fig.tight_layout()
fig.savefig(Path(__file__).resolve().parent.parent / 'figs' / 'q11.png', dpi=200)
