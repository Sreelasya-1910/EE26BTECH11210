import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Import custom modules
from CoordGeo.line.funcs import line_gen, line_gen_num
from CoordGeo.plotting.funcs import label_pts

# line: x = t + 2, y = 2t, z = 2 - 3t
pt = lambda t: np.array([[t + 2.0], [2.0 * t], [2.0 - 3.0 * t]])
L = line_gen_num(pt(-1.0), pt(2.0), 60)
P = np.array([[-1.0], [5.0], [2.0]])
H = np.array([[2.5], [1.0], [0.5]])
Pi = np.array([[6.0], [-3.0], [-1.0]])

fig = plt.figure(figsize=(7, 6))
ax = fig.add_subplot(projection='3d')
ax.plot(L[0, :], L[1, :], L[2, :], 'k-', linewidth=2, label='given line')
s = line_gen_num(P, Pi, 30)
ax.plot(s[0, :], s[1, :], s[2, :], 'r--', linewidth=1.5, label="P P'")
for name, X in [('P(-1,5,2)', P), ('H(5/2,1,1/2)', H), ("P'(6,-3,-1)", Pi)]:
    ax.scatter(X[0], X[1], X[2], s=40)
    ax.text(X[0, 0], X[1, 0], X[2, 0], name)
ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_zlabel('z')
ax.set_title("Image P' of P in the line (H = foot of the perpendicular)")
ax.legend()
plt.savefig('../figs/c12_q35B.png', dpi=200, bbox_inches='tight')
