#!/usr/bin/env python
# coding: utf-8

# In[128]:


import csv
import matplotlib.pyplot as plt
import pandas as pd

data2 = pd.read_csv('/Users/karasu/Documents/KyushuUniv/paper1/time2.csv',index_col=0)
data6 = pd.read_csv('/Users/karasu/Documents/KyushuUniv/paper1/time6.csv')
data8 = pd.read_csv('/Users/karasu/Documents/KyushuUniv/paper1/time8.csv')
data20 = pd.read_csv('/Users/karasu/Documents/KyushuUniv/paper1/time20.csv')


# In[130]:


# print(data2)
#print(data20)


# In[ ]:


lns1 = ax1.plot(wnv3['mosq'], color='blue', lw=line_weight, alpha=alpha, label='Mosquitos')
lns2 = ax2.plot(wnv3['wnv'], color='orange', lw=line_weight, alpha=alpha, label='Westnile')
# Solution for having two legends
leg = lns1 + lns2
labs = [l.get_label() for l in leg]
ax1.legend(leg, labs, loc=0)


# In[40]:


# plt.figure()
# plt.rcParams['legend.fontsize'] = 'large'
ax = data2.plot(kind='line',figsize=(15,10),secondary_y=['highland','sampson','convote','WoW-EP8 ','Bitcoin',' WikiVot',' Referendum '],style='--.',use_index=False)
ax.set_ylabel('Execution time',fontsize=18)
ax.set_title('k=2',fontsize=18)
ax.right_ax.set_ylabel('Execution time(WikiCon)')
ax.tick_params(axis='x', labelrotation=90)
# plt.legend(loc=9, prop={'size': 15})
# plt.rc('legend',fontsize=20)


# In[114]:


import matplotlib.pyplot as plt
import numpy as np
x = np.array([0,1,2,3,4,5,6,7,8,9])
# add label to x axis
my_xticks = ["SCG-MA","SCG-MO","SCG-B "," SCG-R ", "KOCG-top-1"," KOCG-top-r ","BNC-k" ,"BNC-(k + 1)" ,"SPONGE-k","SPONGE-(k + 1)"]
# ax = data2.plot(kind='line',figsize=(15,5),secondary_y=['WikiCon'],style='--.',use_index=True,linewidth=2)

# add secondary y axis to present wikicon(large data)
ax2 = data2.plot(kind='line',figsize=(14,7),secondary_y=['Slashdot ','WikiCon','Epinions','WikiPol '], linestyle='dashed', marker='o',use_index=True,linewidth=3,fontsize=14)
# set 1st y axis label
ax2.set_ylabel('Execution time',fontsize=16)
ax2.set_title('k=2',fontsize=20)
# set secondary y axis label
ax2.right_ax.set_ylabel('Execution time(right)',fontsize=16)
# rotate x axis label
ax2.tick_params(axis='x', labelrotation=45)
plt.xticks(x, my_xticks)
# plt.rcParams['legend.title_fontsize'] = 'small'
plt.rc('legend',**{'fontsize':16})
# plt.show()


# In[115]:


x = np.array([0,1,2,3,4,5,6,7,8,9])
# add label to x axis
my_xticks = ["SCG-MA","SCG-MO","SCG-B "," SCG-R ", "KOCG-top-1"," KOCG-top-r ","BNC-k" ,"BNC-(k + 1)" ,"SPONGE-k","SPONGE-(k + 1)"]
# ax = data2.plot(kind='line',figsize=(15,5),secondary_y=['WikiCon'],style='--.',use_index=True,linewidth=2)

# add secondary y axis to present wikicon(large data)
ax6 = data6.plot(kind='line',figsize=(14,7),secondary_y=['Slashdot ','WikiCon','Epinions','WikiPol ',' Referendum '], linestyle='dashed', marker='o',use_index=True,linewidth=3,fontsize=14)
# set 1st y axis label
ax6.set_ylabel('Execution time',fontsize=16)
ax6.set_title('k=6',fontsize=20)
# set secondary y axis label
ax6.right_ax.set_ylabel('Execution time(right)',fontsize=16)
# rotate x axis label
ax6.tick_params(axis='x', labelrotation=45)
plt.xticks(x, my_xticks)
# plt.rcParams['legend.title_fontsize'] = 'small'
plt.rc('legend',**{'fontsize':16})
# plt.show()


# In[120]:


x = np.array([0,1,2,3,4,5,6,7])
# add label to x axis
my_xticks = ["SCG-MA","SCG-MO","SCG-B "," SCG-R ","BNC-k" ,"BNC-(k + 1)" ,"SPONGE-k","SPONGE-(k + 1)"]
# ax = data2.plot(kind='line',figsize=(15,5),secondary_y=['WikiCon'],style='--.',use_index=True,linewidth=2)

