# import necessary module

from mpl_toolkits.mplot3d import axes3d

import matplotlib.pyplot as plt

import numpy as np

# load data from file

# you replace this using with open

data1 = np.loadtxt("datadd.txt")

first_2000 = data1[:, 3]

second_2000 = data1[:, 7]

third_2000 = data1[:, 11]

data2 = np.loadtxt("datadd.txt")

first_1000 = data2[:, 3]

second_1000 = data2[:, 7]

third_1000 = data2[:, 11]

# new a figure and set it into 3d

fig = plt.figure()

ax = fig.gca(projection='3d')

# set figure information

ax.set_title("3D_Curve")

ax.set_xlabel("x")

ax.set_ylabel("y")

ax.set_zlabel("z")

# draw the figure, the color is r = read

figure1 = ax.plot(first_2000, second_2000, third_2000, c='r')

figure2 = ax.plot(first_1000, second_1000, third_1000, c='b')

plt.show()
