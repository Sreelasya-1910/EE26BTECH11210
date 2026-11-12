import numpy as np

# Q2: f(x) = acos(x) + sin(x); scan x and keep the points where f is a real number
x = np.linspace(-3, 3, 6001)
with np.errstate(invalid="ignore"):
    f = np.arccos(x) + np.sin(x)

in_domain = ~np.isnan(f)
print("Domain found from", x[in_domain].min(), "to", x[in_domain].max())
