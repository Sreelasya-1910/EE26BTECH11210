# Q14: Integral e^x/sqrt(4-e^(2x)) dx = asin(e^x/2) + C.
# Midpoint Riemann approximation for a definite integral where e^x < 2.
import math

def f(x):
    return math.exp(x) / math.sqrt(4.0 - math.exp(2.0*x))

def midpoint_riemann(a, b, n):
    dx = (b-a)/n
    total = 0.0
    for i in range(n):
        total += f(a+(i+0.5)*dx)
    return total*dx

a, b, n = -1.0, 0.0, 100_000
approx = midpoint_riemann(a, b, n)
exact = math.asin(math.exp(b)/2.0) - math.asin(math.exp(a)/2.0)
print("Midpoint Riemann sum:", approx)
print("Exact value:", exact)
print("Absolute error:", abs(approx-exact))
