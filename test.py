import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
from tqdm import tqdm

# --- 1. Simulation Configuration ---
# Define the parameters for our simulation as per the problem description.
# Using a configuration block makes the code easier to read and modify.
SAMPLE_SIZE = 100
NUM_SIMULATIONS = 1000
ALPHA = 0.05  # Significance level for rejecting the null hypothesis

# The range of mean differences (d) to test.
# np.arange is perfect for creating this sequence.
mean_differences = np.arange(0, 1.1, 0.1)

# --- 2. Running the Simulation ---
# We will store the proportion of Type II errors for each value of d.
type_ii_error_rates = []

print("Running simulations...")
# Using tqdm provides a helpful progress bar for long-running loops.
for d in tqdm(mean_differences, desc="Simulating for each mean difference (d)"):
    # Counter for the number of times we fail to reject the null hypothesis.
    non_rejection_count = 0
    
    for _ in range(NUM_SIMULATIONS):
        # a. Draw two samples of size 100.
        # Sample 1: From the standard normal distribution N(0, 1).
        sample1 = np.random.normal(loc=0, scale=1, size=SAMPLE_SIZE)
        
        # Sample 2: From a normal distribution N(d, 1).
        sample2 = np.random.normal(loc=d, scale=1, size=SAMPLE_SIZE)
        
        # b. Run an independent samples t-test.
        # We use `equal_var=True` because we know the populations have the same std dev (1).
        # The function returns the t-statistic and the p-value. We only need the p-value.
        _, p_value = stats.ttest_ind(sample1, sample2, equal_var=True)
        
        # c. Check if the null hypothesis is NOT rejected.
        # This occurs when the p-value is greater than or equal to our significance level.
        if p_value >= ALPHA:
            non_rejection_count += 1
            
    # d. Record the proportion of times the null hypothesis was not rejected.
    proportion_non_rejected = non_rejection_count / NUM_SIMULATIONS
    type_ii_error_rates.append(proportion_non_rejected)

print("Simulation complete.")

# --- 3. Plotting the Results ---
# Use a professional and clean plotting style.
sns.set_style("whitegrid")
plt.figure(figsize=(10, 6))

# Plot the proportion of non-rejections (Type II error rate) against d.
plt.plot(mean_differences, type_ii_error_rates, marker='o', linestyle='-', color='b', label='Simulated Type II Error Rate (β)')

# Add a horizontal line for the significance level for context.
plt.axhline(y=ALPHA, color='r', linestyle='--', label=f'Significance Level (α = {ALPHA})')

# Add informative labels and title.
plt.title('Type II Error Rate vs. Difference in Means (Effect Size)', fontsize=16)
plt.xlabel('Difference in Means (d)', fontsize=12)
plt.ylabel('Proportion of Non-Rejections', fontsize=12)
plt.xticks(mean_differences)
plt.ylim(0, 1.05)
plt.legend()
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Display the plot.
plt.show()

# --- 4. Print the results for clarity ---
print("\n--- Simulation Results ---")
print("d\t| Prop. Non-Rejection (β)")
print("--------------------------------")
for d, rate in zip(mean_differences, type_ii_error_rates):
    print(f"{d:.1f}\t| {rate:.3f}")