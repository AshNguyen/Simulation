# Simple CA simulator in Python
#
# *** Hosts & Pathogens ***
#
# Copyright 2008-2012 Hiroki Sayama
# sayama@binghamton.edu

# Modified to run with Python 3

import matplotlib
matplotlib.use('TkAgg')

import pylab as PL
import random as RD
import scipy as SP
import numpy as np
import matplotlib.pyplot as plt

RD.seed()

width = 50
height = 50
initProb = 0.01
infectionRate = 0.85
regrowthRate = 0.15

def interactive_init_p(val=initProb):
    global time, config, nextConfig, initProb, infectionRate, regrowthRate, d_h, d_i
    initProb = float(val)
    return val 

def interactive_inf_p(val=infectionRate):
    global time, config, nextConfig, initProb, infectionRate, regrowthRate, d_h, d_i
    infectionRate = float(val)
    return val 

def interactive_grow_p(val=regrowthRate):
    global time, config, nextConfig, initProb, infectionRate, regrowthRate, d_h, d_i
    regrowthRate = float(val)
    return val 

def init():
    global time, config, nextConfig, initProb, infectionRate, regrowthRate, d_h, d_i

    time, d_h, d_i = [], [], []
    
    config = SP.zeros([height, width])
    for x in range(width):
        for y in range(height):
            if RD.random() < initProb:
                state = 2
            else:
                state = 1
            config[y, x] = state

    nextConfig = SP.zeros([height, width])

def draw():
    PL.cla()
    time.append(1)
    d_h.append(np.sum([config.flatten() == 1])/len(config.flatten()))
    d_i.append(np.sum([config.flatten() == 2])/len(config.flatten()))
    plt.subplot(2,1,1)
    PL.pcolor(config, vmin = 0, vmax = 2, cmap = PL.cm.jet)
    PL.axis('image')
    plt.subplot(2,1,2)
    plt.plot(np.cumsum(time), d_h, label='healthy {}'.format(d_h[-1]))
    plt.plot(np.cumsum(time), d_i, label='infected {}'.format(d_i[-1]))
    plt.legend()


def step():
    global time, config, nextConfig, initProb, infectionRate, regrowthRate, d_h, d_i

    for x in range(width):
        for y in range(height):
            state = config[y, x]
            if state == 0:
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        if config[(y+dy)%height, (x+dx)%width] == 1:
                            if RD.random() < regrowthRate:
                                state = 1
            elif state == 1:
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        if config[(y+dy)%height, (x+dx)%width] == 2:
                            if RD.random() < infectionRate:
                                state = 2
            else:
                state = 0

            nextConfig[y, x] = state
    config, nextConfig = nextConfig, config

import pycxsimulator
pycxsimulator.GUI(parameterSetters=[interactive_init_p, interactive_inf_p, interactive_grow_p]).start(func=[init,draw,step])
