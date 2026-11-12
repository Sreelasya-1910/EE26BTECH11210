import numpy as np

# Q5: sin(4 theta) = sqrt(3)/2, principal value 4 theta = 60 degrees
four_theta = np.degrees(np.arcsin(np.sqrt(3) / 2))
theta = four_theta / 4
print("4 theta =", four_theta)
print("theta   =", theta)
print("theta/3 =", theta / 3)
