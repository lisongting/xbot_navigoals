#!/usr/bin/env python
#coding=utf-8


import rospy
from std_srvs.srv import Empty
import os

os.system('rosservice call /move_base/clear_costmaps ')

# rospy.wait_for_service('/move_base/clear_costmap')
# try:
# 	clear_costmap = rospy.ServiceProxy('/move_base/clear_costmaps', Empty)
# 	empty = Empty()
# 	resp1 = clear_costmap(empty)

# 	print resp1
# 	rospy.spinonce()
# except rospy.ServiceException, e:
# 	print "Service call failed: %s"%e