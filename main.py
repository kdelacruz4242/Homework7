import serial
import time
import csv
import matplotlib.pyplot as plt
from hashtable import HashTable
from distance import Distance

#GND -> GND
#Echo -> Digital Pin 6 with 10k resistor between
#Trig -> Digital Pin 7
#VCC -> 5V

# Replace 'COM3' with the correct port for your system
arduino_port = 'COM7'
baud_rate = 9600

hashtable = HashTable()
count = 0

# Establish connection with Arduino
arduino = serial.Serial(arduino_port, baud_rate, timeout=1)
time.sleep(2)  # Allow time for connection to establish

while count < 15:
    if arduino.in_waiting > 0:
        distance = arduino.readline().decode('utf-8').strip()
        if distance:
            new_distance = Distance(distance)
            hashtable.insert(new_distance.timestamp, float(new_distance.distance))
            print(new_distance)
            count += 1

    time.sleep(2)  # Read every 2 seconds
arduino.close()

# write to CSV
with open('distance_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Timestamp", "Distance (cm)"])
    for t, d in hashtable.getHashTable():
        writer.writerow([t, d])

# Plot the data
data = hashtable.getHashTable()
data.sort()  # sort by timestamp

timestamps = [t for t, _ in data]
distances = [d for _, d in data]

plt.plot(timestamps, distances, marker='o', color='blue')
plt.title("Ultrasonic Distance Over Time")
plt.xlabel("Timestamp")
plt.ylabel("Distance (cm)")
plt.grid(True)
plt.show()
