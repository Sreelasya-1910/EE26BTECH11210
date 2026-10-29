import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Import custom modules
from CoordGeo.line.funcs import line_gen, line_gen_num
from CoordGeo.plotting.funcs import label_pts

# line: x = 3t - 2, y = 2t - 1, z = 2t + 3
pt = lambda t: np.array([[3 * t - 2], [2 * t - 1], [2 * t + 3]])
L = line_gen_num(pt(-0.6), pt(2.4), 60)
P = np.array([[1.0], [2.0], [3.0]])
Q1 = pt(0.0); Q2 = pt(30.0 / 17.0)

fig = plt.figure(figsize=(7, 6))
ax = fig.add_subplot(projection='3d')
ax.plot(L[0, :], L[1, :], L[2, :], 'k-', linewidth=2, label='given line')
for Q in (Q1, Q2):
    s = line_gen_num(P, Q, 20)
    ax.plot(s[0, :], s[1, :], s[2, :], 'r--', linewidth=1)
for name, X in [('P(1,2,3)', P), ('Q1(-2,-1,3)', Q1), ('Q2(3.29,2.53,6.53)', Q2)]:
    ax.scatter(X[0], X[1], X[2], s=40)
    ax.text(X[0, 0], X[1, 0], X[2, 0], name)
ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_zlabel('z')
ax.set_title('Points on the line at distance 3*sqrt(2) from P')
ax.legend()
plt.savefig('../figs/c12_q35A.png', dpi=200, bbox_inches='tight')
