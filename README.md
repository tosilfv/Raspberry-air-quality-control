# Raspberry HVAC Air Quality Control

Made in Python for Raspberry Pi 4 Model B. This project measures air quality using a Sensirion Sen5x I2C sensor and automatically controls ventilation. It integrates with Philips Hue smart devices to optimize the environment.

### ⚙️ Tech Stack
Python | Raspberry Pi | Sensirion Sen5x (I2C) | Philips Hue API | Automation | Hardware-Software Integration

### 🛠 Installation

1. Clone the repository:
```bash
git clone https://github.com/tosilfv/Raspberry-air-quality-control.git
cd Raspberry-air-quality-control
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

### 🚀 Usage
3. Configure config.py with your sensor and Philips Hue device IDs:
```bash
python main.py
```

The system will:

Measure air quality (PM2.5, PM10, etc.)

Control ventilation automatically

Integrate with Philips Hue devices for environmental automation

---

📸 Demo & Setup Images
<div style="display: flex; gap: 10px; flex-wrap: wrap;"> <img src="https://raw.githubusercontent.com/tosilfv/Raspberry-air-quality-control/main/raspberry_air_quality/images/hvac_air_intake_vent.png" width="200"/> <img src="https://raw.githubusercontent.com/tosilfv/Raspberry-air-quality-control/main/raspberry_air_quality/images/raspberry_sensor.png" width="200"/> <img src="https://raw.githubusercontent.com/tosilfv/Raspberry-air-quality-control/main/raspberry_air_quality/images/philips_hue_bridge.png" width="200"/> <img src="https://raw.githubusercontent.com/tosilfv/Raspberry-air-quality-control/main/raspberry_air_quality/images/philips_hue_smart_plug.png" width="200"/> </div>
<br />

**📄 Notes**

Modular, maintainable Python code for small automation systems.

Designed for hands-on learning and practical automation projects.

Extendable with additional sensors or smart devices.


