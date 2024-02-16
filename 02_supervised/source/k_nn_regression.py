import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsRegressor

# Function: Sine wave
def f(x):
    return np.sin(x)

np.random.seed(0)

k=5
x_range=20
n_sample=30


# Generate sample points with random x-locations
np.random.seed(0)
x_random = np.sort(np.random.uniform(0, x_range, n_sample)) # Random times
y_random = f(x_random) + np.random.normal(scale=0.5, size=x_random.shape) # Noisy samples

# K-NN regression models
knn = KNeighborsRegressor(n_neighbors=k)
knn_weighted = KNeighborsRegressor(n_neighbors=k, weights='distance')

# Fit the models with random samples
knn.fit(x_random.reshape(-1, 1), y_random)
knn_weighted.fit(x_random.reshape(-1, 1), y_random)

# Predict values
x_test = np.linspace(0, x_range, 1000).reshape(-1, 1)
y_pred_random = knn.predict(x_test)
y_pred_weighted_random = knn_weighted.predict(x_test)

# Plotting with random sampling points
plt.figure(figsize=(12, 6))

# Original sine wave
plt.plot(x_test, f(x_test), label='Original Sine Wave', color='green')

# Sampled data with random x-locations
plt.scatter(x_random, y_random, label='Noisy Random Samples', color='red')

# K-NN regression
plt.plot(x_test, y_pred_random, label='K-NN Regression', color='blue')

# Weighted K-NN regression
plt.plot(x_test, y_pred_weighted_random, label='Weighted K-NN Regression', color='purple')

plt.xlabel('X')
plt.ylabel('Y')
plt.title('K-NN Regression on Noisy Sine Wave Data with Random Sampling Points')
plt.legend()
plt.show()

