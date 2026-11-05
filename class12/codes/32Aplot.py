import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Import custom modules
from CoordGeo.line.funcs import line_gen
from CoordGeo.plotting.funcs import label_pts

f = lambda x: (x**2 + 1) / ((x**2 + 2) * (2 * x**2 + 1))
a, b, n = 0.0, 1.0, 10
h = (b - a) / n

# Nodes (x_i, f(x_i)) of the trapezoidal rule
xs = a + h * np.arange(n + 1)
nodes = np.vstack((xs, f(xs)))
T = h * (0.5 * (nodes[1, 0] + nodes[1, -1]) + nodes[1, 1:-1].sum())

x = np.linspace(a, b, 400)
fig, ax = plt.subplots(figsize=(7, 4.5))
ax.plot(x, f(x), 'b-', linewidth=2, label='$f(x)$')

# Each strip is the trapezoid with vertices (x_i,0), (x_i,f_i), (x_{i+1},f_{i+1}), (x_{i+1},0)
for i in range(n):
    P0 = np.array([[nodes[0, i]], [0.0]])
    P1 = nodes[:, i:i + 1]
    P2 = nodes[:, i + 1:i + 2]
    P3 = np.array([[nodes[0, i + 1]], [0.0]])
    poly = np.hstack((P0, P1, P2, P3))
    ax.fill(poly[0, :], poly[1, :], color='tab:blue', alpha=0.3, edgecolor='k')
ax.plot(nodes[0, :], nodes[1, :], 'r.-', label=f'trapezoids ($n={n}$)')

base = line_gen(np.array([[a], [0.0]]), np.array([[b], [0.0]]))
ax.plot(base[0, :], base[1, :], 'k-')
ends = np.array([[a, b], [0.0, 0.0]])
ax.plot(ends[0, :], ends[1, :], 'ko')
label_pts(ends, ['0', '1'])
ax.set_xlabel('x'); ax.set_ylabel('y')
ax.set_title(f'Trapezoidal rule: $T_{{{n}}}$ = {T:.5f}, exact = 0.37024')
ax.grid(True); ax.legend()
plt.savefig('../figs/c12_q32A.png', dpi=200, bbox_inches='tight')
