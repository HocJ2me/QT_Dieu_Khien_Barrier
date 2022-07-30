#include <Servo.h>

Servo myservo;  // create servo object to control a servo

#define buttonPin 5
#define sensorPin 2
#define servoPin 9

int statusBarrier = 1;

void setup() {
  Serial.begin(9600);
  myservo.attach(9);
  pinMode(buttonPin, INPUT_PULLUP);
  pinMode(sensorPin, INPUT);
  myservo.write(10);
  Serial.print("{\"status\":\"close\"}");

}

void OpenBarrier()
{
  Serial.print("{\"status\":\"open\"}");
  myservo.write(110);
  delay(50);
}
void closeBarrier()
{
  Serial.print("{\"status\":\"close\"}");
  myservo.write(10);
  delay(50);
}
void loop() {
  if(digitalRead(sensorPin) == 0)
  {
      delay(50);
      if(digitalRead(sensorPin) == 0)
      {
        OpenBarrier();
        delay(5000);
        closeBarrier();
      }
  }
  if(digitalRead(buttonPin) == 0)
  {
    delay(20);
    if(digitalRead(buttonPin) == 0) 
    {
      while(digitalRead(buttonPin) == 0);
      statusBarrier = 1 - statusBarrier;
    }
  }
  if(statusBarrier == 0) OpenBarrier();
  if(statusBarrier == 1) closeBarrier();
  
  delay(50);
}
