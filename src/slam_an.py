#! /usr/bin/env python3
from typing import Sized
from owlready2 import *
import random
import os
import rospy
import json
import std_msgs.msg as std
from visualization_msgs.msg import Marker
import numpy as np
from datetime import datetime

#import words_for_pico
os.chdir(sys.path[0])
#words_for_pico.run()
# file = open("vertices_list(1)","w+")
arr=[]

now = datetime.now()

dt_string = now.strftime("%d.%m.%Y %H:%M:%S")

filename=rospy.get_param("/current_filename")
fullpath="/home/mike/Output/Corrected/"+filename+"/arrays/"+dt_string


def callback(vertices):

    arr=[]
    for each in vertices.points:
        arr.append([each.x,each.y,each.z])


    
    os.makedirs(fullpath, exist_ok=True)
    np.save(fullpath,arr)
  
  
        

def listener():
    rospy.init_node('listener_for_word', anonymous=True)

    

    sub=rospy.Subscriber("Mapper/vertices", Marker, callback)

    rospy.spin()


if __name__=="__main__":
    # listener()

    # rospy.init_node('listener_new', anonymous=True)
    
    

    listener()


    print("done")
    