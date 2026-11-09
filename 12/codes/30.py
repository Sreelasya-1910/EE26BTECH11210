import itertools
import numpy as np
import cvxpy as cp

# Q30: minimise Z = 18x + 10y subject to 4x + y >= 20, 2x + 3y >= 30, x >= 0, y >= 0
# Constraints written as A v <= b with v = (x, y)
A = np.array([[-4.0, -1.0], [-2.0, -3.0], [-1.0, 0.0], [0.0, -1.0]])
b = np.array([-20.0, -30.0, 0.0, 0.0])
c = np.array([18.0, 10.0])

# Step 1: the feasible region is convex (each row is a half-plane).
# Numerical check: convex combinations of feasible points stay feasible.
rng = np.random.default_rng(0)
pts = rng.uniform([0.0, 0.0], [20.0, 30.0], size=(4000, 2))
feasible = pts[np.all(A @ pts.T <= b[:, None], axis=0)]
convex = True
for _ in range(2000):
    u, w = feasible[rng.integers(len(feasible), size=2)]
    t = rng.uniform()
    convex &= bool(np.all(A @ (t * u + (1 - t) * w) <= b + 1e-9))
print("Convex combinations stay feasible:", convex)

# Step 2: corner points = feasible intersections of two boundary lines
corners = []
for i, j in itertools.combinations(range(len(b)), 2):
    M = A[[i, j]]
    if np.linalg.matrix_rank(M) == 2:
        v = np.linalg.solve(M, b[[i, j]])
        if np.all(A @ v <= b + 1e-9) and not any(np.allclose(v, q) for q in corners):
            corners.append(v)

print("Corner points and Z = 18x + 10y:")
for v in corners:
    print("  ", (v + 0.0).round(4), " Z =", round(float(c @ v), 4))

# Step 3: the problem is convex, so let cvxpy optimise
x = cp.Variable()
y = cp.Variable()
constraints = [4 * x + y >= 20,
               2 * x + 3 * y >= 30,
               x >= 0,
               y >= 0]
objective = cp.Minimize(18 * x + 10 * y)
problem = cp.Problem(objective, constraints)
problem.solve()

print("status:", problem.status)
print("(x, y) =", round(float(x.value), 4), round(float(y.value), 4))
print("Z min  =", round(float(problem.value), 4))
