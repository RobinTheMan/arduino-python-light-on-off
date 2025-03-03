//Robert Wierzal

//Very simple arduino code that just takes in the message from the python code and uses it to turn on and off a light built into the arduino

void setup() {
  Serial.begin(9600); // Initialize serial communication
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    String msg = Serial.readStringUntil('\n'); // Read command
    msg.trim(); // Remove any extra spaces or newlines
    if (msg == "on") {
      digitalWrite(LED_BUILTIN, HIGH); // Turn LED on
    } 
    else if (msg == "off") {
      digitalWrite(LED_BUILTIN, LOW); // Turn LED off
    }
    }
  }
