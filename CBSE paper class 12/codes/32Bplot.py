import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Import custom modules
from CoordGeo.line.funcs import line_gen, line_gen_num
from CoordGeo.plotting.funcs import label_pts

g = lambda x: x * np.sin(x) / (1 + np.sin(x))
a, b, n = 0.0, np.pi, 12
dx = (b - a) / n

x = np.linspace(a, b, 400)
fig, ax = plt.subplots(figsize=(7, 4.5))
ax.plot(x, g(x), 'b-', linewidth=2, label=r'$g(x)=\frac{x\sin x}{1+\sin x}$')

mid = a + (np.arange(n) + 0.5) * dx
ax.bar(mid, g(mid), width=dx, alpha=0.3, edgecolor='k', label='midpoint rectangles (n=12)')

base = line_gen(np.array([[a], [0.0]]), np.array([[b], [0.0]]))
ax.plot(base[0, :], base[1, :], 'k-')
ends = np.array([[a, b], [0.0, 0.0]])
ax.plot(ends[0, :], ends[1, :], 'ko')
label_pts(ends, ['0', r'$\pi$'])
ax.set_xlabel('x'); ax.set_ylabel('y')
ax.set_title(r'Area = $\frac{\pi(\pi-2)}{2} \approx 1.7932$')
ax.grid(True); ax.legend()
plt.savefig('../figs/c12_q32B.png', dpi=200, bbox_inches='tight')
