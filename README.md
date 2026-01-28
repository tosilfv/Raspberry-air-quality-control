# Raspberry HVAC Air Quality Control

A Python project for Raspberry Pi 4 that measures air quality using the Sensirion Sen5x I2C sensor and automatically controls ventilation. It also integrates with Philips Hue smart devices to optimize the environment.

### ⚙️ Tech Stack
Python | Raspberry Pi | Sensirion Sen5x (I2C) | Philips Hue API | Automation | Hardware-Software Integration

---

### 🛠 Installation

1. **Clone the repository:**
```bash
git clone https://github.com/tosilfv/Raspberry-air-quality-control.git
cd Raspberry-air-quality-control
```

2. Create and activate a virtual environment (recommended):
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Create a .env file in the project root with the following variables:<br />
PYTHON_BIN=/path/to/venv/bin/python<br />
SWITCH_ON=/path/to/iv_kone_paalle.py<br />
SWITCH_OFF=/path/to/iv_kone_pois.py<br />
BRIDGE=your_hue_bridge_ip<br />
IV_KONE=your_hue_light_id<br />

PYTHON_BIN points to the Python interpreter in your virtual environment.<br />
SWITCH_ON and SWITCH_OFF point to the scripts controlling the ventilation via Hue.<br />
BRIDGE and IV_KONE define the Hue Bridge IP and the device to control.<br />

### 🚀 Usage
A. Run the main program to start monitoring air quality:
```bash
python iv_kone.py
```

B. Behavior:

The system...

 - Measures air quality (PM1.0, PM2.5, PM10, etc.)

 - Turns off the ventilation if PM10 exceeds 5.5 µg/m³

 - Turns the ventilation back on when PM10 drops below 5.2 µg/m³

 - Automatically controls Philips Hue devices

---


**📄 Notes**

 - Make sure I2C is enabled on your Raspberry Pi: sudo raspi-config -> Interfacing Options -> I2C.

 - Philips Hue control requires the bridge IP and a registered application. Registration only needs to be done once using b.connect(). After that, the line can be commented out.

 - The code includes error handling and automatically resets the sensor when needed.
<br />

📸 Demo & Setup Images
<div style="display: flex; gap: 10px; flex-wrap: wrap;"> <img src="https://raw.githubusercontent.com/tosilfv/Raspberry-air-quality-control/main/raspberry_air_quality/images/hvac_air_intake_vent.png" width="200"/> <img src="https://raw.githubusercontent.com/tosilfv/Raspberry-air-quality-control/main/raspberry_air_quality/images/raspberry_sensor.png" width="200"/> <img src="https://raw.githubusercontent.com/tosilfv/Raspberry-air-quality-control/main/raspberry_air_quality/images/philips_hue_bridge.png" width="200"/> <img src="https://raw.githubusercontent.com/tosilfv/Raspberry-air-quality-control/main/raspberry_air_quality/images/philips_hue_smart_plug.png" width="200"/> </div>
<br />

📝 Additional Information

 - Modular and maintainable Python code for small automation projects

 - Easy to extend with additional sensors or smart devices
