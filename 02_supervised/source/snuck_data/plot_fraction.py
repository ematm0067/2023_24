# Re-importing necessary libraries after code execution state reset

import pandas as pd

import matplotlib.pyplot as plt



simulated_data = pd.read_csv('./simulated_data.csv')



# Define the age bands

age_bins = [0, 14, 20, 30, 40, 50, 60, 70, 80, 90]

age_labels = ['0-13', '14-19', '20-29', '30-39', '40-49', '50-59', '60-69', '70-79', '80-89']



# Categorize ages into bands

simulated_data['age_band'] = pd.cut(simulated_data['age'], bins=age_bins, labels=age_labels, right=False)



# Calculate the fraction of usage=1 (snuck) in each band

snuck_fraction = simulated_data.groupby('age_band')['usage'].mean()

plt.figure(figsize=(5, 2))



# Plotting the line graph

snuck_fraction.plot(kind='line', color='skyblue', marker='o', linestyle='-', linewidth=2, markersize=8)

plt.ylabel('"sneaked" fraction')


plt.xticks(rotation=45)

plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.ylim(0, 1)

plt.tight_layout()
# Show plot
plt.savefig('../02.4_fraction.png', dpi=300)
plt.show()
