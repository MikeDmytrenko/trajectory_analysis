Repo for capturing live trajectory data from SLAM and further proccessing.

slam_an.py captures node poses from the bag file.

Results_save.py processes this data into a dictionary with participant name and corresponding mean error values taken 
with respect to time and with distance.

Error is calculated by taking a map which looks 'good enough' and then compairing every run with it. 
Mean error with respect to time finds the nodes which are closest to each other in the time domain and then calculates the 
distance between them. Mean error with respect to distance performs the same but in the space domain.

bar_chart.py then vizualizes this data in the from of a bar chart.
