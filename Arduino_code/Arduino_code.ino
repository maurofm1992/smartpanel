#include <Filters.h>
int x;
int idea1; 
int idea2; 
int idea3; 
int idea4; 
float testFrequency = 60;                     // test signal frequency (Hz)
float windowLength = 20.0/testFrequency;// how long to average the signal, for statistist

int sensorValue1;
int sensorValue2;
int sensorValue3;
int sensorValue4;

float intercept1 = 0.0502; // to be adjusted based on calibration testing
float slope1 = 0.0451;// to be adjusted based on calibration testing
float intercept2 = 0.0521; // to be adjusted based on calibration testing
float slope2 = 0.0452;// to be adjusted based on calibration testing
float intercept3 = 0.0735; // to be adjusted based on calibration testing
float slope3 = 0.0439;// to be adjusted based on calibration testing
float intercept4 = 0.0675; // to be adjusted based on calibration testing
float slope4 = 0.045;// to be adjusted based on calibration testing

float current_amps1; // estimated actual current in amps
float current_amps2; // estimated actual current in amps
float current_amps3; // estimated actual current in amps
float current_amps4; // estimated actual current in amps

unsigned long printPeriod = 1000; // in milliseconds
// Track time in milliseconds since last reading 
unsigned long previousMillis = 0;

void setup() {
  Serial.begin( 9600 );    // start the serial port
}

void loop() {
  
  RunningStatistics inputStats;                 // create statistics to look at the raw test signal
  inputStats.setWindowSecs( windowLength );
  
  while(true){
    
  x = 0;
  while( x == 0 ) { 

    
    sensorValue1 = analogRead(A0);  // read the analog in value:
    inputStats.input(sensorValue1);  // log to Stats function
        
    if((unsigned long)(millis() - previousMillis) >= printPeriod) {
      previousMillis = millis();   // update time
      
      // display current values to the screen
      // convert signal sigma value to current in amps
      current_amps1 = intercept1 + slope1 * inputStats.sigma();
      if (inputStats.sigma() < 5){
        current_amps1 = 0;
      }
      idea1 = 100 * (current_amps1); 
      Serial.println("load1");
      Serial.println(idea1);
     
      x = 1;
    }
  }
  while( x == 1 ) {
       
    sensorValue2 = analogRead(A1);  // read the analog in value:
    inputStats.input(sensorValue2);  // log to Stats function
        
    if((unsigned long)(millis() - previousMillis) >= printPeriod) {
      previousMillis = millis();   // update time
      
      // display current values to the screen
      // convert signal sigma value to current in amps
      current_amps2 = intercept2 + slope2 * inputStats.sigma();
      if (inputStats.sigma() < 5){
        current_amps2 = 0;
      }
      idea2 = 100 * (current_amps2); 
      Serial.println(idea2);
      
      x = 2;
    }
  }
  while( x == 2 ) {   
    
    sensorValue3 = analogRead(A2);  // read the analog in value:
    inputStats.input(sensorValue3);  // log to Stats function
        
    if((unsigned long)(millis() - previousMillis) >= printPeriod) {
      previousMillis = millis();   // update time
      
      // display current values to the screen
      // convert signal sigma value to current in amps
      current_amps3 = intercept3 + slope3 * inputStats.sigma();
      if (inputStats.sigma() < 5){
        current_amps3 = 0;
      }
      idea3 = 100 * (current_amps3); 
      Serial.println(idea3);
      
      x = 3;
    }
  }
  while( x == 3 ) {   
    
    sensorValue4 = analogRead(A3);  // read the analog in value:
    inputStats.input(sensorValue4);  // log to Stats function
        
    if((unsigned long)(millis() - previousMillis) >= printPeriod) {
      previousMillis = millis();   // update time
      
      // display current values to the screen
      // convert signal sigma value to current in amps
      current_amps4 = intercept4 + slope4 * inputStats.sigma();
      if (inputStats.sigma() < 5){
        current_amps4 = 0;
      }
      idea4 = 100 * (current_amps4); 
      Serial.println(idea4);
      
      x = 0;
    }
  }
  }
  
}
