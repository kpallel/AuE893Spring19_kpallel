


Question 1:
The python code circle.py has been written to make the turtle move in a circle.
A linear velocity of 2 m/s and and angular velocity of 2 rad/sec has been considered for the simulation.
The code runs pretty simple, based on the '/turtle1/cmd_vel' package. The code is published into this package and the control variables are manipulated.
Here we manipulate the 'vel_msg.linear.x' variable, which is the linear velocity of the turtle in the x-direction. Likewise, the angular velocity about the z-axis is manipulated through the variable 'vel_msg.angular.z'.
These variables are published into the cmd_vel package. This entire logic is defined in the def circle() definition.


Question 2:
The python code square_openloop.py has been written to make the turtle move in a square.
A linear velocity of 0.2 m/s and an angular velocity of 0.2 rad/sec can be given to the turtle.
The turtle completes a full square path and comes to a halt.
The code has been modified so as to compute for any given input of distance and velocity.
In this second question we are manipulating the same variables as seen in the previous question. But also we are defining the specific angular speed and relative angle to create the required 2x2 square.
First, we ask the turtle to move in the linear x-direction by giving an input. Then we ask the turtle to stop at the specified distance and rotate for 90 degrees. In each loop, the turtle completes on linear motion,
and one rotation motion. 

Question 3:
The python code square_closedloop.py has been written to make the turtle move in a square for the specified co-ordinates.
In this code we control the co-ordinates of the square using a linear distance formula and a steering formula.
A PID controller has also been used to fine tune the movement of the turtle. The code starts by creating a node, publisher and the subscriber. The goal is distance is defined to give the turtle a sense of destination.
Initial co-ordinates are also defined to start the square. The steering formula used determines the angle required by the turtle to turn in order to face the next goal destination, based on the specified co-ordinates.
The linear displacement is controlled using a distance formula between the present and goal co-ordinates. The turtle is programmed to slow down as the distance between the goal and present co-ordinates approaches a specified
tolerance value. This way both the angular and linear motion of the turtle are controlled to trace a 3x3 square with the specified co-ordinates.
