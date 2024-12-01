import socket
import json

# Connect to the server
s = socket.socket()
host = '192.168.2.74'  # Replace with your Pi's IP address
port = 5000
s.connect((host, port))

# Receive and decode data
response = s.recv(1024).decode('utf-8')
data = json.loads(response)

# Print the data neatly
print(f"Core Temperature: {data['core_temperature']}°C")
print(f"ARM Clock Frequency: {data['arm_clock_frequency']} MHz")
print(f"Core Voltage: {data['core_voltage']} V")
print(f"Throttling Status: {data['throttling_status']}")

s.close()
