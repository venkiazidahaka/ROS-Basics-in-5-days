#! /usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

rospy.init_node('my_node')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
rate = rospy.Rate(2)
t = Twist()
t.linear.x = 1
t.angular.z = 1

while not rospy.is_shutdown():
    pub.publish(t)
    rate.sleep()
