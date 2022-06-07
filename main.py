import networkx as nx
import matplotlib.pyplot as plt
from semestres import *

materias = []
for subject, dependencies in sems.items():
    for dependency in dependencies:
        temp = (dependency, subject)
        materias.append(temp)

G = nx.DiGraph()
G.add_edges_from(materias)
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=1000)
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_labels(G, pos)
plt.show()
