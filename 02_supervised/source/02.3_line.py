import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression


# Data
x = [8, 9, 10, 11, 12, 13, 14, 15]
y = [54, 69, 75, 78, 85, 102, 103, 103]


x_array = np.array(x).reshape(-1, 1)
y_array = np.array(y)

# Perform linear regression
model = LinearRegression().fit(x_array, y_array)
y_pred = model.predict(x_array)

# Plotting
plt.figure(figsize=(8, 3))
plt.scatter(x, y, label='Data Points')
plt.plot(x, y_pred, color='red', label='Linear Regression Line')
plt.xlabel('x')
plt.ylabel('y')

plt.savefig('02.3_line.png')
plt.show()
