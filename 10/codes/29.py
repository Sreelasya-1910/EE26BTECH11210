# Q29: angle PCA = 110 degrees, AB a diameter.
angle_PCA = 110.0
angle_ACB = 90.0                       # angle in a semicircle
angle_PCB = angle_PCA - angle_ACB      # P lies beyond B
angle_CAB = angle_PCB                  # tangent-chord theorem
angle_CBA = 90.0 - angle_CAB
angle_BCO = angle_CBA                  # OB = OC

print("angle PCB =", angle_PCB)
print("angle CAB =", angle_CAB)
print("angle CBA =", angle_CBA)
print("angle BCO =", angle_BCO)
