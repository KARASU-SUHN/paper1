#!/usr/bin/env python
# coding: utf-8

# In[30]:


# Read Text Files with Pandas using read_csv()
# importing pandas
import pandas as pd
  
# read text file into pandas DataFrame
G = pd.read_csv("/Users/karasu/Documents/KyushuUniv/paper1/SCG/datasets/highland.txt",sep="\s+",names=["node","link","weight"],dtype=object)
G=G.drop([0])
# display DataFrame
print(G)


# In[37]:


G1 = G[['node', 'link',"weight"]]


# In[38]:


import networkx as nx
G = nx.Graph()


# In[48]:


G = nx.from_pandas_edgelist(G1, 'node', 'link',"weight")
pos=nx.get_node_attributes(G,'weight')


# In[96]:


from matplotlib.pyplot import figure
figure(figsize=(5, 5))
#nx.draw_networkx(G, with_labels=True)
labels = nx.get_edge_attributes(G,'weight')
layout = nx.spring_layout(G)
#edge_colors=['blue','red']
#values = nx.get_edge_attributes(G,'weight')
nx.draw(G, layout,with_labels=True,node_color='#A0CBE2')#with_labels=True
#nx.draw_networkx_edge_labels(G, pos=layout)
#nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos=layout, edge_labels=labels)


# In[ ]:


#plt.savefig("path_to_fig.png")


# In[98]:



# read text file into pandas DataFrame
G = pd.read_csv("/Users/karasu/Documents/KyushuUniv/paper1/SCG/datasets/sampson.txt",sep="\s+",names=["node","link","weight"],dtype=object)
G=G.drop([0])
# display DataFrame
print(G)
G1 = G[['node', 'link',"weight"]]

import networkx as nx
G = nx.Graph()

G = nx.from_pandas_edgelist(G1, 'node', 'link',"weight")
pos=nx.get_node_attributes(G,'weight')

from matplotlib.pyplot import figure
figure(figsize=(5, 5))
#nx.draw_networkx(G, with_labels=True)
labels = nx.get_edge_attributes(G,'weight')
layout = nx.spring_layout(G)
#edge_colors=['blue','red']
#values = nx.get_edge_attributes(G,'weight')
nx.draw(G, layout,with_labels=True,node_color='green')#with_labels=True
#nx.draw_networkx_edge_labels(G, pos=layout)
#nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos=layout, edge_labels=labels)


# In[112]:


G = pd.read_csv("/Users/karasu/Documents/KyushuUniv/paper1/SCG/datasets/convote.txt",sep="\s+",names=["node","link","weight"],dtype=object)
G=G.drop([0])
# display DataFrame
print(G)
G1 = G[['node', 'link',"weight"]]

import networkx as nx
G = nx.Graph()

G = nx.from_pandas_edgelist(G1, 'node', 'link',"weight")
pos=nx.get_node_attributes(G,'weight')

from matplotlib.pyplot import figure
figure(figsize=(10, 10))
#nx.draw_networkx(G, with_labels=True)
labels = nx.get_edge_attributes(G,'weight')
layout = nx.spring_layout(G)
#edge_colors=['blue','red']
#values = nx.get_edge_attributes(G,'weight')
nx.draw(G, layout,with_labels=True,node_color='orange')#with_labels=True
#nx.draw_networkx_edge_labels(G, pos=layout)
#nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos=layout, edge_labels=labels)


# In[ ]:




