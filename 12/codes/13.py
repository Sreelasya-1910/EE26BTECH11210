import numpy as np

# Q13: decide which statement is correct using boolean logic.
# Each statement is tested on sample functions; trapezoidal rule for the integrals.


def trapezoid(f, a, b, n=20000):
    x = np.linspace(a, b, n + 1)
    y = f(x)
    h = (b - a) / n
    return h * (0.5 * y[0] + y[1:-1].sum() + 0.5 * y[-1])


def implies(p, q):
    return (not p) or q


close = lambda u, v: bool(np.isclose(u, v, atol=1e-6))

a, b = -2.0, 3.0

# (A) integral f(x) = integral f(a+b-x) : tested on several functions
tests = [lambda x: x**2 + 1, lambda x: np.exp(x), lambda x: np.sin(x) + x**3]
A = all(close(trapezoid(f, a, b), trapezoid(lambda x, f=f: f(a + b - x), a, b))
        for f in tests)

# (B) f even => integral_{-a}^{a} f = 0 : tested with f(x) = x^2
f = lambda x: x**2
is_even = True
B = implies(is_even, close(trapezoid(f, -1, 1), 0.0))

# (C) f odd => integral_{-a}^{a} f = 2 integral_0^a f : tested with f(x) = x
f = lambda x: x
is_odd = True
C = implies(is_odd, close(trapezoid(f, -1, 1), 2 * trapezoid(f, 0, 1)))

# (D) integral_0^{2a} f = integral_0^a f - integral_0^a f(2a+x) : tested with f(x) = x, a = 1
f = lambda x: x
D = close(trapezoid(f, 0, 2),
          trapezoid(f, 0, 1) - trapezoid(lambda x: f(2 + x), 0, 1))

for name, value in zip("ABCD", (A, B, C, D)):
    print(f"Statement ({name}) is", value)
print("Correct statement(s):", [n for n, v in zip("ABCD", (A, B, C, D)) if v])
