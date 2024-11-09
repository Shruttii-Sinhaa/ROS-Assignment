# The base git repo was cloned and a new python script was created to draw a rectangle using the turtlesim python-ROS.

You can find the rectangle.py file in the scripts. 

Steps to execute/run the scritp:

(Make sure that you have all the ROS turtlesim dependencies and packages installed)

    -> Clone the repo
    
    -> Run the commands below
    
            catkin_make
            
            source devel/setup.bash
    
    -> Open 3 different terminals and then run the commands below in each of them respectively
    
            roscore
            
            rosrun turtlesim turtlesim_node
            
            rosrun ros_session rectangle.py
