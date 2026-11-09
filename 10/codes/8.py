import numpy as np

# Q8: rectangle AOBC with A(0,2), O(0,0), B(4,0); diagonal AB
A = np.array([0.0, 2.0])
B = np.array([4.0, 0.0])

d = B - A
print("AB =", d)
print("|AB|^2 =", d @ d)          # (B-A)^T (B-A)
