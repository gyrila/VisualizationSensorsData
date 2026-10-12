import csv
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

path = Path('data/data.csv')
lines = path.read_text().splitlines()
reader = csv.reader(lines)

# Remove data anomalies at the beginning of the recording.
for _ in range(5):
    next(reader)

humidity, temperature = [], []
for index, row in enumerate(reader, start=1):
    if  index % 2 == 0:
        temperature.append(row)
    else:
        humidity.append(row)

temperature = np.concatenate(temperature)
humidity = np.concatenate(humidity)

temperature = [float(value) for value in temperature]
humidity = [float(value) for value in humidity]

plt.style.use('ggplot')
fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.plot(range(len(temperature)), temperature, color='red')
ax2.plot(range(len(humidity)), humidity, color='blue')
ax1.set_title('Temperature')
ax2.set_title('Humidity')

plt.show()