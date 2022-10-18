# visualize Die class
import pygal
from pygal.dice.die import Die

die = Die()

results = []

# throws the dic 100 times
for roll_num in range(1000):
    results.append(die.roll())

# analyze the results: number of times obtain a number (1-6)
freq = []
for val in range(1, die.num_sides+1):
    freq.append(results.count(val))

# visualize the results
hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = [str(x) for x in range(1, 7)]
# axes title
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

# D6 as legend
hist.add("D6", freq)
hist.render_to_file("die_visual.svg")