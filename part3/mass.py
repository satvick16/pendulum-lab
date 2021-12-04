import matplotlib.pyplot as plt
from math import pi, sqrt
import numpy as np

plt.style.use("bmh")

experimental = {92: 1.455333333,
                56: 1.462666667,
                35: 1.444,
                28: 1.436666667,
                21: 1.436666667,
                14: 1.466666667,
                7: 1.436}

L = 0.55
base = 2*pi*sqrt(L/9.8)

mass = np.array([92, 56, 35, 28, 21, 14, 7])
residuals = []

for key, value in experimental.items():
    residuals.append(abs(base - value))

m, b = np.polyfit(mass, residuals, 1)

plt.subplot(2, 1, 1)
plt.scatter(mass, residuals, label="residuals")
plt.title("Residuals against predicted model (T = 2*pi*sqrt(L/g))")
plt.xlabel("Mass (grams)")
plt.xlabel("Period (seconds)")

plt.subplot(2, 1, 2)
plt.scatter(list(experimental.keys()), list(
    experimental.values()), label="raw data")
plt.title("Period vs. mass")
plt.ylim(0, 2)
plt.xlabel("Mass (grams)")
plt.xlabel("Period (seconds)")

plt.tight_layout()

plt.show()
