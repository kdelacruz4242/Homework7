import serial
import time
from distance import Distance
from stack import CircularStack

#GND -> GND
#Echo -> Digital Pin 6
#Trig -> Digital Pin 7
#VCC -> 5V

# Replace 'COM3' with the correct port for your system
arduino_port = 'COM7'
baud_rate = 9600

stack = CircularStack()

try:
    # Establish connection with Arduino
    arduino = serial.Serial(arduino_port, baud_rate, timeout=1)
    time.sleep(2)  # Allow time for connection to establish
    print("Connected to Arduino. Reading Ultrasonic Sensor data...")

    while True:
        if arduino.in_waiting > 0:
            distance = arduino.readline().decode('utf-8').strip()
            if distance:
                new_distance = Distance(distance)
                stack.push(new_distance)
                print(f"Distance: {distance} cm")
                stack.print_stack()
        time.sleep(2)  # Read every 2 seconds

except KeyboardInterrupt:
    print("Exiting...")
    arduino.close()

except serial.SerialException:
    print("Error: Could not connect to Arduino. Check your port and connection.")
