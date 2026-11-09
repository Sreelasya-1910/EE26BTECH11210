import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Read the output of 27.c: label, simulated frequency, pmf
labels, sim, pmf = [], [], []
for line in open("27.dat"):
    name, s, p = line.split()
    labels.append(name)
    sim.append(float(s))
    pmf.append(float(p))

x = np.arange(len(labels))
shift = 0.06

fig, ax = plt.subplots(figsize=(7, 4))
ax.stem(x - shift, sim, linefmt="C0-", markerfmt="C0o", basefmt=" ", label="simulation")
ax.stem(x + shift, pmf, linefmt="C1-", markerfmt="C1s", basefmt=" ", label="pmf")
ax.set_ylim(0, 1.3 * max(max(sim), max(pmf)))
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_xlabel("eye colour")
ax.set_ylabel("probability")
ax.set_title("pmf of the eye colour: simulation vs exact")
ax.grid(True, axis="y")
ax.legend(loc="upper center", ncol=2)
plt.savefig("../figs/q27.png", dpi=200, bbox_inches="tight")
