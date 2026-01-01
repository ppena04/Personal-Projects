

# Growth factors
a_best = 1 + 0.01676     # Best 
a_worst = 1 - 0.045      # Worst 

# Fixed-number strategies
b_values_best = {
    "Remove 1/year": -1,
    "Remove 5/year": -5
}

b_values_worst = {
    "Add 3/year": 3,
    "Add 10/year": 10
}

# compute fixed points and stability
def affine_analysis(a, b_dict):
    results = {}
    for label, b in b_dict.items():
        P_star = b / (1 - a)        # fixed point
        stable = abs(a) < 1         # stability criterion
        results[label] = {"Fixed Point": P_star, "Stable?": stable}
    return results

# best conditions
best_results = affine_analysis(a_best, b_values_best)
print("=== Best Conditions (Affine Analysis) ===")
for label, info in best_results.items():
    print(f"{label}: Fixed Point = {info['Fixed Point']:.2f}, Stable? {info['Stable?']}")

# worst conditions
worst_results = affine_analysis(a_worst, b_values_worst)
print("\n=== Worst Conditions (Affine Analysis) ===")
for label, info in worst_results.items():
    print(f"{label}: Fixed Point = {info['Fixed Point']:.2f}, Stable? {info['Stable?']}")

'''
Looking at the best conditions, in both fixed-number hunting strategies are unstable because a > 1.
The population will diverge away from fixed points (59.67 and 298.33). When looking at the worst conditions,
both fixed-number addition strategies are stable because a < 1. the population will stabilize at fixed points (66.67 and 222.22).
'''
