# Q32(B): Numerical integration of x*tan(x)/(sec(x)+tan(x)).
# The endpoint x=pi/2 is singular in the raw expression, so midpoint sampling
# avoids evaluating the endpoint directly.
import math

def f(x):
    return x*math.tan(x)/(1/math.cos(x)+math.tan(x))

def midpoint_riemann(a,b,n):
    dx=(b-a)/n
    total=0.0
    for i in range(n):
        total += f(a+(i+0.5)*dx)
    return total*dx

a,b,n=0.0,math.pi/2-1e-6,100_000
print("Midpoint Riemann approximation:", midpoint_riemann(a,b,n))
