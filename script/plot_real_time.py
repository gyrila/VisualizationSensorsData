import time

import matplotlib.pyplot as plt
import serial
from matplotlib.animation import FuncAnimation

# Port parameters
PORT = '/dev/ttyACM0'
SPEED = 9600


plt.style.use('ggplot')
fig, ax = plt.subplots()
x_data, y_data = [], []
line, = ax.plot([], [])


def update(data):
    time, value_sensor = data
    x_data.append(time)
    y_data.append(value_sensor)
    line.set_data(x_data, y_data)
    ax.relim()
    ax.autoscale_view()
    print(time, value_sensor)
    return line, 
count = 1
def observer():
    try:
        with serial.Serial(PORT, SPEED, timeout=1) as ser:
            print(f"Connecting to the port {PORT}")
            time.sleep(2)
            global count 
            while True:
                ser_data = ser.readline().decode('utf-8')
                ser_data = float(ser_data)
                # print(f'{type(ser_data)} = {ser_data} - {count}')
                count+=1 
                yield count, ser_data
    except:
        print(f"Error connecting to port {PORT}")


ani = FuncAnimation(fig, update, frames=observer, blit=True, interval=10)
plt.show()