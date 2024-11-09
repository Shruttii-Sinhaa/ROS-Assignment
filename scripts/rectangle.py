#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

def move_turtle():
    rospy.init_node('draw_rectangle', anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

    move_cmd = Twist()

    side_1 = 4.0  # Length of the longer side
    side_2 = 1.0  # Length of the shorter side

    speed = 2.0  # Move at 2 m/s

    rate = rospy.Rate(1)  

    while not rospy.is_shutdown():
        for _ in range(2):  
            move_cmd.linear.x = speed  
            move_cmd.angular.z = 0.0  
            pub.publish(move_cmd)
            rospy.sleep(side_1 / speed)  

           
            move_cmd.linear.x = 0.0  
            move_cmd.angular.z = 1.57  
            pub.publish(move_cmd)
            rospy.sleep(1)  

            
            move_cmd.linear.x = speed  
            move_cmd.angular.z = 0.0 
            pub.publish(move_cmd)
            rospy.sleep(side_2 / speed)  

            
            move_cmd.linear.x = 0.0  
            move_cmd.angular.z = 1.57  
            pub.publish(move_cmd)
            rospy.sleep(1)  

if __name__ == '__main__':
    try:
        move_turtle()
    except rospy.ROSInterruptException:
        pass

