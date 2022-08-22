from random_walk import RandomWalk
import matplotlib.pyplot as plt

# continuously generate random walk until irompted
while True:
    rw = RandomWalk(50000)

    # generate all random walks
    rw.fill_walk()

    # config the size of plotting window
    # dpi will set a plot size that makes effective use of space available on screen
    plt.figure(dpi=128, figsize=(10, 6))

    point_numbers = list(range(rw.num_points))
    # x_values and y_values are public data fields
    # different colors for each value in point_numbers (following color gradient)
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor="none", s = 15)

    # indicating first and last point
    plt.scatter(rw.x_values[0], rw.y_values[0], c="green", edgecolor="none", s=50)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c="red", edgecolor="none", s=50)

    # remove axis
    #plt.axes().get_xaxis().set_visible(False)
    #plt.axes().get_yaxis().set_visible(False)

    plt.title("Random Walk", fontsize=32)

    plt.show()

    # ask user whether they want to save
    to_save = input('Do you wish to save? (y/n) ')
    if to_save == 'y'.casefold():
        file_name = input("Enter file name: ")
        plt.savefig((file_name+".png"), bbox_inches="tight")

    # determine whether to continue generate random walk
    to_cont = input("Do you wish to continue? (y/n)")
    if to_cont == "n".casefold():
        break

