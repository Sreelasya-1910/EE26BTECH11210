# Q32(B): trapezoidal rule for the integral of x tan x/(sec x + tan x) over [0, pi].
# tan x/(sec x + tan x) = sin x/(1 + sin x), which removes the singularity at pi/2.
import math


def g(x):
    return x * math.sin(x) / (1.0 + math.sin(x))


def trapezoid(f, a, b, n):
    h = (b - a) / n
    s = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        s += f(a + i * h)
    return h * s


a, b = 0.0, math.pi
exact = math.pi * (math.pi - 2) / 2
for n in (4, 12, 100, 1000):
    T = trapezoid(g, a, b, n)
    print(f"n = {n:5d}  T = {T:.8f}  error = {abs(T - exact):.2e}")
print("Exact value pi(pi-2)/2 =", exact)
