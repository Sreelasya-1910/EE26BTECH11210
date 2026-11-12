# Q5: |2AB| for 3x3 matrices A, B with |A| = 3 and |B| = 5.
# matgeo: the characteristic polynomial is f(lambda) = |M - lambda I|, so |M| = f(0).
# numpy's poly(M) returns the coefficients of det(lambda I - M) = (-1)^n f(lambda).
import numpy as np
import numpy.linalg as LA


def det_from_poly(M):
    n = M.shape[0]
    f = np.poly(M)                 # [1, -s1, s2, -s3] for n = 3
    return (-1) ** n * f[-1]       # |M| = (-1)^n * constant term


# example matrices with |A| = 3 and |B| = 5
A = np.array([[1, 1, 0], [0, 1, 1], [1, 0, 2]])
B = np.array([[1, -1, -1], [-1, 1, 0], [2, 3, 1]])
M = 2 * A @ B

print("|A| =", round(det_from_poly(A)))
print("|B| =", round(det_from_poly(B)))
print("|2AB| from characteristic polynomial =", round(det_from_poly(M)))
print("|2AB| as product of eigenvalues      =", round(np.prod(LA.eigvals(M)).real))
print("2^3 |A| |B|                          =", 2 ** 3 * 3 * 5)
