import matplotlib.pyplot as plt

x = list(range(0, 5001))
y = [m**3 for m in x]

plt.scatter(x, y, c=y, cmap=plt.cm.Greens, edgecolor="none")
plt.title("Cubes of Values", fontsize=24)
plt.xlabel("Values", fontsize=14)
plt.ylabel("Cubes", fontsize=14)

plt.show()