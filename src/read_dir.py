# %%
import math
import std_msgs.msg as std
import numpy as np
import matplotlib.pyplot as plt
import os

# Preprocessing
# %%
i=0
data=[]
dir_name="/home/mike/Output/Corrected/Francesco.txt/arrays/"
for filename in os.listdir(dir_name):
    if filename.endswith(".npy"):
        array1=np.load(dir_name+"/"+filename)
        array1[:,2]=array1[:,2]-array1[0][2]
        data.append(array1)



# %%
#Plotting
fig=plt.figure(figsize=(20, 20), dpi=200)
ax1 = fig.add_subplot(111)
data=np.array(data)
for each in data:
    rgb = np.random.rand(3,)
    ax1.scatter(each[:,0],each[:,1],s=10, c=rgb)
    # plt.show()

# plt.legend(loc='upper left')
plt.show()

# %%
