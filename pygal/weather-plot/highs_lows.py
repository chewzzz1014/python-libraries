# visualize the high and low temperatures from weather record
import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename= "sitka_weather_07-2014.csv"
with open(filename) as f:
    # instances of reader
    reader = csv.reader(f)
    # next() will return next line in file
    header_row = next(reader)


# printing all headers
for idx, header_name in enumerate(header_row):
    print(str(idx)+". "+header_name)


# extracting data in a column
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # extracting high temperature
    dates, highs, lows = [], [], []
    for row in reader:  # loop through all rows
        date = datetime.strptime(row[0], '%Y-%m-%d') # get the first item (date) of every row
        dates.append(date)

        highs.append(int(row[1]))    # get the second item (high temperature) of every row

        low = int(row[3])
        lows.append(low)

    print(highs)


# visualize the high temperature
fig = plt.figure(dpi=128, figsize=(6, 4))
plt.plot(dates, highs, c="red", alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

plt.title("Daily High and Low Temperature, July 2014", fontsize=16)
plt.xlabel("", fontsize=12)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=12)
plt.tick_params(axis="both", which="major", labelsize=12)

plt.show()