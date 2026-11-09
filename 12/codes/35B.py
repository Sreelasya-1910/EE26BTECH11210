import numpy as np

# Q35(B): image of P = (-1,5,2) in the line x = A + k m, A = (2,0,2), m = (1,2,-3)
P = np.array([-1.0, 5.0, 2.0])
A = np.array([2.0, 0.0, 2.0])
m = np.array([1.0, 2.0, -3.0])

k = m @ (P - A) / (m @ m)       # foot of the perpendicular: m^T (A + k m - P) = 0
H = A + k * m
P_image = 2 * H - P             # H is the mid-point of P P'

print("k =", k)
print("H  =", H)
print("P' =", P_image)
print("PP' =", np.linalg.norm(P_image - P), " sqrt(122) =", np.sqrt(122))
