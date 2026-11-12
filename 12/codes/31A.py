import numpy as np
import sympy as sp

# Q31(A): a = (1,-1,2), b = (2,-4,5), c = (lam,-2,-3); a . (b + c)/|b + c| = 1
lam = sp.symbols('lam', real=True)
a = sp.Matrix([1, -1, 2])
b = sp.Matrix([2, -4, 5])
c = sp.Matrix([lam, -2, -3])
s = b + c

# a^T s = |s|, squaring gives a linear equation in lam; keep roots with a^T s > 0
candidates = sp.solve(sp.Eq((a.T * s)[0] ** 2, s.dot(s)), lam)
roots = [r for r in candidates if (a.T * s)[0].subs(lam, r) > 0]
print("lambda =", roots)

lam0 = float(roots[0])
s0 = np.array([2 + lam0, -6.0, 2.0])
print("a . unit(b + c) =", np.array([1.0, -1.0, 2.0]) @ s0 / np.linalg.norm(s0))
