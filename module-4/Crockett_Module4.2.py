import csv
import sys
from datetime import datetime
from matplotlib import pyplot as plt

# File name
filename = 'sitka_weather_2018_simple.csv'

# Lists to store data
dates, highs, lows = [], [], []

# Read the CSV file
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Loop through the rows in the file
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[5])
            low = int(row[6])
        except ValueError:
            # Skip rows with missing data
            continue

        dates.append(current_date)
        highs.append(high)
        lows.append(low)

# Menu loop
while True:
    print("\nMenu Options:")
    print("1. Highs")
    print("2. Lows")
    print("3. Exit")
    choice = input("Enter your choice (1-3): ").strip()

    if choice == '1':
        # Plot high temperatures in red
        fig, ax = plt.subplots()
        ax.plot(dates, highs, c='red')
        plt.title("Daily High Temperatures - 2018", fontsize=20)
        plt.xlabel("Date", fontsize=14)
        plt.ylabel("Temperature (F)", fontsize=14)
        fig.autofmt_xdate()
        plt.tick_params(axis='both', which='major', labelsize=12)
        plt.show()

    elif choice == '2':
        # Plot low temperatures in blue
        fig, ax = plt.subplots()
        ax.plot(dates, lows, c='blue')
        plt.title("Daily Low Temperatures - 2018", fontsize=20)
        plt.xlabel("Date", fontsize=14)
        plt.ylabel("Temperature (F)", fontsize=14)
        fig.autofmt_xdate()
        plt.tick_params(axis='both', which='major', labelsize=12)
        plt.show()

    elif choice == '3':
        print("Exiting program. Have a great day!")
        sys.exit()

    else:
        print("Invalid selection. Please enter 1, 2, or 3.")
