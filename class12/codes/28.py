# Q28: Differentiate y=sqrt(log(sin(x^3/3 - 1))) symbolically.
import sympy as sp
x = sp.symbols('x', real=True)
u = x**3/3 - 1
y = sp.sqrt(sp.log(sp.sin(u)))
print("dy/dx =", sp.simplify(sp.diff(y, x)))
