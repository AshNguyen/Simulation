import matplotlib
matplotlib.use('TkAgg')
from pylab import *
import networkx as nx
import random as rd

p_i = 0.5 # infection probability
p_r = 0.5 # recovery probability
p_e = 0.1  # connection probability
n = 100 # number of nodes

def initialize():
    global g, nextg
    g = nx.erdos_renyi_graph(n, p_e)
    g.pos = nx.spring_layout(g)
    for i in g.nodes:
        g.nodes[i]['state'] = 1 if rd.random() < .5 else 0
    nextg = g.copy()
    nextg.pos = g.pos

def observe():
    global g, nextg
    cla()
    nx.draw(g, vmin = 0, vmax = 1,
            node_color = [g.nodes[i]['state'] for i in g.nodes],
            pos = g.pos)
    ls = [g.nodes[a]['state'] for a in g.nodes]
    print(sum(ls)/len(ls))

def update():
    global g, nextg
    for a in list(g.nodes):
        if g.nodes[a]['state'] == 0: # if susceptible
            for b in list(g.neighbors(a)):
                if g.nodes[b]['state'] == 1: # if neighbor b is infected
                    nextg.nodes[a]['state'] = 1 if rd.random() < p_i else 0
        else: # if infected
            nextg.nodes[a]['state'] = 0 if rd.random() < p_r else 1
    g = nextg.copy()
    g.pos = nextg.pos


import pycxsimulator
pycxsimulator.GUI().start(func=[initialize, observe, update])