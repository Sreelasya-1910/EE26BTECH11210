# Q32(A): Numerical midpoint Riemann approximation for integral
# (x^2+1)/((x^2+2)(2x^2+1)) dx over [0, 1], for illustration.
def f(x):
    return (x*x+1)/((x*x+2)*(2*x*x+1))

def midpoint_riemann(a,b,n):
    dx=(b-a)/n
    return dx*sum(f(a+(i+0.5)*dx) for i in range(n))

a,b,n=0.0,1.0,100_000
print("Midpoint Riemann approximation:", midpoint_riemann(a,b,n))
