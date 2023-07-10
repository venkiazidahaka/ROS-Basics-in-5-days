#! /usr/bin/env python

import rospy
from nav_msgs.msg import Odometry


def callback(msg):
    print(msg.data)


rospy.init_node('odom_node')
sub = rospy.Subscriber('/odom', Odometry, callback)
rospy.spin()
