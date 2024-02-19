import numpy as np
import matplotlib.pyplot as plt

# Generating a more focused range of values for m and c for the contour plot
m_values = np.linspace(0, 5, 100)  # Tightened range around the true m
c_values = np.linspace(0, 5, 100)  # Tightened range around the true c
M, C = np.meshgrid(m_values, c_values)
Error = np.zeros(M.shape)

# Calculating the error for each combination of m and c

Error=(M-2)**2+(1.5*C-3)**2

# Plotting the contour plot with gradient descent steps
plt.figure(figsize=(5, 3.5))
cp = plt.contour(M, C, Error, levels=np.linspace(Error.min(), Error.max(), 30), cmap='viridis')
plt.colorbar(cp)


plt.xlabel('m')
plt.ylabel('c')
plt.tight_layout()
plt.savefig('02.3_simple_contour.png')
plt.show()
