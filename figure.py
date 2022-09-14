#!/usr/bin/env python
# coding: utf-8

# In[9]:


# Read Text Files with Pandas using read_csv()
# importing pandas
import pandas as pd
import networkx as nx
from matplotlib.pyplot import figure

# read text file into pandas DataFrame
highland = pd.read_csv("/Users/karasu/Documents/KyushuUniv/paper1/SCG/datasets/highland.txt",sep="\s+",names=["node","link","weight"],dtype=object)
highland=highland.drop([0])
# display DataFrame
print(highland)

G1 = highland[['node', 'link',"weight"]]
highland = nx.Graph()

highland = nx.from_pandas_edgelist(G1, 'node', 'link','weight')
pos=nx.get_node_attributes(highland,'weight')

#draw figure
figure(figsize=(5, 5))
#nx.draw_networkx(G, with_labels=True)
labels = nx.get_edge_attributes(highland,'weight')
layout = nx.spring_layout(highland)
nx.draw(highland, layout,with_labels=True,node_color='#A0CBE2')#with_labels=False
labels = nx.get_edge_attributes(highland, "weight")
nx.draw_networkx_edge_labels(highland, pos=layout, edge_labels=labels)


# In[10]:


# read text file into pandas DataFrame
sampson = pd.read_csv("/Users/karasu/Documents/KyushuUniv/paper1/SCG/datasets/sampson.txt",sep="\s+",names=["node","link","weight"],dtype=object)
sampson=sampson.drop([0])
# display DataFrame
print(sampson)

G2 = sampson[['node', 'link',"weight"]]
sampson = nx.Graph()

sampson = nx.from_pandas_edgelist(G2, 'node', 'link','weight')
pos=nx.get_node_attributes(sampson,'weight')

#draw figure
figure(figsize=(5, 5))

labels = nx.get_edge_attributes(sampson,'weight')
layout = nx.spring_layout(sampson)
nx.draw(sampson, layout,with_labels=True,node_color='green')#with_labels=False
labels = nx.get_edge_attributes(sampson, "weight")
nx.draw_networkx_edge_labels(sampson, pos=layout, edge_labels=labels)


# In[12]:


# read text file into pandas DataFrame
convote = pd.read_csv("/Users/karasu/Documents/KyushuUniv/paper1/SCG/datasets/convote.txt",sep="\s+",names=["node","link","weight"],dtype=object)
convote=convote.drop([0])
# display DataFrame
print(convote)

G3 = convote[['node', 'link',"weight"]]
convote = nx.Graph()

convote = nx.from_pandas_edgelist(G3, 'node', 'link','weight')
pos=nx.get_node_attributes(convote,'weight')

#draw figure
figure(figsize=(12, 12))
labels = nx.get_edge_attributes(convote,'weight')
layout = nx.spring_layout(convote)
nx.draw(convote, layout,with_labels=True,node_color='orange')#with_labels=False
labels = nx.get_edge_attributes(convote, "weight")
nx.draw_networkx_edge_labels(convote, pos=layout, edge_labels=labels)


# In[25]:


# read text file into pandas DataFrame
wow8 = pd.read_csv("/Users/karasu/Documents/KyushuUniv/paper1/SCG/datasets/wow8.txt",sep="\s+",names=["node","link","weight"],dtype=object)
wow8=wow8.drop([0])
#print(wow8)
G4 = wow8[['node', 'link',"weight"]]
wow8 = nx.Graph()
wow8 = nx.from_pandas_edgelist(G4, 'node', 'link','weight')
pos=nx.get_node_attributes(wow8,'weight')
#draw figure
figure(figsize=(20, 20))
nx.draw(wow8,with_labels=False,node_color='blue',edge_color='grey')#with_labels=True


# In[ ]:




