import matplotlib
matplotlib.use('TkAgg')
from pylab import *

n = 100 # size of space: n x n
p = 0.6 # probability of initially panicky individuals

def initialize():
    global config, nextconfig, density_alive, time
    config = zeros([n, n])
    for x in range(n):
        for y in range(n):
            config[x, y] = 1 if random() < p else 0
    nextconfig = zeros([n, n])
    density_alive = []
    time = []

    
def observe():
    global config, nextconfig, density_alive, time
    cla()
    density_alive.append(sum(config)/(config.shape[0]**2))
    time.append(1)
    plt.subplot(1,2,1)
    plt.plot(np.cumsum(time), density_alive)
    plt.subplot(1,2,2)
    imshow(config, vmin = 0, vmax = 1, cmap = cm.binary)

def update():
    global config, nextconfig, density_alive
    for x in range(n):
        for y in range(n):
            count = 0
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    count += config[(x + dx) % n, (y + dy) % n]
            if config[x, y] == 0 and count == 3: 
                nextconfig[x, y] = 1
            elif (config[x, y] == 1 and (count == 3 or count == 4)):
                nextconfig[x, y] = 1
            else: 
                nextconfig[x, y] = 0
    config, nextconfig = nextconfig, config

import pycxsimulator
pycxsimulator.GUI().start(func=[initialize, observe, update])
