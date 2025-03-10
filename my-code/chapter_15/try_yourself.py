# import matplotlib.pyplot as plt
# import numpy as np

# plt.style.use('_mpl-gallery')

# # make data
# x = np.linspace(0, 10, 100)
# y = 4 + 1 * np.sin(2 * x)
# x2 = np.linspace(0, 10, 25)
# y2 = 4 + 1 * np.sin(2 * x2)

# # plot
# fig, ax = plt.subplots()

# ax.plot(x2, y2 + 2.5, 'x', markeredgewidth=2)
# ax.plot(x, y, linewidth=2.0)
# ax.plot(x2, y2 - 2.5, 'o-', linewidth=2)

# ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
#        ylim=(0, 8), yticks=np.arange(1, 8))

# plt.show()

# import matplotlib.pyplot as plt

# from mpl_toolkits.mplot3d import axes3d

# plt.style.use('_mpl-gallery')

# # Make data
# X, Y, Z = axes3d.get_test_data(0.05)

# # Plot
# fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
# ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)

# ax.set(xticklabels=[],
#        yticklabels=[],
#        zticklabels=[])

# plt.show()

import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')  # Use a built-in matplotlib style

# Make data
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
mental_health_scores = [5, 4, 3, 2, 1, 1, 1]

# Plot
fig, ax = plt.subplots(figsize=(12, 6))

# Use red color for the declining mental health
ax.plot(days, mental_health_scores, 'o-', color='red', linewidth=2.5, label='Mental Health Declining')

# Set y-axis limits and ticks
ax.set(ylim=(0, 6), yticks=np.arange(0, 7, 1))

# Add titles and labels
ax.set_title('Mental Health Trends Over the Week', fontsize=20, color='darkblue', weight='bold')
ax.set_xlabel('Days of the Week', fontsize=16, weight='bold')
ax.set_ylabel('Mental Health Score', fontsize=16, weight='bold')

# Add grid
ax.grid(True, linestyle='--', alpha=0.6)

# Add legend
ax.legend(loc='upper right', fontsize=12)

# Show the plot
plt.show()
