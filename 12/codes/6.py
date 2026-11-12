import numpy as np

# Q6: A adj(A) = |A| I  =>  |A| |adj A| = |A|^3  =>  |adj A| = |A|^2  (order 3)
# Check on an example 3x3 matrix with |A| = 5
A = np.array([[1, -1, -1], [-1, 1, 0], [2, 3, 1]])
detA = round(np.linalg.det(A))

# adj(A) from the cofactors: adj(A)[j][i] = (-1)^(i+j) * minor(i, j)
adj = np.zeros((3, 3))
for i in range(3):
    for j in range(3):
        minor = np.delete(np.delete(A, i, axis=0), j, axis=1)
        adj[j, i] = (-1) ** (i + j) * np.linalg.det(minor)

print("|A| =", detA)
print("A adj(A) =\n", (A @ adj).round(6))
print("|adj A| =", round(np.linalg.det(adj)), " |A|^2 =", detA ** 2)
