import numpy as np

# Q11: B(0,0), C(16,0), D(12,0), A(12,h), angle BAC = 90 degrees
BC, DC = 16.0, 4.0
BD = BC - DC
B = np.array([0.0, 0.0])
C = np.array([BC, 0.0])
D = np.array([BD, 0.0])

# (B-A)^T (C-A) = -BD*DC + h^2 = 0
h = np.sqrt(BD * DC)
A = np.array([BD, h])

print("A =", A.round(4))
print("(B-A)^T (C-A) =", (B - A) @ (C - A))
print("AC =", np.linalg.norm(C - A))
