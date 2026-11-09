import numpy as np

# Q1: tangents PA and PB, angle APB = 80 degrees; r = d cos(phi), phi = angle POA.
# Unit directions of PA and PB are (-sin(phi), +-cos(phi)), so cos(APB) = -cos(2 phi).
r = 2.0
apb = np.deg2rad(80.0)
phi = 0.5 * np.arccos(-np.cos(apb))
d = r / np.cos(phi)

O = np.array([0.0, 0.0])
P = np.array([d, 0.0])
A = r * np.array([np.cos(phi), np.sin(phi)])
B = r * np.array([np.cos(phi), -np.sin(phi)])

# Radius is perpendicular to the tangent: (A - O)^T (A - P) = 0
print("Angle POA =", np.degrees(phi))
print("P =", P.round(4), " A =", A.round(4), " B =", B.round(4))
print("OA.PA =", (A - O) @ (A - P), " OB.PB =", (B - O) @ (B - P))

u, w = A - P, B - P
print("Angle APB from coordinates =",
      np.degrees(np.arccos(u @ w / (np.linalg.norm(u) * np.linalg.norm(w)))))
