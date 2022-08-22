# create a line graph of squares
import matplotlib.pyplot as plt

val = [1, 2, 3, 4, 5]
sqrt = [1, 4, 9, 16, 25]

# plotting and configuring the styling
plt.plot(val, sqrt, linewidth=5)

# title and axes title
plt.title("Squares Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# need this since we're coding on IDE instead of notebook
plt.show()

