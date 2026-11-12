import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Import custom modules
from CoordGeo.line.funcs import line_gen
from CoordGeo.plotting.funcs import label_pts

g = lambda x: x * np.sin(x) / (1 + np.sin(x))
a, b, n = 0.0, np.pi, 12
h = (b - a) / n

# Nodes (x_i, g(x_i)) of the trapezoidal rule
xs = a + h * np.arange(n + 1)
nodes = np.vstack((xs, g(xs)))
T = h * (0.5 * (nodes[1, 0] + nodes[1, -1]) + nodes[1, 1:-1].sum())

x = np.linspace(a, b, 400)
fig, ax = plt.subplots(figsize=(7, 4.5))
ax.plot(x, g(x), 'b-', linewidth=2, label=r'$g(x)=\frac{x\sin x}{1+\sin x}$')

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
label_pts(ends, ['0', r'$\pi$'])
ax.set_xlabel('x'); ax.set_ylabel('y')
ax.set_title(rf'Trapezoidal rule: $T_{{{n}}}$ = {T:.4f}, exact = $\frac{{\pi(\pi-2)}}{{2}} \approx 1.7932$')
ax.grid(True); ax.legend()
plt.savefig('../figs/c12_q32B.png', dpi=200, bbox_inches='tight')
