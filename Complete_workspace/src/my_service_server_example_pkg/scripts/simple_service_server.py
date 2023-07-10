#! /usr/bin/env python

import rospy
# you import the service message python classes generated from Empty.srv.
from std_srvs.srv import Empty, EmptyResponse


def my_callback(request):
    print("My callback has been called")
    return EmptyResponse()


rospy.init_node("service_server")
my_service = rospy.Service("/my_service", Empty, my_callback)
rospy.spin()
