import serial
import csv
import time
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os

# --- Configuration ---
#Change 'COM3' to whatever port the Arduino is on!
SERIAL_PORT = 'COM3' 
BAUD_RATE = 9600

# --- File Saving Setup ---
# Get the exact folder where this Python script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Generate a timestamped filename inside that exact folder
file_name_only = f"ultrasonic_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
filename = os.path.join(script_dir, file_name_only)

# Set up the CSV file with headers right away
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Timestamp", "Distance_cm"])

print(f"Data will be saved to: {filename}")

# --- Initialize Serial Connection ---
try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    print("Connecting to Arduino... please wait.")
    time.sleep(2) # Wait for the Arduino to reset after connecting
except Exception as e:
    print(f"Error opening serial port: {e}")
    print("Check that the COM port is correct and the Arduino IDE Serial Monitor is CLOSED.")
    exit()

# --- Set up Matplotlib Figure ---
fig, ax = plt.subplots()
xs = []
ys = []
max_points = 50 # Number of points to display on the live graph at once

def animate(i, xs, ys):
    try:
        if ser.in_waiting > 0:
            # Read and decode the serial data
            line = ser.readline().decode('utf-8').strip()
            
            # The HC-SR04 can sometimes output negative numbers or noise if it misreads
            if line.lstrip('-').isdigit(): 
                val = int(line)
                
                # Cap the distance to avoid graph blowouts (HC-SR04 max is ~400cm)
                if val > 400:
                    val = 400 
                    
                current_time = datetime.now().strftime('%H:%M:%S.%f')[:-3]
                
                # Append to lists for plotting
                xs.append(current_time)
                ys.append(val)
                
                # Keep lists constrained to max_points
                xs = xs[-max_points:]
                ys = ys[-max_points:]
                
                # Write to CSV in real-time
                with open(filename, mode='a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([current_time, val])
                
                # Draw the plot
                ax.clear()
                ax.plot(xs, ys, marker='o', color='g')
                ax.set_title("Live Ultrasonic Distance Data")
                ax.set_ylabel("Distance (cm)")
                ax.set_xlabel("Time")
                # Set a fixed Y-axis limit for a more stable graph
                ax.set_ylim(0, 50) 
                plt.xticks(rotation=45, ha='right')
                plt.subplots_adjust(bottom=0.30)
                
    except Exception as e:
        print(f"Error reading data: {e}")

# --- Run the application ---
print("Starting live graph... Close the graph window to stop and save.")
# Run the animation loop
ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=100)
plt.show()

# --- Clean up ---
# This runs after the user clicks the "X" on the Matplotlib window
ser.close()
print(f"Serial connection closed. All data successfully saved to {filename}")
