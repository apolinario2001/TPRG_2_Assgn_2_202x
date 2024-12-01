import socket
import os
import json

# Initialize the server
s = socket.socket()
host = ''  # Bind to all interfaces
port = 5000
s.bind((host, port))
s.listen(5)

# Functions to retrieve data from vcgencmd
def get_core_temp():
    result = os.popen('vcgencmd measure_temp').readline()
    return float(result.replace("temp=", "").replace("'C\n", ""))

def get_arm_clock():
    result = os.popen('vcgencmd measure_clock arm').readline()
    return int(result.split("=")[1]) / 1e6  # Convert Hz to MHz

def get_core_voltage():
    result = os.popen('vcgencmd measure_volts core').readline()
    return float(result.replace("volt=", "").replace("V\n", ""))

def get_throttling_status():
    result = os.popen('vcgencmd get_throttled').readline()
    return result.split("=")[1].strip()

# Server loop
while True:
    c, addr = s.accept()
    print('Got connection from', addr)
    
    # Collect data
    data = {
        "core_temperature": get_core_temp(),
        "arm_clock_frequency": get_arm_clock(),
        "core_voltage": get_core_voltage(),
        "throttling_status": get_throttling_status()
    }
    
    # Convert to JSON and send
    res = json.dumps(data).encode('utf-8')
    c.send(res)
    c.close()
