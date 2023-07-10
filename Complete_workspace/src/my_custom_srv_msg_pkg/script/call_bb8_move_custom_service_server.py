#! /usr/bin/env python
import rospkg
import rospy
from my_custom_srv_msg_pkg.srv import MyCustomServiceMessage, MyCustomServiceMessageRequest


# Initialise a ROS node with the name service_client
rospy.init_node('service_move_bb8_in_circle_custom_client')
# Wait for the service client /move_bb8_in_circle_custom to be running
rospy.wait_for_service('/move_bb8_in_circle_custom')
move_bb8_in_circle_service_client = rospy.ServiceProxy(
    '/move_bb8_in_circle_custom', MyCustomServiceMessage)  # Create the connection to the service
# Create an object of type EmptyRequest
move_bb8_in_circle_request_object = MyCustomServiceMessageRequest()


"""
# BB8CustomServiceMessage
float64 side       # The distance of each side of the circle
int32 repetitions    # The number of times BB-8 has to execute the circle movement when the service is called
---
bool success         # Did it achieve it?
"""

move_bb8_in_circle_request_object.duration = 4

rospy.loginfo("Doing Service Call...")
# Send through the connection the path to the trajectory file to be executed
result = move_bb8_in_circle_service_client(move_bb8_in_circle_request_object)
rospy.loginfo(str(result))  # Print the result given by the service called

rospy.loginfo("END of Service call...")
