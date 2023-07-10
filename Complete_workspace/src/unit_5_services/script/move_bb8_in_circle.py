#! /usr/bin/env python
import rospy
from std_srvs.srv import Empty, EmptyResponse
from geometry_msgs.msg import Twist

move_bb8 = Twist()


def my_callback():
    move_bb8.linear.x = 0.2
    move_bb8.angular.z = 0.2
    pub.publish(bb8_service)
    rospy.loginfo("Service started")

    return EmptyResponse()


rospy.init_node("bb8_service_server")
bb8_service = rospy.Service("/move_bb8_in_circle", Empty, my_callback)

pub = rospy.Publisher("/cmd_vel", Twist, queue_size=1)
rospy.loginfo("Service /move_bb8_in_circle Ready")
rospy.spin()
