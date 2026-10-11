import serial
import time

PORT = '/dev/ttyACM0'
SCOPE = 9600

try:
    with serial.Serial(PORT, SCOPE, timeout=1) as ser:
        print(f"Connecting to the port {PORT}")
        time.sleep(2)
        while True:
            print(ser.readline().decode('utf-8'))
except:
    print(f"Error connecting to port {PORT}")