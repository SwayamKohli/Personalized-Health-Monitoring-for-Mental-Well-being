# Personalized Health Monitoring for Mental Well-being

## 🏥 Overview
The **Personalized Health Monitoring for Mental Well-being** project is an **IoT-enabled system** designed to monitor both physiological and environmental factors. By analyzing heart rate, SpO2, skin conductivity, and ambient temperature, it provides real-time insights into stress levels, offers **personalized wellness recommendations**, and facilitates **connections to mental health professionals** in emergencies.

---

## ✨ Features
- **📊 Real-Time Monitoring**: Collects and processes data from multiple sensors.
- **💡 Stress Analysis**: Combines heart rate and GSR data to estimate stress levels.
- **🎯 Personalized Recommendations**: Offers dynamic wellness tips to users.
- **📈 Data Visualization**: Interactive graphs powered by Kivy for real-time insights.
- **📞 Emergency Support**: Connects users to mental health resources.

---

## 🛠️ Architecture
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
├── config.yaml               # Configuration Settings
├── LICENSE                   # License Information
└── README.md                 # Project Documentation
```

---

## 🚀 Prerequisites
- **Hardware**: ESP32, MAX30102, GSR sensor, DS18B20
- **Software**: Arduino IDE, Python 3.x, Kivy framework
- **Libraries**:
  - `ThingSpeak` for cloud integration
  - `requests` for API calls
  - `kivy` for UI development

---

## 📦 Installation
### Clone the Repository:
```bash
git clone https://github.com/SwayamKohli/Personalized-Health-Monitoring-for-Mental-Well-being.git
cd Personalized-Health-Monitoring-for-Mental-Well-being
```

### Set Up the Backend:
- Upload `backend.cpp` to your ESP32 device.
- Configure Wi-Fi credentials in the code.

### Set Up the Frontend:
- Ensure Python 3.x and the Kivy framework are installed:
  ```bash
  pip install kivy requests
  ```

### Run the Application:
```bash
python frontend.py
```

---

## 🎯 Usage
1. **Collect Data**: Ensure the sensors are connected and transmitting data.
2. **Monitor Health**: Visualize real-time metrics in the Kivy app.
3. **Emergency Contact**: Use the app to access mental health support.

---

## 🌟 Future Improvements
- Machine learning models for advanced stress prediction.
- Mobile app integration for remote monitoring.
- Multi-device synchronization for comprehensive health tracking.

---

## 🐈‍⬛ GitHub Profiles of Creators:
- [Swayam Kohli](https://github.com/SwayamKohli)  
- Shreyash Agarwal 
- Hitesh Kundu  
- Maitreyi Jha

---

## ⚖️ License

This project is licensed under the [Creative Commons Attribution-NonCommercial 4.0 International Public License](LICENSE).  

### Authors:
- Swayam Kohli  
- Shreyash Agarwal  
- Hitesh Kundi  
- Maitreyi Jha  

For the full terms of this license, visit [Creative Commons Legal Code](https://creativecommons.org/licenses/by-nc/4.0/legalcode).

## Contact
For queries or collaboration, reach out to **Swayam Kohli** at [swayam11489@gmail.com](mailto:swayam11489@gmail.com).

---

