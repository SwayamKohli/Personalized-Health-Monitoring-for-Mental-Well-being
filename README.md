# Personalized Health Monitoring for Mental Well-being

## Overview
The Personalized Health Monitoring for Mental Well-being project is an IoT-enabled system that collects and analyzes physiological and environmental data to assess mental health. It provides real-time insights, detects stress levels, and recommends personalized wellness strategies. The system also includes an emergency contact feature for immediate mental health support.

## Features
- **Real-Time Data Collection**: Gathers data from sensors such as heart rate monitors, GSR sensors, and temperature sensors.
- **Stress Detection**: Analyzes heart rate and GSR data to estimate stress levels.
- **Wellness Recommendations**: Offers personalized recommendations based on the detected stress level.
- **Data Visualization**: Utilizes a Kivy-based application for visual representation of vital metrics.
- **Emergency Contact**: Provides a button to display mental health support contacts.

## Architecture
The system includes the following key components:
- **ESP32 Microcontroller**: Central unit collecting and transmitting sensor data.
- **MAX30102 Sensor**: Measures heart rate and SpO2.
- **GSR Sensor**: Monitors skin conductivity to detect stress.
- **DS18B20 Sensor**: Records ambient temperature.
- **ThingSpeak Integration**: Cloud service for data storage and retrieval.
- **Kivy Application**: User interface for visualizing real-time data and stress levels.

## Project Structure
personalized-health-monitoring/
│
├── backend.cpp
├── frontend.py
├── config.yaml
├── IoT and Healthcare.pptx
└── README.md

## Prerequisites
- **Hardware**: ESP32, MAX30102, GSR sensor, DS18B20
- **Software**: Arduino IDE, Python 3.x, Kivy framework
- **Libraries**:
  - `ThingSpeak` for cloud integration
  - `requests` for data fetching in Python
  - `kivy` for the user interface

## Installation
### Clone the Repository:
```bash
git clone https://github.com/SwayamKohli/Personalized-Health-Monitoring-for-Mental-Well-being.git
cd Personalized-Health-Monitoring-for-Mental-Well-being
```

### Set Up the Backend:
Upload `backend.cpp` to your ESP32 device and configure the Wi-Fi credentials.

### Set Up the Frontend:
Ensure Python 3.x and the Kivy framework are installed:
```bash
pip install kivy
```

### Run the Application:
```bash
python frontend.py
```

## Usage
1. **Data Collection**: Ensure the sensors are connected to the ESP32 and data is being transmitted.
2. **Monitoring**: Run the Kivy app to visualize real-time data and stress levels.
3. **Emergency Contact**: Press the button in the app for immediate mental health support.

## Future Improvements
- Integrate machine learning for more accurate stress level predictions.
- Add multi-device synchronization for comprehensive monitoring.
- Enhance the mobile application for broader accessibility.

## Contributing
Contributions are welcome! Open an issue or submit a pull request for any bug fixes or new features.