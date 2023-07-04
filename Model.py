import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import random as r
import numpy as np
import matplotlib.colors
color = matplotlib.colors.LinearSegmentedColormap.from_list("", [(0.3, 0.39, 0), (1, 0.97, 0), (1, 1, 1)])


def new_consumers(x):
    return round(x * 0.05)


def generate_image():
    area = np.arange(225).reshape((15, 15))
    area = np.full((15, 15), 2)
    for el in range(int(number_of_clients)):
        i = r.randint(0, 14)
        j = r.randint(0, 14)
        while area[i][j] != 2:
            i = r.randint(0, 14)
            j = r.randint(0, 14)
        area[i][j] = 0
    for el in range(int(number_of_consumers)):
        i = r.randint(0, 14)
        j = r.randint(0, 14)
        while area[i][j] != 2:
            i = r.randint(0, 14)
            j = r.randint(0, 14)
        area[i][j] = 1
    return area


def change_image():
    n_cons = 0
    for i in range(15):
        for j in range(15):
            if area[i][j] == 1:
                n_cons += 1
    if n_cons > number_of_consumers:
        for el in range(n_cons - int(number_of_consumers)):
            ind = r.randint(0, 14)
            jnd = r.randint(0, 14)
            while area[ind][jnd] != 1:
                ind = r.randint(0, 14)
                jnd = r.randint(0, 14)
            area[ind][jnd] = 0
    elif n_cons < number_of_consumers:
        for el in range(int(number_of_consumers) - n_cons):
            ind = r.randint(0, 14)
            jnd = r.randint(0, 14)
            while area[ind][jnd] != 0:
                ind = r.randint(0, 14)
                jnd = r.randint(0, 14)
            area[ind][jnd] = 1


number_of_clients = 100
number_of_consumers = 0
clients = []
consumers = []
erase = []
duration = 20
days = np.array(np.arange(1, 100))
area = generate_image()
fig, ax = plt.subplots()
ax.imshow(area, cmap=color, vmin=0, vmax=2)
fig.set_figwidth(8)
fig.set_figheight(8)
plt.grid()
plt.show()
for i in range(len(days)):
    change = new_consumers(number_of_clients)
    percent = 1 + round(r.random(), 2)
    change = round(change * percent)
    erase.append(change)
    if i > duration:
        number_of_clients += erase[i-duration]
        number_of_consumers -= erase[i-duration]
    number_of_clients -= change
    number_of_consumers += change
    if i % 5 == 0:
        fig, ax = plt.subplots()
        change_image()
        ax.imshow(area, cmap=color, vmin=0, vmax=2)
        fig.set_figwidth(8)
        fig.set_figheight(8)
        plt.grid()
        plt.show()
    clients.append(number_of_clients)
    consumers.append(number_of_consumers)
dic = {'Clients': clients, 'Consumers': consumers, 'Days': days}
dataframe = pd.DataFrame(dic)
sns.lineplot(data=dataframe, x="Days", y="Consumers", label="Users", color='y')
sns.lineplot(data=dataframe, x="Days", y="Clients", label="Clients", color='g')
plt.grid()
plt.show()
print(dataframe)
