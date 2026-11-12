from pathlib import Path
import sys
import numpy as np
import matplotlib.pyplot as plt

from CoordGeo.plotting.funcs import label_pts

# Polynomial p(y) = 7y^2 - (11/3)y - 2/3
y = np.linspace(-0.5, 1.0, 500)
p = 7*y**2 - (11/3)*y - 2/3

# Roots
root1 = 2/3
root2 = -1/7

plt.figure(figsize=(8, 5))
plt.plot(y, p, label=r'$p(y)=7y^2-\frac{11}{3}y-\frac{2}{3}$')
plt.axhline(0, color="black")
plt.axvline(0, color="black")

# Use CoordGeo's point-labeling function
label_pts(
    np.array([[root1, 0], [root2, 0]]).T,
    [r'$2/3$', r'$-1/7$']
)

plt.scatter([root1, root2], [0, 0])
plt.xlabel("y")
plt.ylabel("p(y)")
plt.title("Zeroes of the Polynomial")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("q6.png", dpi=200)

