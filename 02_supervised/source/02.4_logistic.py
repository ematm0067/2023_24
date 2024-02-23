import numpy as np
import matplotlib.pyplot as plt

# Define the standard logistic function
def logistic_function(x):
    return 1 / (1 + np.exp(-x))

# Generate x values from -3 to 3
x_values = np.linspace(-5, 5, 400)

# Calculate the y values using the logistic function
y_values = logistic_function(x_values)

# Plotting the standard logistic function
plt.figure(figsize=(5, 2))
plt.plot(x_values, y_values, label='Logistic Function', color='purple')
plt.xlabel('x')
plt.ylabel('sigma(x)')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()

plt.tight_layout()
plt.savefig('./02.4_logistic.png', dpi=300)
plt.show()
