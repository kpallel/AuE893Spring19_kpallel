#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg          import Pose
from std_srvs.srv           import Empty


def circle():
    rospy.init_node('circle_turtle', anonymous=True)
    publisher = rospy.Publisher('/turtle1/cmd_vel',Twist, queue_size = 10)
    

    rate = rospy.Rate(10)                  
    vel_msg = Twist()
    linear_vel = 2
    angular_vel = 2

    while not rospy.is_shutdown():

	vel_msg.linear.x = linear_vel
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0

        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = angular_vel

        rospy.loginfo("linear_vel = %f: angular_vel = %f", linear_vel,angular_vel)
	publisher.publish(vel_msg)
        #rate.sleep(10)
        

if __name__ == '__main__':
    try:
        circle()
    except rospy.ROSInterruptException:
        pass


