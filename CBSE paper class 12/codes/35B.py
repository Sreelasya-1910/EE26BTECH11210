# Q35(B): Reflection of P=(-1,5,2) in the line (2x-4)/2 = y/2 = (2-z)/3.
import sympy as sp
P = sp.Matrix([-1,5,2])
A = sp.Matrix([2,0,2])   # point on line when parameter = 0
v = sp.Matrix([1,1,-3])  # direction vector
# Projection foot H = A + t*v, where t = ((P-A).v)/(v.v)
t = ((P-A).dot(v))/(v.dot(v))
H = A + t*v
P_reflected = 2*H - P
print("Foot of perpendicular H =", H)
print("Image point =", P_reflected)
print("Distance P to image =", sp.sqrt((P_reflected-P).dot(P_reflected-P)))
