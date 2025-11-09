import subprocess
import os
import time
from sensirion_i2c_driver import I2cConnection, LinuxI2cTransceiver
from sensirion_i2c_sen5x import Sen5xI2cDevice
from dotenv import load_dotenv

load_dotenv()

pois_paalta = False

def iv_kone_pois():
    ## Specify the path to the Python interpreter of the virtualenv
    python_bin = os.getenv("PYTHON_BIN")

    ## Specify the script's path that you want to execute under the virtualenv
    # IV-KONE POIS
    script_file = os.getenv("SWITCH_OFF")

    ## Launching the script as a subprocess
    subprocess.Popen([python_bin, script_file])

def iv_kone_paalle():
    python_bin = os.getenv("PYTHON_BIN")

    # IV-KONE PÄÄLLE
    script_file = os.getenv("SWITCH_ON")

    subprocess.Popen([python_bin, script_file])

i2c = LinuxI2cTransceiver('/dev/i2c-1')
device = Sen5xI2cDevice(I2cConnection(i2c))

# Print device information
print(f"Version: {device.get_version()}")
print(f"Serial Number: {device.get_serial_number()}")

# Perform a device reset (reboot firmware)
device.device_reset()

# Start measurement
device.start_measurement()
time.sleep(1)

def read_data():
    try:
        # Wait until next result is available
        print("Waiting for new data...")
        while device.read_data_ready() is False:
            time.sleep(0.1)
        # Read measured values -> clears the "data ready" flag
        values = device.read_measured_values()
        #print(values)
        
        print(values.mass_concentration_10p0.physical)
        
        if values.mass_concentration_10p0.physical > 5.5:
            iv_kone_pois()
            global pois_paalta
            pois_paalta = True

        if pois_paalta:
            if values.mass_concentration_10p0.physical < 5.2:
                iv_kone_paalle()
                pois_paalta = False

        # Read device status
        status = device.read_device_status()
        print("Device Status: {}\n".format(status))
    except Exception as e: # pylint: disable = broad-except
        print(f"Error: {e}")

while True:
    read_data()
    time.sleep(5)
