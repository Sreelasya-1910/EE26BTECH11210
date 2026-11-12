import sympy as sp

# Q32(a): AP with d = 2, nth term 4 (index of last term m = n - 1), sum of n terms -14.
# x[n] = (a + n d) u[n]  has the z-transform (w = z^-1)
#   X = a/(1-w) + d w/(1-w)^2
# and the running sum y = x * u has Y = X/(1-w).
w, a, d = sp.symbols('w a d')
X = a / (1 - w) + d * w / (1 - w) ** 2
Y = sp.simplify(X / (1 - w))

# y[n] is the coefficient of w^n in Y
series = sp.series(Y, w, 0, 8).removeO()
y = lambda n: sp.expand(series.coeff(w, n))
print("y[n] for n = 0..3:", [y(n) for n in range(4)])

# Matches y[n] = (n+1) a + n(n+1) d / 2
n = sp.symbols('n')
formula = (n + 1) * a + n * (n + 1) * d / 2
print("formula check:", all(sp.simplify(y(k) - formula.subs(n, k)) == 0 for k in range(8)))

# Last term x[m] = a + m d = 4 with d = 2, and y[m] = -14
m = sp.symbols('m', integer=True, nonnegative=True)
a_m = 4 - 2 * m
sol = sp.solve(sp.Eq(formula.subs({a: a_m, d: 2, n: m}), -14), m)
print("m =", sol, "-> number of terms =", [s + 1 for s in sol])
m0 = sol[0]
print("a =", a_m.subs(m, m0))
print("S_20 = y[19] =", formula.subs({a: a_m.subs(m, m0), d: 2, n: 19}))
