# Q23(A): Differentiate y=5^x/x^5 symbolically.
import sympy as sp
x = sp.symbols('x', positive=True)
y = 5**x / x**5
print("y =", y)
print("dy/dx =", sp.simplify(sp.diff(y, x)))
