import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

# Parameters
p_0 = 100  # initial population
years = 10  # years

# Growth rates for each environmental condition
r_best = 0.01676
r_medium = 0.00549
r_worst = -0.04500

# Growth
P_best = [p_0]
P_medium = [p_0]
P_worst = [p_0]

# Population models: P(t) = P(t) * (1 + r)
for _ in range(years):
    P_best.append(P_best[-1] * (1 + r_best))
    P_medium.append(P_medium[-1] * (1 + r_medium))
    P_worst.append(P_worst[-1] * (1 + r_worst))

# Generate years on x-axis starting from current year
current_year = datetime.now().year
year_labels = [current_year + i for i in range(years + 1)]

# Plot the model
plt.figure(figsize=(8,5))
plt.plot(year_labels, P_best, 'k-', label='Best (r = 0.01676)')      # solid black
plt.plot(year_labels, P_medium, 'k--', label='Medium (r = 0.00549)') # dashed
plt.plot(year_labels, P_worst, 'k:', label='Worst (r = -0.04500)')   # dotted

plt.title("Simulated Bobcat Populations Over 10 Years")
plt.xlabel("Year")
plt.ylabel("Population Size")
plt.legend()
plt.grid(True, linestyle=':', color='gray', alpha=0.6)
plt.tight_layout()
plt.show()
