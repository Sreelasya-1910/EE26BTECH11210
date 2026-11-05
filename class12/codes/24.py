# Q24: Graph and corner points for maximize Z=5x+4y, 3x+y<=6, x<=1, x,y>=0.
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2.5, 500)
y1 = 6 - 3*x
y2 = np.full_like(x, np.nan)
plt.plot(x, y1, label="3x + y = 6")
plt.axvline(1, label="x = 1")
plt.axhline(0, linewidth=0.8)
plt.axvline(0, linewidth=0.8)
# Feasible polygon vertices: (0,0), (1,0), (1,3), (0,6)
px = [0, 1, 1, 0]
py = [0, 0, 3, 6]
plt.fill(px, py, alpha=0.25, label="Feasible region")
for a,b in zip(px,py):
    plt.scatter(a,b)
    plt.annotate(f"({a},{b})",(a,b))
plt.xlim(-0.2, 2.2); plt.ylim(-0.2, 7)
plt.xlabel("x"); plt.ylabel("y"); plt.title("Q24: Feasible region")
plt.grid(True); plt.legend(); plt.tight_layout()
plt.savefig("24.png", dpi=160)
plt.show()
