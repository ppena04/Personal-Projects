

import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

# Parameters
p0 = 100
r_worst = -0.045
years = 25

# Function for adaptive stabilize-to-target strategy
def stabilize_to_target_worst(p0, r, years, target, add_frac=0.05, remove_frac=0.05):
    pop = [p0]
    for i in range(years):
        grown = pop[-1] * (1 + r)
        if grown < target:
            # add proportionally 
            next_pop = grown + add_frac * (target - grown)
        else:
            # remove a fraction
            next_pop = grown - remove_frac * (grown - target)
        if next_pop < 0:
            next_pop = 0
        pop.append(next_pop)
    return np.array(pop)

# Simulate stabilization at 50
P_50 = stabilize_to_target_worst(p0, r_worst, years, target=50)

# Simulate stabilization at 200
P_200 = stabilize_to_target_worst(p0, r_worst, years, target=200)

# Prepare time axis
current_year = datetime.now().year
years_axis = [current_year + i for i in range(years + 1)]

# Plot the results
plt.figure(figsize=(8,5))
plt.plot(years_axis, P_50, 'k-', label='Stabilize at 50')
plt.axhline(50, color='gray', linestyle='--', label='Target = 50')
plt.plot(years_axis, P_200, 'k--', label='Stabilize at 200')
plt.axhline(200, color='gray', linestyle=':', label='Target = 200')
plt.title("Bobcat Population Stabilization (Worst Conditions)")
plt.xlabel("Year")
plt.ylabel("Population Size")
plt.legend()
plt.grid(True, linestyle=':', color='gray', alpha=0.6)
plt.tight_layout()
plt.show()

''' 
Under worst conditions, the environment alone cannot sustain the population, as it would decline toward extinction.
The adaptive management strategy can stabilize the population at different desired levels (50 or 200), but:
Achieving a higher target of 200 requires much more continuous intervention. The lower target (50) stabilizes faster 
because it requires less compensation against the negative growth.
'''
