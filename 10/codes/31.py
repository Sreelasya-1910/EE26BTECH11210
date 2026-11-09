import numpy as np

# Q31(b): points dividing AB into four equal parts
# A + (k/4)(B - A) = (1 - k/4) A + (k/4) B = [A B] [1 - k/4; k/4],  k = 1, 2, 3
A = np.array([[-2.0], [2.0]])
B = np.array([[2.0], [8.0]])

AB = np.hstack((A, B))                                   # columns A and B
W = np.array([[1 - k / 4 for k in (1, 2, 3)],
              [k / 4 for k in (1, 2, 3)]])               # one column of weights per k

points = AB @ W                                          # columns give the points
print("[A B] =\n", AB)
print("W =\n", W)
print("[P1 P2 P3] =\n", points)

# check against A + (k/4)(B - A) and the mid-point (A + B)/2
for k in (1, 2, 3):
    print(f"k = {k}:", (A + (k / 4) * (B - A)).ravel())
print("mid-point (A + B)/2 =", ((A + B) / 2).ravel())
