
# %%
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

# Preprocessing
# %%
array1=np.load("array.npy")
array1=array1
array1[:,2]=array1[:,2]-array1[0][2]
result_dict={}
# %% Loop, reads data for every participant from your data folder
for Participant_name in os.listdir("/home/mike/Output/Corrected"):


    data=[]
    dir_name="/home/mike/Output/Corrected/"+Participant_name+"/arrays/"
    for filename in os.listdir(dir_name):
        if filename.endswith(".npy"):
            array10=np.load(dir_name+"/"+filename)
            array10[:,2]=array10[:,2]-array10[0][2]
            data.append(array10)
   
    # Processing with time and distance
    error_dist_arr=[]
    error_dist=[]
    error_time_arr=[]
    error_time=[]
    for eachArr in data:
        for eachS in array1:
            smallest_time=100000.0
            smallest_dist=100000.0
            for eachB in eachArr:
                time_diff=abs(eachS[2]-eachB[2])
                dist=math.hypot(eachS[0]-eachB[0],eachS[1]-eachB[1])
                if time_diff<smallest_time:
                    smallest_time=time_diff
                    bigger_id_T=eachB
                if dist<smallest_dist:
                    smallest_dist=dist
                    bigger_id_D=eachB

            error_time.append([math.hypot(eachS[0]-bigger_id_T[0],eachS[1]-bigger_id_T[1]),round(eachS[2]-array1[0][2],3)])
            error_dist.append([smallest_dist,round(eachS[2]-array1[0][2],3)])
        error_time_arr.append(error_time)
        error_dist_arr.append(error_dist)

        error_time=[]
        error_dist=[]


  
    # Get mean
    meansT=[]
    meansD=[]
    error_time_arr=np.array(error_time_arr)
    for each in error_time_arr:
        meansT.append(np.mean(each[:,0]))

    error_dist_arr=np.array(error_dist_arr)

    for each in error_dist_arr:
        meansD.append(np.mean(each[:,0]))

    to_save=[meansT,meansD]
    result_dict[Participant_name.split('.')[0]]=np.transpose(to_save)

    # %%
    # Write to csv
    # header = ['Mean error time', 'Mean error time']

    # to_save=np.transpose(to_save)
    # with open('../Results/data1.csv', 'w', encoding='UTF8') as f:
    #     writer = csv.writer(f)
    #     writer.writerow("Name:"+Participant_name)
    #     writer.writerow(header)
    #     writer.writerows(to_save)
            

    # %%


   


with open('data_dic.pkl','wb') as f:
    pickle.dump(result_dict,f)

    # %%

    # to_save = pd.DataFrame(np.transpose(to_save))

    # to_save.to_csv('../Results/data1.csv', mode='a', header=['Mean error time', 'Mean error distance'], index_label=Participant_name)

# %%
