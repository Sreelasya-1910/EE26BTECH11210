# Q12: the integrand simplifies to x^3 for x > 0, x != 1.
# Trapezoidal rule for the definite integral from 2 to 4 of the original integrand.
import math


def f(x):
    return (math.exp(9 * math.log(x)) - math.exp(8 * math.log(x))) / \
           (math.exp(6 * math.log(x)) - math.exp(5 * math.log(x)))


def trapezoid(f, a, b, n):
    h = (b - a) / n
    s = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        s += f(a + i * h)
    return h * s


a, b = 2.0, 4.0
exact = (b ** 4 - a ** 4) / 4          # x^4/4 evaluated from 2 to 4 = 60
for n in (4, 40, 400, 4000):
    T = trapezoid(f, a, b, n)
    print(f"n = {n:5d}  T = {T:.6f}  error = {abs(T - exact):.2e}")
print("Exact integral:", exact)
