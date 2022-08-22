# one 6D die and one 1-D die
from die import Die
import pygal

die_1 = Die()
die_2 = Die(10)

results = []
for roll_num in range(1000):
    results.append(die_1.roll() + die_2.roll())

freq = []
max_result = die_1.num_sides + die_2.num_sides
for val in range(2, max_result+1):
    freq.append(results.count(val))

hist = pygal.Bar()
hist.title = 'Results of rolling a D6 and a D10 50,000 times'
hist.x_labels = [str(x) for x in range(2, 17)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add("D6 + D10", freq)
hist.render_to_file("D6_D10_dice_visual.svg")
