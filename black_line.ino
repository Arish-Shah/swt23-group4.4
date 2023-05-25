#include <Ultrasonic.h>

void setup() {
  initialize();
  sensorAutoCalibrate();
  pinMode(A3, INPUT);
  pinMode(20, OUTPUT);
}


void loop() {
  int sensors[5];
  char buffer[50];
  float output = analogRead(A3);
  Ultrasonic ultrasonic(10);
  calibratedSensors(sensors);

  int left = sensors[0];
  int middle = (sensors[1] + sensors[2] + sensors[3]) / 3;
  int right = sensors[4];
  int lightpercent = ((1023 - output) / 1023) * 100;
  int distance = ultrasonic.read(); // gives distance in cm

  // stop at obstacle
  if (distance < 10) {
    stopSmooth();
  }  else {
    // follow black line
    if (middle > 200) {
      activateMotor(0, 0.2);
      activateMotor(1, 0.2);
    }
    
    if (right > 200) {
      activateMotor(1, 0);
    }

    if (left > 200) {
      activateMotor(0, 0);
    }
  }

  // headlight
  if (lightpercent > 90) {
    digitalWrite(20, LOW); 
  } else {
    digitalWrite(20, HIGH);
  }

  delay(5);
}