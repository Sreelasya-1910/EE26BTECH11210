import math

# Q32(B): integral of x tan x/(sec x + tan x) over [0, pi]
# tan x/(sec x + tan x) = sin x/(1 + sin x)


def g(x):
    return x * math.sin(x) / (1.0 + math.sin(x))


# Trapezoidal rule as a difference equation:
#   I[n+1] = I[n] + (h/2)(g(x[n]) + g(x[n+1])),  I[0] = 0,  x[n] = a + n h
a, b = 0.0, math.pi
exact = math.pi * (math.pi - 2) / 2

for N in (4, 12, 100, 1000):
    h = (b - a) / N
    I = 0.0
    for n in range(N):
        I = I + (h / 2) * (g(a + n * h) + g(a + (n + 1) * h))
    print(f"N = {N:5d}  I[N] = {I:.8f}  error = {abs(I - exact):.2e}")

print("Exact value pi(pi-2)/2 =", exact)
