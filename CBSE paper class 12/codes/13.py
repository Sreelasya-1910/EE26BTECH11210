# Q13: Numerical checks of the integral identities from the paper.
# These are illustrative numerical tests, not a replacement for proofs.
import scipy.integrate as si

def f(x):
    return x*x + 1

a, b = -2.0, 3.0
lhs = si.quad(f, a, b)[0]
rhs = si.quad(lambda x: f(a+b-x), a, b)[0]
print("Option A: integral f(x) vs f(a+b-x):", lhs, rhs, "equal:", abs(lhs-rhs)<1e-8)

# For an even function, integral from -a to a is generally NOT zero.
a = 2.0
even_integral = si.quad(lambda x: x*x, -a, a)[0]
print("Option B counterexample (even f=x^2):", even_integral)

# For an odd function, integral from -a to a is zero, not generally 2*integral_0^a.
odd_lhs = si.quad(lambda x: x, -a, a)[0]
odd_rhs = 2*si.quad(lambda x: x, 0, a)[0]
print("Option C counterexample (odd f=x):", odd_lhs, odd_rhs)
