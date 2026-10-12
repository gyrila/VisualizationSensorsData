import matplotlib.pyplot as plt

plt.style.use('ggplot')
fig, ax = plt.subplots()
x_data, y_data = [], []
line, = ax.plot([], [])

def update(time, value_sensor):
    x_data.append(time)
    