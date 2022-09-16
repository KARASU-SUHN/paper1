#!/usr/bin/env python
# coding: utf-8

# ##### 

# In[128]:


import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()

G.add_edge("0", "1", weight=1)
G.add_edge("1", "2", weight=-1)
G.add_edge("2", "3", weight=1)
G.add_edge("3", "0", weight=-1)
G.add_edge("4", "5", weight=1)
G.add_edge("5", "6", weight=-1)
G.add_edge("6", "7", weight=1)
G.add_edge("7", "4", weight=-1)
G.add_edge("3", "4", weight=1)
G.add_edge("0", "7", weight=1)

elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] > 0]
esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] <= 0]

#pos = nx.spring_layout(G, seed=23)  # positions for all nodes - seed for reproducibility
pos = nx.shell_layout(G) 
# nodes
#nx.draw_networkx_nodes(G, pos, node_size=700)

nx.draw_networkx_nodes(G, pos, node_size=700,node_color="#4169e1")

# edges
#nx.draw_networkx_edges(G, pos, edgelist=elarge, width=5)
nx.draw_networkx_edges(
    G, pos, edgelist=esmall, width=5, alpha=0.7, edge_color="r", style="dashed"
)
nx.draw_networkx_edges(
    G, pos, edgelist=elarge, width=5, alpha=0.7, edge_color="#000000", style="solid"
)

#https://www.colordic.org/ hexadecimal color code

# node labels
nx.draw_networkx_labels(G, pos, font_size=16, font_family="sans-serif")
# edge weight labels
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels)

ax = plt.gca()
ax.margins(0.08)
plt.axis("off")
plt.tight_layout()
plt.show()


# In[146]:


import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()

G.add_edge("0", "1", weight=1)
G.add_edge("1", "2", weight=-1)
G.add_edge("2", "3", weight=1)
G.add_edge("3", "0", weight=-1)
G.add_edge("4", "5", weight=1)
G.add_edge("5", "6", weight=-1)
G.add_edge("6", "7", weight=1)
G.add_edge("7", "4", weight=-1)
G.add_edge("3", "4", weight=1)
G.add_edge("0", "7", weight=1)

elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] > 0]
esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] <= 0]

#pos = nx.spring_layout(G, seed=23)  # positions for all nodes - seed for reproducibility
pos = nx.shell_layout(G) 
# nodes
#nx.draw_networkx_nodes(G, pos, node_size=700)

color_list = ["#008000", "#008000", "#ff8c00", "#ff8c00",
              "#ff8c00", "#ff8c00", "#008000","#008000"]

nx.draw_networkx_nodes(G, pos, node_size=700,node_color=color_list)

# edges

nx.draw_networkx_edges(
    G, pos, edgelist=esmall, width=5, alpha=0.7, edge_color="r", style="dashed"
)
nx.draw_networkx_edges(
    G, pos, edgelist=elarge, width=5, alpha=0.7, edge_color="#000000", style="solid"
)


# node labels
nx.draw_networkx_labels(G, pos, font_size=16, font_family="sans-serif")
# edge weight labels
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels)

ax = plt.gca()
ax.margins(0.08)
plt.axis("off")
plt.tight_layout()
plt.show()


# In[ ]:




