# Q34: Solve y' = cos(x) - 2y using Laplace transform.
# General solution: y = C*exp(-2x) + (2*cos(x)+sin(x))/5.
import sympy as sp
x = sp.symbols('x', real=True)
C = sp.symbols('C')
y = C*sp.exp(-2*x) + (2*sp.cos(x)+sp.sin(x))/5
print("General solution y(x) =", y)
print("Check y' - (cos(x)-2y) =", sp.simplify(sp.diff(y,x) - (sp.cos(x)-2*y)))
