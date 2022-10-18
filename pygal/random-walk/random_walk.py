# generate random walk and visualize them
# visualization in rw_visual.py

from random import choice

class RandomWalk():
    def __init__(self, num_points=5000):
        # store number of points in walk
        self.num_points = num_points

        # coordinates of each point. Use list to stores coordinates for all points
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        # calculate all the points in walk
        while len(self.x_values) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()

            # reject moves that go nowhere
            if x_step==0 or y_step==0:
                continue

            # calculate next (x, y). From current position, move x_step and y_step
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)

    def get_step(self):
        direction = choice([1, -1])
        distance = choice(range(0, 5))
        return direction * distance