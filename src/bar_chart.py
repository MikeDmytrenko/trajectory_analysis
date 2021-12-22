# %%
# Imports

import math

from numpy.core.fromnumeric import mean
from numpy.core.multiarray import result_type
import std_msgs.msg as std
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import csv
import pickle
from collections import Counter
from Participant import Participant

# %%

file=open("data_dic.pkl","rb")

dict1=pickle.load(file)

# %% Reorder

reordered_keys= ['Stefano','Ariel','Anastasiia','Aliya','Mattea',
'Francesco','Gerald','Esra','Thanaphon','Francesco(1)','Amy','Sofia']

dict2={k: dict1[k] for k in reordered_keys}



# %% read csv 
intersections_dict={}
for filename in os.listdir('data'):
    if filename.endswith(".csv"):
        intersections=pd.read_csv('data/'+filename,engine='python',
        encoding='utf-8', error_bad_lines=False)

        intersections_dict[filename.split('.')[0]]=intersections

# %% Process intersections
Participant_list=[]
max_cl_loops=15
for eachName in dict2:
    count=0
    group=intersections_dict[eachName].groupby('Intersection num')['Recognized word'].apply(list)
    for index, value in group.iteritems():
        print(f"Index : {index}, Value : {value}")
        counter=Counter(value)
        
        for each in counter:
            if counter[each]>1:
                count=count+counter[each]-1

    Participant_list.append(Participant(eachName,dict2[eachName][:,0],dict2[eachName][:,1],count/max_cl_loops))

extra_part='Uncorrected'

Participant_list.append(Participant(extra_part,dict1[extra_part][:,0],dict1[extra_part][:,1],0))
# %% 
# Pre-proccess
x_values=[]
meansT=[]
meansD=[]
stdsT=[]
stdsD=[]
for each in Participant_list:
    x_values.append(each.name)
    meansT.append(np.mean(each.meansT))
    meansD.append(np.mean(each.meansD))
    stdsT.append(np.std(each.meansT))
    stdsD.append(np.std(each.meansT))
   
   
# %%
# Build the plot of Time
fig, ax = plt.subplots(figsize=(15, 5), dpi=100)

ax.bar(x_values, meansT, yerr=stdsT, align='center', alpha=0.5, ecolor='black', capsize=10)
ax.set_ylabel('Mean error in m')
ax.set_xticks(x_values)
ax.set_xticklabels(x_values)
ax.set_title('Errors across all participants with Time')
ax.yaxis.grid(True)

rects=ax.patches

labels=[round(i.perc_cl_loops,2) for i in Participant_list]

for rect, label in zip(rects, labels):
    height = rect.get_height()
    ax.text(
    rect.get_x() + rect.get_width() / 2, height + 5, label, ha="center", va="bottom")


# Save the figure and show
plt.tight_layout()
plt.savefig('bar_plot_timed.png')
plt.show()


# %%
fig, ax = plt.subplots(figsize=(15, 5), dpi=100)

ax.bar(x_values, meansD, yerr=stdsD, align='center', alpha=0.5, ecolor='black', capsize=10)
ax.set_ylabel('Mean error in m')
ax.set_xticks(x_values)
ax.set_xticklabels(x_values)
ax.set_title('Errors across all participants with Distance')
ax.yaxis.grid(True)

rects=ax.patches

labels=[round(i.perc_cl_loops,2) for i in Participant_list]

for rect, label in zip(rects, labels):
    height = rect.get_height()
    ax.text(
    rect.get_x() + rect.get_width() / 2, height + 5, label, ha="center", va="bottom")



# Save the figure and show
plt.tight_layout()
plt.savefig('bar_plot_with_distance.png')
plt.show()






# %%
