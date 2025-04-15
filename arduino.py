"""""
#define TRIG 7
#define ECHO 6

void setup() {
  Serial.begin(9600);
  pinMode(TRIG, OUTPUT);
  pinMode(ECHO, INPUT);
}

void loop() {
  digitalWrite(TRIG, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG, LOW);

  long duration = pulseIn(ECHO, HIGH);
  float distance = (duration * 0.0343) / 2; // Convert to cm
  Serial.println(distance); // Send distance to Python
  delay(2000);
}
""'
# and download standard firmata