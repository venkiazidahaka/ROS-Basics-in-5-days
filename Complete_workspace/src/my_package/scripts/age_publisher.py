#! /usr/bin/env python

import rospy
from my_package.msg import Age

rospy.init_node('age_publisher_node')
pub = rospy.Publisher('/age', Age, queue_size=1)
rate = rospy.Rate(2)
age = Age()
age.years = 5
age.months = 5
age.days = 5

while not rospy.is_shutdown():
    pub.publish(age)
    rate.sleep()
