import matplotlib.pyplot as plt
from random import choice

class RandomWalk:
    def __init__(self, num_points=5000):
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        """Determine the direction and distance for each step."""
        direction = choice([1, -1])  # Randomly choose direction
        distance = choice(range(0, 9))  # Choose distance from 0 to 8
        step = direction * distance
        return step

    def fill_walk(self):
        """Calculate all points in the walk."""
        while len(self.x_values) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()

            # Reject moves that go nowhere (both steps are zero)
            if x_step == 0 and y_step == 0:
                continue

            # Calculate new position
            new_x = self.x_values[-1] + x_step
            new_y = self.y_values[-1] + y_step

            self.x_values.append(new_x)
            self.y_values.append(new_y)

# Create an instance of RandomWalk and generate points
rw = RandomWalk()
rw.fill_walk()

# Plotting the results using ax.plot() instead of ax.scatter()
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(rw.x_values, rw.y_values, linewidth=2)  # Use ax.plot() with linewidth argument
ax.set_title("Random Walk Simulation", fontsize=24)
ax.set_xlabel("X Values", fontsize=14)
ax.set_ylabel("Y Values", fontsize=14)
plt.show()