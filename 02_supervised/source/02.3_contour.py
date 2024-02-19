import numpy as np
import matplotlib.pyplot as plt

# Data
x = np.array([8, 9, 10, 11, 12, 13, 14, 15])
y = np.array([54, 69, 75, 78, 85, 102, 103, 103])

# Generating a range of values for m and c
m_values = np.linspace(5, 8, 1000)
c_values = np.linspace(-10, 10, 1000)

# Preparing the grid for m and c values
M, C = np.meshgrid(m_values, c_values)

# Calculating the error for each combination of m and c
Error = np.zeros(M.shape)
for i in range(len(x)):
    Error += (y[i] - (M*x[i] + C))**2
Error /= 8

# Plotting the contour plot
plt.figure(figsize=(5, 3.5))
cp = plt.contour(M, C, Error, levels=[17.25,17.5,18,19,20,22,30,42,80,160,320,640], cmap='viridis')
plt.colorbar(cp)
#plt.title('Contour Plot of Error Function')
plt.xlabel('m')
plt.ylabel('c')
plt.tight_layout()
plt.savefig('02.3_contour.png')
plt.show()

#np.geomspace(Error.min(), Error.max(), 20)
