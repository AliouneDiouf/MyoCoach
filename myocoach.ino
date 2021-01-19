
float randomNumber[100];
float dataEMG[2];

void setup() {
  Serial.begin(115200); // Starts the serial communication
}
void loop() 
{
   int sensorValue = analogRead(A0);
  // Convert the analog reading (which goes from 0 - 1023) to a voltage (0 - 5V):
      float voltage = sensorValue * (5.0 / 1023.0);
      dataEMG[0]= voltage;
      dataEMG[1]= random(0,500)/100.00;
      Serial.print(dataEMG[0]);
      Serial.print(":");
      Serial.print(dataEMG[1]);
      Serial.println();
      
 
   delay(250);
 
}
