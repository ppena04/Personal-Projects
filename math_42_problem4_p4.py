import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

# Parameters
p0 = 100
r_best = 0.01676
years = 25
target = 200  # desired population 

# Function for adaptive stabilize-to-target strategy
def stabilize_to_target(p0, r, years, target, add_frac=0.05, remove_frac=0.05):
    pop = [p0]
    for i in range(years):
        grown = pop[-1] * (1 + r)
        if grown < target:
            # add proportionally to the gap
            next_pop = grown + add_frac * (target - grown)
        else:
            # remove a fraction of the excess
            next_pop = grown - remove_frac * (grown - target)
        if next_pop < 0:
            next_pop = 0
        pop.append(next_pop)
    return np.array(pop)

# Run the simulation
P_stable = stabilize_to_target(p0, r_best, years, target)

# time axis
current_year = datetime.now().year
years_axis = [current_year + i for i in range(years + 1)]

# Plot 
plt.figure(figsize=(8,5))
plt.plot(years_axis, P_stable, 'k-', label='Adaptive strategy to ~200')
plt.axhline(target, color='gray', linestyle='--', label='Target = 200')
plt.title("Bobcat Population Stabilizing Around 200 (Best Conditions)")
plt.xlabel("Year")
plt.ylabel("Population Size")
plt.legend()
plt.grid(True, linestyle=':', color='gray', alpha=0.6)
plt.tight_layout()
plt.show()

''' 
Here the population starts at 100 animals. The natural growth rate is 1.676% per year. The simulation runs for 25 years and
we want to hit a target population of 200 animals. We implement the  stabilize_to_target function that is our stabilization strategy.
This is meant to add or remove animals based on how far the current population is from the target population. Once we reach 200, the
population should start to slow down by removing a small percentage of animals over time, which is what is happening in this model.
'''