# Personalized Health Monitoring for Mental Well-being

## Overview
The **Personalized Health Monitoring for Mental Well-being** project is an **IoT-enabled system** designed to monitor both physiological and environmental factors. By analyzing heart rate, SpO2, skin conductivity, and ambient temperature, it provides real-time insights into stress levels, offers **personalized wellness recommendations**, and facilitates **connections to mental health professionals** in emergencies.

---

## Features
- **📊 Real-Time Monitoring**: Collects and processes data from multiple sensors.
- **💡 Stress Analysis**: Combines heart rate and GSR data to estimate stress levels.
- **🎯 Personalized Recommendations**: Offers dynamic wellness tips to users.
- **📈 Data Visualization**: Interactive graphs powered by Kivy for real-time insights.
- **📞 Emergency Support**: Connects users to mental health resources.

---

## Architecture
### Key Components:
- **ESP32 Microcontroller**: Collects and transmits sensor data.
- **MAX30102**: Monitors heart rate and blood oxygen levels (SpO2).
- **GSR Sensor**: Measures skin conductivity to assess stress.
- **DS18B20**: Records ambient temperature.
- **ThingSpeak Integration**: Cloud storage for real-time data.
- **Kivy App**: Provides a sleek, user-friendly interface.

---

## 📁 Project Structure
```plaintext
personalized-health-monitoring/
├── backend.cpp               # ESP32 Backend Code
├── frontend.py               # Kivy-Based Frontend
├── LICENSE                   # License Information
└── README.md                 # Project Documentation
```

---

## Prerequisites
- **Hardware**: ESP32, MAX30102, GSR sensor, DS18B20
- **Software**: Arduino IDE, Python 3.x, Kivy framework
- **Libraries**:
  - `ThingSpeak` for cloud integration
  - `requests` for API calls
  - `kivy` for UI development

---

## Installation

1. **Clone the Repository**:
```bash
git clone https://github.com/SwayamKohli/Personalized-Health-Monitoring-for-Mental-Well-being.git
cd Personalized-Health-Monitoring-for-Mental-Well-being
```

2. **Set Up the Backend**:
- Upload `backend.cpp` to your ESP32 device.
- Configure Wi-Fi credentials in the code.

3. **Set Up the Frontend**:
Ensure Python 3.x and the Kivy framework are installed:
  ```bash
pip install kivy requests
```

4. **Run the Application**:
```bash
python frontend.py
```

---

## Usage
1. **Collect Data**: Ensure the sensors are connected and transmitting data.
2. **Monitor Health**: Visualize real-time metrics in the Kivy app.
3. **Emergency Contact**: Use the app to access mental health support.

---

## Future Improvements
- Machine learning models for advanced stress prediction.
- Mobile app integration for remote monitoring.
- Multi-device synchronization for comprehensive health tracking.

---

## 🐈‍⬛ GitHub Profiles of Creators:
[![GitHub Shreyash Agarwal](https://img.shields.io/badge/ShreyashAgarwal-%23FFFFFF.svg?logo=GitHub&logoColor=black)]() 
[![GitHub Swayam Kohli](https://img.shields.io/badge/SwayamKohli-%23FFFFFF.svg?logo=GitHub&logoColor=black)](https://github.com/SwayamKohli) 
[![GitHub Maitreyi Jha](https://img.shields.io/badge/MaitreyiJha-%23FFFFFF.svg?logo=GitHub&logoColor=black)]() 
[![GitHub Hitesh Kundu](https://img.shields.io/badge/HiteshKundu-%23FFFFFF.svg?logo=GitHub&logoColor=black)]() 

---

## ⚖️ License

This project is licensed under the [Creative Commons Attribution-NonCommercial 4.0 International Public License](LICENSE).  
For the full terms of this license, visit [Creative Commons Legal Code](https://creativecommons.org/licenses/by-nc/4.0/legalcode).

---

