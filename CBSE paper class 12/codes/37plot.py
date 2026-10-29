import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Import custom modules
from CoordGeo.line.funcs import line_gen
from CoordGeo.plotting.funcs import label_pts

# r(t) = 5 + (2/3) k t ;  k = -3 gives r = 5 - 2t,  k = -6 gives r = 5 - 4t
fig, ax = plt.subplots(figsize=(6, 4.5))
for k, col, t0 in [(-3.0, 'b', 2.5), (-6.0, 'g', 1.25)]:
    s = line_gen(np.array([[0.0], [5.0]]), np.array([[t0], [0.0]]))
    ax.plot(s[0, :], s[1, :], col + '-', label=f'k = {k:.0f}')
    pt = np.array([[t0], [0.0]])
    ax.plot(pt[0, :], pt[1, :], 'ro')
    label_pts(pt, [f't = {t0:g} h'])

given = np.array([[1.0, 1.0], [3.0, 1.0]])          # (1, 3) and (1, 1)
ax.plot(given[0, :], given[1, :], 'ks')
label_pts(given, ['r(1)=3', 'r(1)=1'])
ax.set_xlabel('t (hours)'); ax.set_ylabel('r (mm)')
ax.set_xlim(-0.2, 3); ax.set_ylim(-0.3, 5.6)
ax.grid(True); ax.legend()
plt.savefig('../figs/c12_q37.png', dpi=200, bbox_inches='tight')
