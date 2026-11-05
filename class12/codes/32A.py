# Q32(A): trapezoidal rule for the integral of (x^2+1)/((x^2+2)(2x^2+1)) over [0, 1].
import math


def f(x):
    return (x * x + 1) / ((x * x + 2) * (2 * x * x + 1))


def trapezoid(f, a, b, n):
    h = (b - a) / n
    s = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        s += f(a + i * h)
    return h * s


a, b = 0.0, 1.0
# F(x) = (atan(x/sqrt2) + atan(sqrt2 x)) / (3 sqrt2), so F(1) - F(0) = pi / (6 sqrt2)
exact = math.pi / (6 * math.sqrt(2))
for n in (2, 10, 100, 1000):
    T = trapezoid(f, a, b, n)
    print(f"n = {n:5d}  T = {T:.8f}  error = {abs(T - exact):.2e}")
print("Exact value pi/(6 sqrt2) =", exact)
