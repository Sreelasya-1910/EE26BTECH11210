import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Import custom modules
from CoordGeo.line.funcs import line_gen, line_gen_num
from CoordGeo.plotting.funcs import label_pts

f = lambda x: (x**2 + 1) / ((x**2 + 2) * (2 * x**2 + 1))
a, b, n = 0.0, 1.0, 10
dx = (b - a) / n

x = np.linspace(a, b, 400)
fig, ax = plt.subplots(figsize=(7, 4.5))
ax.plot(x, f(x), 'b-', linewidth=2, label='f(x)')

mid = a + (np.arange(n) + 0.5) * dx
ax.bar(mid, f(mid), width=dx, alpha=0.3, edgecolor='k', label='midpoint rectangles (n=10)')

base = line_gen(np.array([[a], [0.0]]), np.array([[b], [0.0]]))
ax.plot(base[0, :], base[1, :], 'k-')
ends = np.array([[a, b], [0.0, 0.0]])
ax.plot(ends[0, :], ends[1, :], 'ko')
label_pts(ends, ['0', '1'])
ax.set_xlabel('x'); ax.set_ylabel('y')
ax.set_title('Area = 0.37024 (Riemann sum)')
ax.grid(True); ax.legend()
plt.savefig('../figs/c12_q32A.png', dpi=200, bbox_inches='tight')
