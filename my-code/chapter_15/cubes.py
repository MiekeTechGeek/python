import matplotlib.pyplot as plt
import numpy as np

# First, generate data for the first five cubic numbers
x_values_5 = [1, 2, 3, 4, 5]  # Numbers from 1 to 5
y_values_5 = [x**3 for x in x_values_5]  # Cubes of these numbers

# Plotting the first five cubic numbers
plt.figure(figsize=(8, 6))
plt.plot(x_values_5, y_values_5, marker='o', linestyle='-', color='blue', label="First Five Cubic Numbers")
plt.title("First Five Cubic Numbers")
plt.xlabel("Number")
plt.ylabel("Cube of Number")
plt.legend()
plt.grid(True)
plt.show()

# Now generate data for the first 5000 cubic numbers
x_values_5000 = np.arange(1, 5001)  # Numbers from 1 to 5000
y_values_5000 = x_values_5000**3    # Cubes of these numbers

# Apply a colormap while plotting
colors = y_values_5000 / max(y_values_5000)  # Normalize colors based on cube values

plt.figure(figsize=(10, 8))
scatter = plt.scatter(x_values_5000, y_values_5000, c=colors, cmap='plasma', s=3) # viridis # s=1
plt.colorbar(scatter)  # Add colorbar to show color mapping
plt.title("First 5,000 Cubic Numbers with Colormap")
plt.xlabel("Number")
plt.ylabel("Cube of Number")
plt.grid(True)
plt.show()