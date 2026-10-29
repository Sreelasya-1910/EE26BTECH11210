# Q12: Simplifies to integral of x**3 for x>0, x != 1.
# Midpoint Riemann sum for the definite integral from 2 to 4.
def f(x):
    return x**3

def midpoint_riemann(a, b, n):
    dx = (b-a)/n
    return dx * sum(f(a+(i+0.5)*dx) for i in range(n))

a, b, n = 2.0, 4.0, 100_000
approx = midpoint_riemann(a, b, n)
exact = (b**4-a**4)/4
print("Midpoint Riemann sum:", approx)
print("Exact integral:", exact)  # 60
print("Absolute error:", abs(approx-exact))
