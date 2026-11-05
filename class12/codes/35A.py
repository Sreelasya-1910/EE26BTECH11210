# Q35(A): Parametrize line and solve for points at distance 3*sqrt(2) from P=(1,2,3).
import sympy as sp
t = sp.symbols('t', real=True)
# (2x+4)/6 = (y+1)/2 = (-2z+6)/(-4) = t
x, y, z = 3*t-2, 2*t-1, 2*t-3
distance_sq = sp.expand((x-1)**2 + (y-2)**2 + (z-3)**2)
print("Distance squared expression:", distance_sq)
print("Solve distance^2 = 18:", sp.solve(sp.Eq(distance_sq, 18), t))
print("Corresponding points:", [(sp.simplify(x.subs(t,v)), sp.simplify(y.subs(t,v)), sp.simplify(z.subs(t,v))) for v in sp.solve(sp.Eq(distance_sq,18),t)])
