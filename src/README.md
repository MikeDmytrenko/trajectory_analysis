Repo for capturing live trajectory data from SLAM and further proccessing.
Package can be used after exp_automated.bash script has finished and all poses were saved
slam_an.py captures node poses from the bag file.

Results_save.py processes this data into a dictionary with participant name and corresponding mean error values taken 
with respect to time and with distance.

Error is calculated by taking a map which looks 'good enough' and then compairing every run with it. 
Mean error with respect to time finds the nodes which are closest to each other in the time domain and then calculates the 
distance between them. Mean error with respect to distance performs the same but in the space domain.

bar_chart.py then vizualizes this data in the from of a bar chart. 


![bar_plot_with_distance](https://user-images.githubusercontent.com/47984690/151825515-37f8f0a3-b5b4-46d6-91a9-728ae2b41bc3.png)
![bar_plot_with_error_bars](https://user-images.githubusercontent.com/47984690/151825520-68f2606d-2a29-485c-b1c5-b89b1b216e8f.png)
