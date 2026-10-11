import serial
import csv
import time

# Port parameters
PORT = '/dev/ttyACM0'
SCOPE = 9600

# Folder parameters
PATH = 'data/'
FILE_NAME = 'data'

folder = open(f"{PATH}{FILE_NAME}.csv", 'w', newline='') 
sensor_writer = csv.writer(folder)

try:
    with serial.Serial(PORT, SCOPE, timeout=1) as ser:
        print(f"Connecting to the port {PORT}")
        time.sleep(2)
        while True:
            ser_data = ser.readline().decode('utf-8')
            print(ser_data)
            sensor_writer.writerow(ser_data.strip().split())
            folder.flush()
except:
    print(f"Error connecting to port {PORT}")