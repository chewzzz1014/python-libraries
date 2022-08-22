# rolling 2 dices for different distribution of results
# we'll consider the sum of 2 dices
import pygal
from die import Die

die_1 = Die()
die_2 = Die()

# roll 2 dices
results = []
for roll_num in range(1000):
    results.append(die_1.roll()+die_2.roll())

# store the analyzed result
freq = []
max_result = die_1.num_sides + die_2.num_sides
for val in range(2, max_result+1):
    freq.append(results.count(val))

# visualization
hist = pygal.Bar()

hist.title = "Results of rolling two D6 dice 1000 times"
hist.x_labels = [str(x) for x in range(2, 13)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add("D6 + D6", freq)
hist.render_to_file("D6_D6_dice_visual.svg")
