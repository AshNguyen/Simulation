import matplotlib
matplotlib.use('TkAgg')
from pylab import *
import networkx as nx
import random as rd

def initialize():
    g = nx.karate_club_graph()
    g.pos = nx.spring_layout(g)
    for i in g.nodes:
        g.nodes[i]['state'] = 1 if random() < .5 else 0
    step = 0
    return g, step
# def observe():
#     global g, step, states
#     cla()
#     nx.draw(g, vmin = 0, vmax = 1,
#             node_color = [g.nodes[i]['state'] for i in g.nodes],
#             pos = g.pos)
    

def update(g, step):
    listener = rd.choice(list(g.nodes))
    speaker = rd.choice(list(g.neighbors(listener)))
    g.nodes[listener]['state'] = g.nodes[speaker]['state']
    step += 1
    states = [g.nodes[i]['state'] for i in g.nodes]
    if ((np.sum(states)/len(states)) == 1 or (np.sum(states)/len(states) == 0)):
        print('Homogeneity reached at step {}'.format(step))
        return False, step
    else: 
        return True, step

# import pycxsimulator
# pycxsimulator.GUI().start(func=[initialize, observe, update])

def experiment(n): 
    record = []
    for _ in range(n): 
        condition = True
        graph, step = initialize()
        while condition: 
            condition, last_step = update(graph, step)
        record.append(last_step)
    return record
experiment(1)