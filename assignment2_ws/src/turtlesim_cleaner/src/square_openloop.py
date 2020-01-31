#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
PI = 3.1415926535897

def move():
    # Starts a new node
    rospy.init_node('robot_cleaner', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()

	#Receiveing the user's input
    print("Let's move your robot")
    speed = input ("Input your speed:")
    #angle = input
    #speeda = input
    distance = input("Type your distance:")
    #isForward = True("Foward?: ")#True or False
    for i in range(0,4):
                

        #Checking if the movement is forward or backwards
        #if(isForward):
        vel_msg.linear.x = abs(speed)
   
        #else:
        #vel_msg.linear.x = -abs(speed)
        #Since we are moving just in x-axis
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
   

   

        #Setting the current time for distance calculus
        t0 = rospy.Time.now().to_sec()
        current_distance = 0
        

        #Loop to move the turtle in an specified distance
        while(current_distance < distance):
            #Publish the velocity
            velocity_publisher.publish(vel_msg)
            #Takes actual time to velocity calculus
            t1=rospy.Time.now().to_sec()
            #Calculates distancePoseStamped
            current_distance= speed*(t1-t0)
            #After the loop, stops the robot
        vel_msg.linear.x = 0
        #Force the robot to stop
       
        velocity_publisher.publish(vel_msg)
        t01 = rospy.Time.now().to_sec()
        current_angle = 0

        angular_speed = 90 * 2 * PI / 360
        relative_angle = 90 * 2 * PI / 360
        vel_msg.angular.z = angular_speed

        while(current_angle < relative_angle):
            velocity_publisher.publish(vel_msg)
            t11 = rospy.Time.now().to_sec()
            current_angle = angular_speed*(t11-t01)


        #Forcing our robot to stop
        vel_msg.angular.z = 0
        velocity_publisher.publish(vel_msg)
       


if __name__ == '__main__':
    try:
        #Testing our function
        move()
    except rospy.ROSInterruptException: pass
