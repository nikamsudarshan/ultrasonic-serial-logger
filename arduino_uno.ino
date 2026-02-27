const int trigPin = 9;
const int echoPin = 10;

void setup() {
  Serial.begin(9600); // Ensure baud rates match to avoid garbage characters
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
}

void loop() {
  // Clear the trigPin by setting it LOW
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);

  // Trigger the sensor by setting the trigPin HIGH for 10 microseconds
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  // Read the echoPin, returns the sound wave travel time in microseconds
  long duration = pulseIn(echoPin, HIGH);

  // Calculate the distance
  int distance = duration * 0.034 / 2;

  // Print the distance to the Serial Monitor
  Serial.println(distance);
  
  delay(100); // Send data 10 times a second
}
