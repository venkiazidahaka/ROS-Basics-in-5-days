#! /usr/bin/env python
import rospkg
import rospy
from std_srvs.srv import Empty, EmptyRequest

rospy.init_node("move_bb8_client")
rospy.wait_for_service("/move_bb8_in_circle")
bb8_service_client = rospy.ServiceProxy("/move_bb8_in_circle", Empty)
bb8_service_client_request_object = EmptyRequest()

result = bb8_service_client(bb8_service_client_request_object)
print(result)
