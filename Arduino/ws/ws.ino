#include <TimerOne.h>

// msgFreq -> frequency to send temperature messages
// counter -> the Arduino timer1 can only count to 8 secounds. So, this counter is used to count each second (e.g. counter = 10 -> 10 seconds elapsed)
// sendMsgFlag -> is true when it is time to send a message
unsigned int msgFreq, counter;
bool sendMsgFlag;

void setup() {
  Serial.begin(9600);
  Serial.setTimeout(100); //excellent to reduce latency when reading incoming data
  
  pinMode(5, OUTPUT);  //dcMotor Enable
  pinMode(4, OUTPUT);  //dcMotor Direction1
  pinMode(3, OUTPUT);  //dcMotor Direction2
  pinMode(12, OUTPUT); //led

  //dc motor initial rotation direction
  digitalWrite(4, HIGH);
  digitalWrite(3, LOW);

  //timer setup
  //max period: 8388480
  //pin 9 and 10 wont be available
  msgFreq = 2;//seconds
  counter = 0;
  Timer1.initialize(1000000); //trigger after 1 second
  Timer1.attachInterrupt( timerCallback );
}

void loop() {
  // disable the timer signals while we use the counter variable. counter variable is constatly being changed in the callback called by the interruption
  noInterrupts();
  sendMsgFLag = counter > msgFreq;
  interrupts();
  if(sendMsgFlag){
    Serial.println(analogRead(0));
    Timer1.restart();
    counter = 0;
  }
}

// callback called when Arduino receives a message
// I decided to use 2 values in the message: the mode(command), and the datavalue.
// mode: M, L, F | motor, led, freq 
// datavalue: mode state, value
void serialEvent(){
  String dataIn = Serial.readString();
  char command = dataIn[0];
  unsigned long int value = dataIn.substring(1).toInt();
  switch(command){
    case 'M':
      if(value)
        analogWrite(5, 200);
      else
        analogWrite(5, 0);
      break;
    case 'L':
      if(value)
        digitalWrite(12, HIGH);
      else
        digitalWrite(12, LOW);
      break;
    case 'F':
      Timer1.restart();
      counter = 0;
      msgFreq = value;
      break;
    default:
      break;
  }
}

void timerCallback(){
    counter++;
}
