import csv
import matplotlib.pyplot as plt
from hashtable import HashTable
timestamps = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
distances = [20, 21, 22, 23, 24, 25]

#generates a csv files
with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for timestamp in timestamps:
        writer.writerow([timestamp])
    for distance in distances:
        writer.writerow([distance])

#reads from the csv file
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        timestamps.append(row[0])
        try:
            distances.append(row[1])
        except IndexError:
            distances.append(None)

plt.plot(timestamps, distances, color = 'red')
plt.title('UltraSonic Distance Over Time')
plt.xlabel('Timestamp')
plt.ylabel('Distance (cm)')
plt.grid(True)
plt.show()