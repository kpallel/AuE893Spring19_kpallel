#!/usr/bin/env python
import rospy
from geometry_msgs.msg  import Twist
from turtlesim.msg import Pose
from math import pow,atan2,sqrt

class turtlebot():

    def __init__(self):
        #Creating our node,publisher and subscriber
        rospy.init_node('turtlebot_controller', anonymous=True)
        self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        self.pose_subscriber = rospy.Subscriber('/turtle1/pose', Pose, self.update_pos)
        self.pose = Pose()
        self.rate = rospy.Rate(10)

    #Callback function implementing the pose value received
    def update_pos(self, data):
        self.pose = data
        self.pose.x = round(self.pose.x, 4)
        self.pose.y = round(self.pose.y, 4)

    def cal_distance(self, goal_x, goal_y):
        distance = sqrt(pow((goal_x - self.pose.x), 2) + pow((goal_y - self.pose.y), 2))
        return distance

    def move2goal(self):
	coordinates = [[0,0], [0,0], [0,0], [0,0], [0,0]]
        goal_pose = Pose()
	x_co = [5,8,8,5,5]
	y_co = [5,5,8,8,5]
	k=1.5

	for x in range (0,5):
	    X_pos = x_co[x]
	    Y_pos = y_co[x]
	    coordinates[x][0] = X_pos
	    coordinates[x][1] = Y_pos

       
        distance_tolerance = 0.05
        vel_msg = Twist()


	for i in range (0,5):
      	
            while abs((atan2(coordinates[i][1] - self.pose.y, coordinates[i][0] - self.pose.x) - self.pose.theta)) >= 0.005:
            
	    #angular velocity in the z-axis:
                vel_msg.angular.x = 0
                vel_msg.angular.y = 0
                vel_msg.angular.z = k * (atan2(coordinates[i][1] - self.pose.y, coordinates[i][0] - self.pose.x) - self.pose.theta)

            #Publishing our vel_msg
                self.velocity_publisher.publish(vel_msg)
                self.rate.sleep()
	    

	    while  sqrt(pow((coordinates[i][0] - self.pose.x), 2) + pow((coordinates[i][1] - self.pose.y), 2)) >= distance_tolerance:

            #Porportional Controller
            #linear velocity in the x-axis:
                vel_msg.linear.x = k * sqrt(pow((coordinates[i][0] - self.pose.x), 2) + pow((coordinates[i][1] - self.pose.y), 2))
                vel_msg.linear.y = 0
                vel_msg.linear.z = 0
	        vel_msg.angular.z = 0

 	        self.velocity_publisher.publish(vel_msg)
                self.rate.sleep()

          
        #Bringing the turtle to a halt
            vel_msg.linear.x = 0
            vel_msg.angular.z =0
            self.velocity_publisher.publish(vel_msg)

        rospy.spin()

if __name__ == '__main__':
    try:
        #Testing our function
        x = turtlebot()
        x.move2goal()

    except rospy.ROSInterruptException: pass
