import numpy as np
import matplotlib.pyplot as plt

# Generating a more focused range of values for m and c for the contour plot
m_values = np.linspace(0, 5, 100)  # Tightened range around the true m
c_values = np.linspace(0, 5, 100)  # Tightened range around the true c
M, C = np.meshgrid(m_values, c_values)
Error = np.zeros(M.shape)

# Calculating the error for each combination of m and c

Error=(M-2)**2+(1.5*C-3)**2

# Gradient descent settings (adjusted for a more focused visualization)
m_start, c_start = 0, 0  # Starting values for m and c, closer to the true values
learning_rate = .43  # Reduced learning rate
steps = 10

# Gradient Descent Implementation
m, c = m_start, c_start
m_steps, c_steps = [m], [c]  # to store the trajectory of m and c
for _ in range(steps):
    grad_m = 2*(m-2)
    grad_c = 2*1.5*(1.5*c-3)
    m -= learning_rate * grad_m
    c -= learning_rate * grad_c
    m_steps.append(m)
    c_steps.append(c)

# Plotting the contour plot with gradient descent steps
plt.figure(figsize=(5, 3.5))
cp = plt.contour(M, C, Error, levels=np.linspace(Error.min(), Error.max(), 30), cmap='viridis')
plt.colorbar(cp)
plt.scatter(m_steps, c_steps, color='red')  # Mark gradient steps
for i in range(1, len(m_steps)):
    plt.arrow(m_steps[i-1], c_steps[i-1], m_steps[i]-m_steps[i-1], c_steps[i]-c_steps[i-1], 
              head_width=0.02, head_length=0.04, fc='red', ec='red')
plt.xlabel('m')
plt.ylabel('c')
plt.tight_layout()
plt.savefig('02.3_gradient_big_eta.png')
plt.show()
