import numpy as np

# Q38: lighthouse AB = 50 m, angles of depression 30 deg (P) and 45 deg (Q)
A = np.array([0.0, 0.0])
B = np.array([0.0, 50.0])
e2 = np.array([0.0, 1.0])


def ground_point(theta_deg):
    th = np.deg2rad(theta_deg)
    m = np.array([np.cos(th), -np.sin(th)])     # line of sight from B
    lam = -(e2 @ B) / (e2 @ m)                  # e2^T (B + lam m) = 0
    return B + lam * m


P = ground_point(30)
Q = ground_point(45)

print("P =", P.round(4), " Q =", Q.round(4))
print("QA =", np.linalg.norm(Q - A))
print("PQ =", np.linalg.norm(P - Q))
print("Speed =", (np.linalg.norm(Q - A) / 1000) / (10 / 60), "km/h")
