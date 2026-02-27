# Ultrasonic Sensor Live Logger

This project provides a complete hardware-to-software bridge for reading distance data from an HC-SR04 ultrasonic sensor, visualizing it in real-time, and logging it for later analysis. 

An Arduino Uno reads the sensor and streams the data over a Serial connection. A Python script reads that stream, displays a live updating graph using Matplotlib, and automatically saves the data into a timestamped CSV file.

## 📁 Files in this Repository
* **`arduino_uno.ino`**: The C++ code to flash to the Arduino. It handles triggering the ultrasonic sensor, calculating the distance in centimeters, and sending it over Serial.
* **`sensor_logger.py`**: The Python script that reads the Serial port, animates the live data graph, and handles the CSV file generation.
* **`ultrasonic_data_20260227_225818.csv`**: An example output file showing the logged timestamp and distance data.

## 🛠️ Hardware Wiring
Connect the HC-SR04 ultrasonic sensor to the Arduino Uno as follows:
* **VCC** ➔ **5V** on Arduino
* **GND** ➔ **GND** on Arduino
* **Trig** ➔ **Digital Pin 9**
* **Echo** ➔ **Digital Pin 10**

## 💻 Software Setup & Usage

### 1. Arduino Setup
1. Open `arduino_uno.ino` in the Arduino IDE.
2. Connect your Arduino Uno and select the correct port (`Tools > Port`).
3. Upload the code to the board.
4. **Important:** Close the Arduino IDE Serial Monitor before running the Python script to free up the port.

### 2. Python Setup
Ensure you have Python 3 installed. You will need to install the required libraries for serial communication and graphing:
```bash
pip install pyserial matplotlib

```

### 3. Configuration

Open `sensor_logger.py` in a text editor and update the `SERIAL_PORT` variable to match your system:

* **Windows:** Usually `COM3`, `COM4`, etc.
* **Linux:** Usually `/dev/ttyACM0` or `/dev/ttyUSB0`
* **macOS:** Usually `/dev/cu.usbmodem...`

### 4. Running the Logger

Run the script from your terminal or command prompt:

```bash
python sensor_logger.py

```

A window will pop up showing the live distance data. To stop the program and save the data, simply close the graph window. The timestamped CSV file will automatically be generated in the same directory as the script.

```
