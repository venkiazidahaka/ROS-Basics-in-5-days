#! /usr/bin/env python
import rospkg
import rospy
# Import the service message used by the service /execute_trajectory
from iri_wam_reproduce_trajectory.srv import ExecTraj, ExecTrajRequest

# Initialise a ROS node with the name service_client
rospy.init_node('service_execute_trajectory_client')
# Wait for the service client /execute_trajectory to be running
rospy.wait_for_service('/execute_trajectory')
execute_trajectory_service_client = rospy.ServiceProxy(
    '/execute_trajectory', ExecTraj)  # Create the connection to the service
# Create an object of type ExecTrajRequest
execute_trajectory_request_object = ExecTrajRequest()

"""
user:~/catkin_ws$ rossrv show iri_wam_reproduce_trajectory/ExecTraj
string file
---

"""

rospack = rospkg.RosPack()
# This rospack.get_path() works in the same way as $(find name_of_package) in the launch files.
traj = rospack.get_path('iri_wam_reproduce_trajectory') + \
    "/config/get_food.txt"

# Fill the variable file of this object with the desired file path
execute_trajectory_request_object.file = traj
# Send through the connection the path to the trajectory file to be executed
result = execute_trajectory_service_client(execute_trajectory_request_object)
print(result)  # Print the result type ExecTrajResponse
