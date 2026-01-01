import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

# Parameters
p0 = 100
r_worst = -0.045
years_short = 10
years_long = 25

# simulate discrete growth with addition
def discrete_addition(p0, r, years, add_type, add_value):
    pop = [p0]
    for i in range(years):
        grown = pop[-1] * (1 + r)
        if add_type == "fixed":
            next_pop = grown + add_value
        elif add_type == "percent":
            next_pop = grown + add_value * pop[-1]
        if next_pop < 0:
            next_pop = 0
        pop.append(next_pop)
    return np.array(pop)

# Simulate addition strategies for 10 years
add_strategies_10 = {
    "Add 3 per year": discrete_addition(p0, r_worst, years_short, "fixed", 3),
    "Add 10 per year": discrete_addition(p0, r_worst, years_short, "fixed", 10),
    "Add 1% per year": discrete_addition(p0, r_worst, years_short, "percent", 0.01),
    "Add 5% per year": discrete_addition(p0, r_worst, years_short, "percent", 0.05),
}

# Simulate addition strategies for 25 years
add_strategies_25 = {
    "Add 3 per year": discrete_addition(p0, r_worst, years_long, "fixed", 3),
    "Add 10 per year": discrete_addition(p0, r_worst, years_long, "fixed", 10),
    "Add 1% per year": discrete_addition(p0, r_worst, years_long, "percent", 0.01),
    "Add 5% per year": discrete_addition(p0, r_worst, years_long, "percent", 0.05),
}

# Prepare time axes
current_year = datetime.now().year
years_10 = [current_year + i for i in range(years_short + 1)]
years_25 = [current_year + i for i in range(years_long + 1)]

# Plot 10-year simulation
plt.figure(figsize=(8,5))
for label, P in add_strategies_10.items():
    plt.plot(years_10, P, label=label)
plt.title("Bobcat Population (Worst Conditions, 10 Years, Additions)")
plt.xlabel("Year")
plt.ylabel("Population Size")
plt.legend()
plt.grid(True, linestyle=':', color='gray', alpha=0.6)
plt.tight_layout()
plt.show()

# Plot 25-year simulation
plt.figure(figsize=(8,5))
for label, P in add_strategies_25.items():
    plt.plot(years_25, P, label=label)
plt.title("Bobcat Population (Worst Conditions, 25 Years, Additions)")
plt.xlabel("Year")
plt.ylabel("Population Size")
plt.legend()
plt.grid(True, linestyle=':', color='gray', alpha=0.6)
plt.tight_layout()
plt.show()
''' 
When adding 3 animals per year, we see the population start to decrease linearly. When we add 10 animals per year, we see the population start to increase a lot.
Adding 5% each  year for 10 years leads to very minimal growth. Only adding 1% each year leads to a substancial decrease in the population.
   '''
