# Q14: integral of e^x / sqrt(4 - e^(2x)) dx = asin(e^x / 2) + C.
# Trapezoidal rule over [-1, 0], where e^x < 2.
import math


def f(x):
    return math.exp(x) / math.sqrt(4.0 - math.exp(2.0 * x))


def trapezoid(f, a, b, n):
    h = (b - a) / n
    s = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        s += f(a + i * h)
    return h * s


a, b = -1.0, 0.0
exact = math.asin(math.exp(b) / 2.0) - math.asin(math.exp(a) / 2.0)
for n in (4, 40, 400, 4000):
    T = trapezoid(f, a, b, n)
    print(f"n = {n:5d}  T = {T:.8f}  error = {abs(T - exact):.2e}")
print("Exact value:", exact)
