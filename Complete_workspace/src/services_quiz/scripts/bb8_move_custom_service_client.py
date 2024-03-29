#! /usr/bin/env python

import rospkg
import rospy
from services_quiz.srv import BB8CustomServiceMessage, BB8CustomServiceMessageRequest

# Initialise a ROS node with the name service_client
rospy.init_node('service_move_bb8_in_square_custom_client')
# Wait for the service client /move_bb8_in_square to be running
rospy.wait_for_service('/move_bb8_in_square_custom')
move_bb8_in_square_service_client = rospy.ServiceProxy(
    '/move_bb8_in_square_custom', BB8CustomServiceMessage)  # Create the connection to the service
# Create an object of type EmptyRequest
move_bb8_in_square_request_object = BB8CustomServiceMessageRequest()


"""
# BB8CustomServiceMessage
float64 side       # The distance of each side of the square
int32 repetitions    # The number of times BB-8 has to execute the square movement when the service is called
---
bool success         # Did it achieve it?
"""
move_bb8_in_square_request_object.side = 1
move_bb8_in_square_request_object.repetitions = 2

rospy.loginfo("Start Two Small Squares...")
# Send through the connection the path to the trajectory file to be executed
result = move_bb8_in_square_service_client(move_bb8_in_square_request_object)
rospy.loginfo(str(result))  # Print the result given by the service called

move_bb8_in_square_request_object.side = 0.6
move_bb8_in_square_request_object.repetitions = 1

rospy.loginfo("Start One Big Square...")
# Send through the connection the path to the trajectory file to be executed
result = move_bb8_in_square_service_client(move_bb8_in_square_request_object)
rospy.loginfo(str(result))

rospy.loginfo("END of Service call...")
