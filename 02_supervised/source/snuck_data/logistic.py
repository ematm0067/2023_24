# Re-importing necessary libraries after code execution state reset

import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

from sklearn.linear_model import LogisticRegression



# Assuming the data has been loaded into a DataFrame named simulated_data

# For demonstration, creating the DataFrame directly with the provided sample data

simulated_data = pd.read_csv('simulated_data.csv')



# Add jitter to the 'usage' column for plotting clarity

simulated_data['usage_jittered'] = simulated_data['usage'] + np.random.uniform(-0.05, 0.05, size=len(simulated_data))



# Fit logistic regression model

X = simulated_data[['age']]

y = simulated_data['usage']

model = LogisticRegression()

model.fit(X, y)



# Generate predictions for the logistic curve

x_range = np.linspace(simulated_data['age'].min(), simulated_data['age'].max(), 300)

y_predicted = model.predict_proba(x_range.reshape(-1, 1))[:,1]



# Plotting

plt.figure(figsize=(5, 2))

plt.scatter(simulated_data['age'], simulated_data['usage_jittered'], c=simulated_data['usage'], cmap='bwr', alpha=0.7, label='Data')

plt.plot(x_range, y_predicted, color='green', label='Logistic Regression')



plt.xlabel('Age')

plt.yticks([0, 1], ['Snuck', 'Sneaked'])


plt.legend()

plt.tight_layout()
plt.grid(True, linestyle='--', alpha=0.6)
plt.savefig('../02.4_fit.png', dpi=300)

plt.show()



# Display the coefficients

beta_0 = model.intercept_[0]  # Intercept (beta_0)

beta_1 = model.coef_[0][0]  # Coefficient for age (beta_1)


print(beta_0, beta_1)
