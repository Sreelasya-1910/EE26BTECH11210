from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

from CoordGeo.plotting.funcs import label_pts

# Points on y = x^2 - 2x - 1
x = np.linspace(-1.5, 3.5, 101)
y = x**2 - 2 * x - 1

# Zeroes alpha = 1 + sqrt(2), beta = 1 - sqrt(2), and the vertex
alpha, beta = 1 + np.sqrt(2), 1 - np.sqrt(2)
zeros = np.array([[alpha, beta], [0.0, 0.0]])
vertex = np.array([[1.0], [-2.0]])

fig, ax = plt.subplots(figsize=(7, 5))
plt.sca(ax)
ax.plot(x, y, 'b-', label=r'$y = x^2 - 2x - 1$')
ax.axhline(0, color='k', linewidth=0.8)
ax.axvline(0, color='k', linewidth=0.8)

pts = np.hstack((zeros, vertex))
ax.scatter(pts[0, :], pts[1, :], color='r', zorder=3)
label_pts(pts, [r'$\alpha = 1+\sqrt{2}$', r'$\beta = 1-\sqrt{2}$', '$(1,-2)$'])

ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.grid(True)
ax.legend()
fig.tight_layout()
fig.savefig(Path(__file__).resolve().parent.parent / 'figs' / 'q21b.png', dpi=200)
