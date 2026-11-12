import itertools
import numpy as np

# Q3: generate every 3x3 matrix whose entries are 2 or 3 and count them in the loop
count = 0
matrices = set()
for entries in itertools.product([2, 3], repeat=9):
    A = np.array(entries).reshape(3, 3)
    matrices.add(A.tobytes())
    count += 1

print("Number of matrices counted in the loop =", count)
print("Number of distinct matrices            =", len(matrices))