# add secondary y axis to present wikicon(large data)
ax8 = data8.plot(kind='line',figsize=(14,7),secondary_y=['Slashdot ','WikiCon','Epinions','WikiPol ',' Referendum '], linestyle='dashed', marker='o',use_index=True,linewidth=3,fontsize=14)
# set 1st y axis label
ax8.set_ylabel('Execution time',fontsize=16)
ax8.set_title('k=8',fontsize=20)
# set secondary y axis label
ax8.right_ax.set_ylabel('Execution time(right)',fontsize=16)
# rotate x axis label
ax8.tick_params(axis='x', labelrotation=45)
plt.xticks(x, my_xticks)
# plt.rcParams['legend.title_fontsize'] = 'small'
plt.rc('legend',**{'fontsize':16})
# plt.show()


# In[131]:


import matplotlib.pyplot as plt
import numpy as np
x = np.array([0,1,2,3,4,5,6])
# add label to x axis
my_xticks = ["SCG-MA","SCG-MO","SCG-R","BNC-k" ,"BNC-(k + 1)" ,"SPONGE-k","SPONGE-(k + 1)"]
# ax = data2.plot(kind='line',figsize=(15,5),secondary_y=['WikiCon'],style='--.',use_index=True,linewidth=2)

# add secondary y axis to present wikicon(large data)
ax20 = data20.plot(kind='line',figsize=(13,6),linestyle='dashed', marker='o',use_index=True,linewidth=3,fontsize=14)
# set 1st y axis label

ax20.set_ylabel('Execution time',fontsize=16)
ax20.set_title('k=20',fontsize=20)
# set secondary y axis label
# ax.right_ax.set_ylabel('Execution time(WikiCon)')
# rotate x axis label
ax20.tick_params(axis='x', labelrotation=45)
plt.xticks(x, my_xticks)
plt.rc('legend',**{'fontsize':16})
# plt.show()


# In[274]:


b = pd.read_csv('/Users/karasu/Documents/KyushuUniv/paper1/largesize/SCGB.csv',index_col=0)
ma = pd.read_csv('/Users/karasu/Documents/KyushuUniv/paper1/largesize/SCGMA.csv',index_col=0)
mo = pd.read_csv('/Users/karasu/Documents/KyushuUniv/paper1/largesize/SCGMO.csv',index_col=0)
r = pd.read_csv('/Users/karasu/Documents/KyushuUniv/paper1/largesize/SCGR.csv',index_col=0)


# In[292]:


plt.style.use('ggplot')
b.T.plot(kind='bar',figsize=(7.5,4.5),use_index=False,color=['firebrick', 'seagreen', 'chocolate', 'steelblue'])
x = np.array([0,1,2])
my_xticks = ["k=2","k=6","k=8"]
# b.tick_params(axis='x', labelrotation=45)
plt.yticks(fontsize=16)
plt.xticks(x, my_xticks, rotation=0,fontsize=16)
plt.ylabel('SCG-B', weight='bold',fontsize=16)


# In[291]:


plt.style.use('ggplot')
ma.T.plot(kind='bar',figsize=(7.5,4.5),use_index=False,color=['firebrick', 'seagreen', 'chocolate', 'steelblue'])
x = np.array([0,1,2,3])
my_xticks = ["k=2","k=6","k=8","k=20"]
# b.tick_params(axis='x', labelrotation=45)
plt.yticks(fontsize=14)
plt.xticks(x, my_xticks, rotation=0,fontsize=16)
plt.ylabel('SCG-MA', weight='bold',fontsize=16)


# In[290]:


plt.style.use('ggplot')
mo.T.plot(kind='bar',figsize=(7.5,4.5),use_index=False,color=['firebrick', 'seagreen', 'chocolate', 'steelblue'])
x = np.array([0,1,2,3])
my_xticks = ["k=2","k=6","k=8","k=20"]
# b.tick_params(axis='x', labelrotation=45)
plt.yticks(fontsize=14)
plt.xticks(x, my_xticks,rotation=0,fontsize=16)
plt.ylabel('SCG-MO', weight='bold',fontsize=16)


# In[289]:



plt.style.use('ggplot')
r.T.plot(kind='bar',figsize=(7.5,4.5),use_index=False,color=['firebrick', 'seagreen', 'chocolate', 'steelblue'])
x = np.array([0,1,2,3])
my_xticks = ["k=2","k=6","k=8","k=20"]
# b.tick_params(axis='x', labelrotation=45)
plt.yticks(fontsize=14)
plt.xticks(x, my_xticks,rotation=0,fontsize=16)
plt.ylabel('SCG-R', weight='bold',fontsize=16)


# In[ ]:




