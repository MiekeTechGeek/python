import matplotlib.pyplot as plt
import random
from collections import Counter

def roll_die(sides=6):
    """Roll a die with a given number of sides."""
    return random.randint(1, sides)

# 1. Rolling two 8-sided dice (D8) 1,000 times
num_rolls = 1000
d8_results = [roll_die(8) + roll_die(8) for _ in range(num_rolls)]

d8_counts = Counter(d8_results)
plt.figure(figsize=(10, 5))
plt.bar(d8_counts.keys(), d8_counts.values(), color='blue', alpha=0.7)
plt.title("Rolling Two D8 Dice 1,000 Times")
plt.xlabel("Sum of Dice")
plt.ylabel("Frequency")
plt.xticks(range(2, 17))
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# 2. Rolling three D6 dice
num_rolls = 1000
three_d6_results = [roll_die(6) + roll_die(6) + roll_die(6) for _ in range(num_rolls)]

d6_counts = Counter(three_d6_results)
plt.figure(figsize=(10, 5))
plt.bar(d6_counts.keys(), d6_counts.values(), color='green', alpha=0.7)
plt.title("Rolling Three D6 Dice 1,000 Times")
plt.xlabel("Sum of Dice")
plt.ylabel("Frequency")
plt.xticks(range(3, 19))
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# 3. Multiplication of two dice instead of summation
num_rolls = 1000
multiplication_results = [roll_die(6) * roll_die(6) for _ in range(num_rolls)]

multiplication_counts = Counter(multiplication_results)
plt.figure(figsize=(10, 5))
plt.bar(multiplication_counts.keys(), multiplication_counts.values(), color='red', alpha=0.7)
plt.title("Multiplication of Two D6 Dice 1,000 Times")
plt.xlabel("Product of Dice")
plt.ylabel("Frequency")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

print("Dice simulations completed successfully!")
