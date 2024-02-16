import matplotlib.pyplot as plt

# Data
x = [8, 9, 10, 11, 12, 13, 14, 15]
y = [54, 69, 75, 78, 85, 102, 103, 103]

# Plotting the scatter plot
plt.figure(figsize=(4, 2.5))
plt.scatter(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.savefig('02.3_points.png')
plt.show()
