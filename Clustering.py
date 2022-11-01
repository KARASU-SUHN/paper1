#!/usr/bin/env python
# coding: utf-8

# In[1]:


import networkx as nx
import networkx.algorithms.community as nxcom
from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
plt.rcParams.update(plt.rcParamsDefault)
plt.rcParams.update({'figure.figsize': (15, 10)})
# get reproducible results
import random
from numpy import random as nprand
random.seed(123)
nprand.seed(123)


# In[3]:


G_karate = nx.karate_club_graph()
# Find the communities
communities = sorted(nxcom.greedy_modularity_communities(G_karate), key=len, reverse=True)
# Count the communities
print(f"The karate club has {len(communities)} communities.")


# In[4]:


def set_node_community(G, communities):
    '''Add community to node attributes'''
    for c, v_c in enumerate(communities):
        for v in v_c:
            # Add 1 to save 0 for external edges
            G.nodes[v]['community'] = c + 1
def set_edge_community(G):
    '''Find internal edges and add their community to their attributes'''
    for v, w, in G.edges:
        if G.nodes[v]['community'] == G.nodes[w]['community']:
            # Internal edge, mark with community
            G.edges[v, w]['community'] = G.nodes[v]['community']
        else:
            # External edge, mark as 0
            G.edges[v, w]['community'] = 0
def get_color(i, r_off=1, g_off=1, b_off=1):
    '''Assign a color to a vertex.'''
    r0, g0, b0 = 0, 0, 0
    n = 16
    low, high = 0.1, 0.9
    span = high - low
    r = low + span * (((i + r_off) * 3) % n) / (n - 1)
    g = low + span * (((i + g_off) * 5) % n) / (n - 1)
    b = low + span * (((i + b_off) * 7) % n) / (n - 1)
    return (r, g, b)


# In[5]:


# Set node and edge communities
set_node_community(G_karate, communities)
set_edge_community(G_karate)
node_color = [get_color(G_karate.nodes[v]['community']) for v in G_karate.nodes]
# Set community color for edges between members of the same community (internal) and intra-community edges (external)
external = [(v, w) for v, w in G_karate.edges if G_karate.edges[v, w]['community'] == 0]
internal = [(v, w) for v, w in G_karate.edges if G_karate.edges[v, w]['community'] > 0]
internal_color = ['black' for e in internal]


# In[56]:


karate_pos = nx.spring_layout(G_karate)
plt.rcParams.update({'figure.figsize': (11, 5)})
# Draw external edges
nx.draw_networkx(
    G_karate,
    pos=karate_pos,
    node_size=1,
    node_color="white",
     alpha=0.5,
    edgelist=external,
    width=2,
    edge_color="silver")
# Draw nodes and internal edges
nx.draw_networkx(
    G_karate,
    pos=karate_pos,
    node_color="white",
     alpha=1,
     width=1,
    edgelist=internal)
options = {
"node_size": 300,
"node_color": "white",
"edgecolors": "black",
"linewidths": 0.8
}
nx.draw_networkx_nodes(G_karate, pos=karate_pos, **options)
plt.show()


# In[55]:


karate_pos = nx.spring_layout(G_karate)
plt.rcParams.update({'figure.figsize': (11, 5)})
# Draw external edges
nx.draw_networkx(
    G_karate,
    pos=karate_pos,
    node_size=1,
    node_color="white",
     alpha=0.5,
    edgelist=external,
    width=2,
    edge_color="silver")
# Draw nodes and internal edges
nx.draw_networkx(
    G_karate,
    pos=karate_pos,
     alpha=1,
     width=1,
    edgelist=internal,
    node_color=node_color,
    edge_color=internal_color)
#     options = {
#     "node_size": 300,
#     "node_color": "white",
#     "edgecolors": "black",
#     "linewidths": 0.8
# }
#     nx.draw_networkx_nodes(G_karate, pos=karate_pos, **options)
plt.show()


# In[49]:


karate_pos = nx.spring_layout(G_karate)
plt.rcParams.update({'figure.figsize': (15, 10)})
# Draw external edges
nx.draw_networkx(
    G_karate,
    pos=karate_pos,
    node_size=1,
    edgelist=external,
    edge_color="silver")
# Draw nodes and internal edges
nx.draw_networkx(
    G_karate,
    pos=karate_pos,
    node_color=node_color,
    edgelist=internal,
    edge_color=internal_color)
plt.show()


# In[ ]:





# In[ ]:




