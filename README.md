# Personalized Health Monitoring for Mental Well-being

This repository contains the implementation of an IoT-enabled system for personalized mental well-being monitoring. Developed for the CyberCup 4.0 Hackathon by Team NULL Pointers, the project integrates physiological and environmental data to assess mental health. Using sensors like MAX30102 for heart rate and SpO2, a GSR sensor for skin conductivity, and DS18B20 for temperature, the system collects real-time data processed via an ESP32 microcontroller.

# Key Features
- Real-time data collection from sensors.
- Data visualization through a Kivy-based application.
- Stress level calculation with personalized wellness recommendations.
- Emergency contact feature for immediate support.

# Technologies Used
- Hardware: ESP32, MAX30102, GSR sensor, DS18B20
- Software: Arduino IDE, Python, Kivy framework
- Cloud: ThingSpeak for data storage and retrieval

# How to Use
1. Upload the `backend.cpp` code to an ESP32 device.
2. Run the `frontend.py` script on a local machine with Python and Kivy installed.
3. Connect the device to the cloud for data transmission.

# Contributions
Contributions and feedback are welcome! Feel free to open an issue or submit a pull request.


