import csv
import matplotlib.pyplot as plt
from distance import Distance
from hashtable import HashTable

ht = HashTable()
data = ht.get_all()
data.sort()  # sort by timestamp

#generates a csv files
with open('distance_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Timestamp", "Distance (cm)"])
    for t, d in HashTable.get_all():
        writer.writerow([t, d])

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