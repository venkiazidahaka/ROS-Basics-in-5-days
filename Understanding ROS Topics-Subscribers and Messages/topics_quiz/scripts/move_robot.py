#! /usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

vel = Twist()

# vel.linear.x = 1


def check_and_avoid(msg):
    if msg.ranges[360] > 1:
        vel.linear.x = 0.5
        vel.angular.z = 0

    if msg.ranges[360] < 1:
        vel.linear.x = 0.1
        vel.angular.z = 0.5

    if msg.ranges[0] < 1:
        vel.linear.x = 0.1
        vel.angular.z = 0.5

    if msg.ranges[719] < 1:
        vel.linear.x = 0.1
        vel.angular.z = 0.5


rospy.init_node('topics_quiz_node')
sub = rospy.Subscriber("/kobuki/laser/scan", LaserScan,
                       callback=check_and_avoid, queue_size=1)
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
rate = rospy.Rate(2)
# pub.publish(vel)
# rate.sleep()
# rospy.spin()
# pub = rospy.Publisher('/cmd_vel', Int32, queue_size=1)


while not rospy.is_shutdown():
    pub.publish(vel)
    rate.sleep()
