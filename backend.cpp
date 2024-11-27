#include <Wire.h>
#include "MAX30105.h"
#include "spo2_algorithm.h"
#include <OneWire.h>
#include <DallasTemperature.h>
#include <WiFi.h>
#include "ThingSpeak.h"

// Pin definitions
#define GSR_PIN 36  // Analog pin for GSR sensor
#define ONE_WIRE_BUS 4  // DS18B20 data wire is connected to GPIO 4

// Wi-Fi credentials
const char* ssid = "null";
const char* password = "MHSS1510";
WiFiClient client;

// ThingSpeak details
unsigned long myChannelNumber = 2702924;
const char * myWriteAPIKey = "IKKXTLXHK1T69GAI";

unsigned long lastTime = 0;
unsigned long timerDelay = 15000;  // Send data every 15 seconds

// Objects
MAX30105 particleSensor;
OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature tempSensor(&oneWire);

// Variables for MAX30102
uint32_t irBuffer[100]; //infrared LED sensor data
uint32_t redBuffer[100];  //red LED sensor data
int32_t bufferLength; //data length
int32_t spo2; //SPO2 value
int8_t validSPO2; //indicator to show if the SPO2 calculation is valid
int32_t heartRate; //heart rate value
int8_t validHeartRate; //indicator to show if the heart rate calculation is valid

void setup() {
  Serial.begin(115200);
  Wire.begin();
  
  // Initialize MAX30102
  if (!particleSensor.begin(Wire, I2C_SPEED_FAST)) {
    Serial.println("MAX30102 was not found. Please check wiring/power.");
    while (1);
  }

  byte ledBrightness = 60; //Options: 0=Off to 255=50mA
  byte sampleAverage = 4; //Options: 1, 2, 4, 8, 16, 32
  byte ledMode = 2; //Options: 1 = Red only, 2 = Red + IR, 3 = Red + IR + Green
  byte sampleRate = 100; //Options: 50, 100, 200, 400, 800, 1000, 1600, 3200
  int pulseWidth = 411; //Options: 69, 118, 215, 411
  int adcRange = 4096; //Options: 2048, 4096, 8192, 16384

  particleSensor.setup(ledBrightness, sampleAverage, ledMode, sampleRate, pulseWidth, adcRange);
  
  // Initialize DS18B20
  tempSensor.begin();
  
  // Connect to Wi-Fi
  WiFi.begin(ssid, password);
  Serial.println("Connecting to WiFi");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
  
  ThingSpeak.begin(client);
}

void loop() {
  bufferLength = 100; //buffer length of 100 stores 4 seconds of samples running at 25sps

  //read the first 100 samples, and determine the signal range
  for (byte i = 0 ; i < bufferLength ; i++) {
    while (particleSensor.available() == false) //do we have new data?
      particleSensor.check(); //Check the sensor for new data

    redBuffer[i] = particleSensor.getRed();
    irBuffer[i] = particleSensor.getIR();
    particleSensor.nextSample(); //We're finished with this sample so move to next sample
  }

  //calculate heart rate and SpO2 after first 100 samples (first 4 seconds of samples)
  maxim_heart_rate_and_oxygen_saturation(irBuffer, bufferLength, redBuffer, &spo2, &validSPO2, &heartRate, &validHeartRate);

  // Read GSR
  int gsrValue = analogRead(GSR_PIN);
  
  // Read Temperature
  tempSensor.requestTemperatures();
  float tempC = tempSensor.getTempCByIndex(0);
  
  // Print data to Serial for debugging
  Serial.print("Heart Rate: ");
  Serial.print(heartRate, DEC);
  Serial.print(" bpm / SpO2: ");
  Serial.print(spo2, DEC);
  Serial.print("% / GSR: ");
  Serial.print(gsrValue);
  Serial.print(" / Temperature: ");
  Serial.print(tempC);
  Serial.println(" °C");
  
  // Send data to ThingSpeak
  if ((millis() - lastTime) > timerDelay) {
    // Check WiFi connection status
    if(WiFi.status() == WL_CONNECTED){
      ThingSpeak.setField(1, tempC);
      ThingSpeak.setField(2, heartRate);
      ThingSpeak.setField(3, gsrValue);
      ThingSpeak.setField(4, spo2);
      
      int x = ThingSpeak.writeFields(myChannelNumber, myWriteAPIKey);
      
      if(x == 200){
        Serial.println("Channel update successful.");
      }
      else{
        Serial.println("Problem updating channel. HTTP error code " + String(x));
      }
    }
    else {
      Serial.println("WiFi Disconnected");
      WiFi.reconnect();
    }
    lastTime = millis();
  }
  
  delay(500); // Short delay to prevent overwhelming the serial output
}