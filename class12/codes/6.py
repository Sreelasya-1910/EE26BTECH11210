# Q6: |adj A| for a 3x3 matrix A with |A| = 5.
# matgeo: Cayley-Hamilton, f(A) = 0 with f(lambda) = |A - lambda I|.
import numpy as np
import numpy.linalg as LA
from CoordGeo.matrix.funcs import polyvalm

# example matrix with |A| = 5
A = np.array([[1, -1, -1], [-1, 1, 0], [2, 3, 1]])

f = np.poly(A)                     # lambda^3 - s1 lambda^2 + s2 lambda - s3
s1, s2, s3 = -f[1], f[2], -f[3]    # trace, sum of principal 2x2 minors, |A|
print("s1, s2, |A| =", s1, s2, s3)

# Cayley-Hamilton: A^3 - s1 A^2 + s2 A - s3 I = 0
print("f(A) =\n", polyvalm(f, A).round(9))

# A (A^2 - s1 A + s2 I) = |A| I, hence adj A = A^2 - s1 A + s2 I
adjA = polyvalm([1, -s1, s2], A)
print("A adj(A) =\n", (A @ adjA).round(9))

# eigenvalues of adj A are |A| / lambda_i, so |adj A| = |A|^3 / |A| = |A|^2
print("|adj A| =", round(np.prod(LA.eigvals(adjA)).real))
print("|A|^2   =", round(s3) ** 2)
