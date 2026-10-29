import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Import custom modules
from CoordGeo.line.funcs import line_gen, line_gen_num
from CoordGeo.plotting.funcs import label_pts

P1 = np.array([[0.0], [20.0]]); P2 = np.array([[3.0], [8.0]]); P3 = np.array([[15.0], [0.0]])

fig, ax = plt.subplots(figsize=(7, 6))
l1 = line_gen(np.array([[0.0], [20.0]]), np.array([[5.0], [0.0]]))      # 4x + y = 20
l2 = line_gen(np.array([[0.0], [10.0]]), np.array([[15.0], [0.0]]))     # 2x + 3y = 30
ax.plot(l1[0, :], l1[1, :], 'b-', label='4x + y = 20')
ax.plot(l2[0, :], l2[1, :], 'g-', label='2x + 3y = 30')

# unbounded feasible region, clipped to the plotting window
poly = np.array([[0, 3, 15, 18, 18, 0], [20, 8, 0, 0, 22, 22]], dtype=float)
ax.fill(poly[0, :], poly[1, :], alpha=0.2, color='orange', label='feasible region')

# objective line Z = 134 through the optimum
z = line_gen(np.array([[0.0], [13.4]]), np.array([[134.0 / 18.0], [0.0]]))
ax.plot(z[0, :], z[1, :], 'r--', label='18x + 10y = 134')

pts = np.block([P1, P2, P3])
ax.plot(pts[0, :], pts[1, :], 'ko')
label_pts(pts, ['(0,20)', '(3,8) min Z=134', '(15,0)'])
ax.set_xlim(-1, 18); ax.set_ylim(-1, 22)
ax.set_xlabel('x'); ax.set_ylabel('y')
ax.grid(True); ax.legend(loc='upper right')
plt.savefig('../figs/c12_q30.png', dpi=200, bbox_inches='tight')
