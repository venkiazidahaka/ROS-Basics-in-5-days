#! /usr/bin/env python

import time
import rospy
from services_quiz.srv import BB8CustomServiceMessage, BB8CustomServiceMessageResponse
from geometry_msgs.msg import Twist


def stop_bb8():
    rospy.loginfo("shutdown time! Stop the robot")

    move_square.linear.x = 0.0
    move_square.angular.z = 0.0
    my_pub.publish(move_square)


def move_x_time(moving_time, linear_speed=0.2, angular_speed=0.2):

    move_square.linear.x = linear_speed
    move_square.angular.z = angular_speed

    rospy.loginfo("Moving Forwards")
    my_pub.publish(move_square)
    time.sleep(moving_time)
    stop_bb8()
    rospy.loginfo("######## Finished Moving Forwards")


def square_movement(side=0.2):

    i = 0
    # More Speed, more time to stop
    time_magnitude = side / 0.2

    while i < 4:
        # Move Forwards
        move_x_time(moving_time=2.0*time_magnitude,
                    linear_speed=0.2, angular_speed=0.0)
        # Stop
        move_x_time(moving_time=4.0, linear_speed=0.0, angular_speed=0.0)
        # Turn, the turning is not afected by the length of the side we want
        move_x_time(moving_time=4.0, linear_speed=0.0, angular_speed=0.2)
        # Stop
        move_x_time(moving_time=0.1, linear_speed=0.0, angular_speed=0.0)

        i += 1
    rospy.loginfo("######## Finished Moving in a Square")


def my_callback(request):
    rospy.loginfo("The Service move_bb8_in_circle_custom has been called")

    repetitions_of_square = request.repetitions + 1
    new_side = request.side
    for i in range(repetitions_of_square):
        rospy.loginfo("Start Movement with side = " +
                      str(new_side)+"Repetition = "+str(i))
        square_movement(side=new_side)

    rospy.loginfo("Finished service move_bb8_in_square that was called called")
    response = BB8CustomServiceMessageResponse()
    response.success = True
    return response


rospy.init_node('service_move_bb8_in_square_custom_server')
# create the Service called move_bb8_in_circle with the defined callback
my_service = rospy.Service(
    '/move_bb8_in_square_custom', BB8CustomServiceMessage, my_callback)
my_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
move_square = Twist()
rate = rospy.Rate(1)
rospy.loginfo("Service /move_bb8_in_circle_custom Ready")
rospy.spin()  # mantain the service open.
