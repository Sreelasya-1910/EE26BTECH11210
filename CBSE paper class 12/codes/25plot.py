import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Import custom modules
from CoordGeo.line.funcs import line_gen
from CoordGeo.plotting.funcs import label_pts

x = np.array([0, 1, 2, 3])
p = np.array([2, 3, 4, 1]) / 10.0            # pmf of X
mean = np.sum(x * p)

fig, ax = plt.subplots(figsize=(6, 4))
ax.bar(x, p, width=0.4, alpha=0.4, edgecolor='k', label='P(X = x)')
pts = np.block([[x], [p]])
ax.plot(pts[0, :], pts[1, :], 'ro')
label_pts(pts, ['0.2', '0.3', '0.4', '0.1'])

# vertical line at the mean E[X] = 1.4
m = line_gen(np.array([[mean], [0.0]]), np.array([[mean], [0.5]]))
ax.plot(m[0, :], m[1, :], 'b--', label='E[X] = 1.4')
ax.set_xticks(x); ax.set_ylim(0, 0.5)
ax.set_xlabel('x'); ax.set_ylabel('P(X = x)')
ax.grid(True); ax.legend()
plt.savefig('../figs/c12_q25.png', dpi=200, bbox_inches='tight')
