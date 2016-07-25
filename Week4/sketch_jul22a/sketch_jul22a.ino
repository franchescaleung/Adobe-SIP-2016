#include <Servo.h>
int sensorRight=5;
int sensorLeft = 7;
Servo servoRight;
Servo servoLeft;

//servoLeft.attach(12);
//servoRight.attach(11);

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(sensorRight, INPUT_PULLUP);
  pinMode(sensorLeft, INPUT_PULLUP);
  servoLeft.attach(12);
  servoRight.attach(11);

//  pinMode(servoLeft, OUTPUT);
//  pinMode(servoRight, OUTPUT);
}


void stopServos(){
  servoLeft.writeMicroseconds(1500);
  servoRight.writeMicroseconds(1500);
}

void forwardServos(){
  servoLeft.writeMicroseconds(1700);
  servoRight.writeMicroseconds(1300);
}

void backwardServos(){
  servoLeft.writeMicroseconds(1300);
  servoRight.writeMicroseconds(1700);

}

void leftServos(){
  servoLeft.writeMicroseconds(1300);
  servoRight.writeMicroseconds(1300);
}

void rightServos(){
  servoLeft.writeMicroseconds(1700);
  servoRight.writeMicroseconds(1700);
}

void loop() {
//digitalRead(sensorLeft) == 0
  
  if (digitalRead(sensorLeft) == 0 && digitalRead(sensorRight) == 0){
    backwardServos();
    delay(400);
    leftServos();
    delay(500);
    forwardServos();
  }
  else if (digitalRead(sensorLeft)==0 && digitalRead(sensorRight) == 1){
    backwardServos();
    delay(400);
    leftServos();
    delay(500);
    forwardServos();
    
  }
  else if (digitalRead(sensorRight) == 0 && digitalRead(sensorLeft) == 1){
    backwardServos();
    delay(400);
    rightServos();
    delay(500);
    forwardServos();
  }
  else if (digitalRead(sensorRight) == 1 && digitalRead(sensorLeft) ==1){
    forwardServos();
    delay(400);
  }
  
 }
