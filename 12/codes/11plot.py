import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Import custom modules
from CoordGeo.line.funcs import line_gen, line_gen_num
from CoordGeo.plotting.funcs import label_pts

x = np.linspace(-10, 10, 400)
f = 2 * x - np.sin(x)
df = 2 - np.cos(x)

fig, ax = plt.subplots(figsize=(7, 5))
ax.plot(x, f, 'b-', linewidth=2, label=r'$f(x) = 2x - \sin x$')
ax.plot(x, df, 'r-', linewidth=2, label=r"$f'(x) = 2 - \cos x$")

# bounds 1 <= f'(x) <= 3 drawn as line segments
lo = line_gen_num(np.array([[-10.0], [1.0]]), np.array([[10.0], [1.0]]), 50)
hi = line_gen_num(np.array([[-10.0], [3.0]]), np.array([[10.0], [3.0]]), 50)
ax.plot(lo[0, :], lo[1, :], 'k--', linewidth=1)
ax.plot(hi[0, :], hi[1, :], 'k--', linewidth=1)
pts = np.array([[0.0], [1.0]])
ax.plot(pts[0, :], pts[1, :], 'ko')
label_pts(pts, ["f'(0)=1"])
ax.axhline(0, color='gray'); ax.axvline(0, color='gray')
ax.set_xlabel('x'); ax.set_ylabel('y')
ax.grid(True); ax.legend()
plt.savefig('../figs/c12_q11.png', dpi=200, bbox_inches='tight')
