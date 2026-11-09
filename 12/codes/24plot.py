import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Import custom modules
from CoordGeo.line.funcs import line_gen, line_gen_num
from CoordGeo.plotting.funcs import label_pts

A = np.array([[0.0], [0.0]]); B = np.array([[1.0], [0.0]])
C = np.array([[1.0], [3.0]]); D = np.array([[0.0], [6.0]])

fig, ax = plt.subplots(figsize=(6, 6))
for X, Y in [(A, B), (B, C), (C, D), (D, A)]:
    s = line_gen(X, Y)
    ax.plot(s[0, :], s[1, :], 'k-', linewidth=2)
verts = np.block([A, B, C, D])
ax.fill(verts[0, :], verts[1, :], alpha=0.25, label='feasible region')

# extend the constraint lines 3x + y = 6 and x = 1 for reference
ext = line_gen(np.array([[1.0], [3.0]]), np.array([[2.0], [0.0]]))
ax.plot(ext[0, :], ext[1, :], 'k:', linewidth=1)
ext = line_gen(np.array([[1.0], [3.0]]), np.array([[1.0], [7.0]]))
ax.plot(ext[0, :], ext[1, :], 'k:', linewidth=1)

ax.plot(verts[0, :], verts[1, :], 'ro')
label_pts(verts, ['O(0,0)', 'B(1,0)', 'C(1,3)', 'D(0,6)'])
ax.annotate('max Z = 24', (0, 6), xytext=(0.25, 6.4))
ax.set_xlim(-0.3, 2.2); ax.set_ylim(-0.5, 7.5)
ax.set_xlabel('x'); ax.set_ylabel('y')
ax.grid(True); ax.legend(loc='upper right')
plt.savefig('../figs/c12_q24.png', dpi=200, bbox_inches='tight')
