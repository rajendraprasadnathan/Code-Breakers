#include <ESP8266WiFi.h>

#include <ThingSpeak.h>
#include <Servo.h>

Servo servo;

int  i;
WiFiClient client;

void setup()
{
  i = 0;
Serial.begin(9600);
ThingSpeak.begin(client);

pinMode(D2, OUTPUT);
  WiFi.disconnect();
  delay(3000);
   WiFi.begin("honor1","12345678");
  while ((!(WiFi.status() == WL_CONNECTED))){
    delay(300);
    servo.attach(D4); //D4

servo.write(0);

delay(2000);

  }
  Serial.println("connected!");

}


void loop()
{int j;

    i = (ThingSpeak.readIntField( 563910,1,"QLHCCM4ORXK9KQLU"));
    j=(ThingSpeak.readIntField( 563910,2,"QLHCCM4ORXK9KQLU"));
    if (i == 0) {
      digitalWrite(D2,HIGH);
      delay(2000);
      servo.write(90);
      delay(2000);
      servo.write(0);
      digitalWrite(D2,LOW);
      delay(2000);

    }
    else  {
      servo.write(90);
      delay(2000);
      servo.write(0);
      

    }
    
    if(j==1){
      servo.write(90);
      delay(2000);
      servo.write(0);
    }
    else{
      digitalWrite(D2,HIGH);
      delay(2000);
      servo.write(90);
      delay(2000);
      servo.write(0);
      digitalWrite(D2,LOW);
      delay(2000);
      
    }

}
