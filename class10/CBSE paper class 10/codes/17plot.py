from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

from CoordGeo.line.funcs import line_gen
from CoordGeo.plotting.funcs import label_pts

# Triangle LMN: angle L = 22, angle N = 28, angle M = 130 degrees, LN = 72.
# M lies on the ray from L at 22 degrees and on the ray from N at 152 degrees.
aL, aN = np.deg2rad(22.0), np.deg2rad(28.0)
L = np.array([[0.0], [0.0]])
N = np.array([[72.0], [0.0]])
S = np.array([[np.cos(aL), np.cos(aN)],
              [np.sin(aL), -np.sin(aN)]])
t, s = np.linalg.solve(S, N - L).flatten()
M = L + t * np.array([[np.cos(aL)], [np.sin(aL)]])

# Triangle ABC is LMN scaled by k = AB/LM = 1/9 (A <-> L, B <-> M, C <-> N)
k = 5.0 / 45.0
A, B, C = k * L, k * M, k * N

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 3.8))

for ax, V, names, sides in [(ax1, (A, B, C), 'ABC', ('AB = 5', None, None)),
                            (ax2, (L, M, N), 'LMN', ('LM = 45', None, 'LN = 72'))]:
    plt.sca(ax)
    for X, Y in [(V[0], V[1]), (V[1], V[2]), (V[2], V[0])]:
        pts = line_gen(X, Y)
        ax.plot(pts[0, :], pts[1, :], 'b-')
    verts = np.hstack(V)
    ax.scatter(verts[0, :], verts[1, :], color='k', zorder=3)
    label_pts(verts, [f'${n}({verts[0, i]:.1f},{verts[1, i]:.1f})$'
                      for i, n in enumerate(names)])
    # given side lengths used in the solution, written at the mid-points
    mid = (V[0] + V[1]) / 2
    ax.annotate(f'${sides[0]}$', (mid[0, 0], mid[1, 0]), textcoords='offset points',
                xytext=(-22, 6), ha='center')
    if sides[2]:
        mid = (V[0] + V[2]) / 2
        ax.annotate(f'${sides[2]}$', (mid[0, 0], mid[1, 0]), textcoords='offset points',
                    xytext=(0, -16), ha='center')
    ax.set_xlabel('$x$ (cm)')
    ax.set_ylabel('$y$ (cm)')
    ax.margins(y=0.35)
    ax.grid(True)
    ax.set_aspect('equal', adjustable='box')

ax1.set_title(r'$\triangle ABC$')
ax2.set_title(r'$\triangle LMN$')

fig.tight_layout()
fig.savefig(Path(__file__).resolve().parent.parent / 'figs' / 'q17.png', dpi=200)
