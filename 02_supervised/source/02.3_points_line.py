import matplotlib.pyplot as plt
import numpy as np

# Data
x = np.array([8, 9, 10, 11, 12, 13, 14, 15])
y = np.array([54, 69, 75, 78, 85, 102, 103, 103])

# Calculate the linear regression parameters
slope, intercept = np.polyfit(x, y, 1)

# Calculate y-values of the regression line
y_pred = slope * x + intercept

# Plotting the scatter plot
plt.figure(figsize=(4, 2.5))
plt.scatter(x, y)

# Plotting the regression line
plt.plot(x, y_pred, color='red')

# Plotting vertical lines from each point to the regression line
for xi, yi, y_pred_i in zip(x, y, y_pred):
    plt.vlines(xi, min(yi, y_pred_i), max(yi, y_pred_i), color='blue', linestyle='dotted')

plt.xlabel('x')
plt.ylabel('y')
plt.savefig('02.3_points_line.png')
plt.show()
