#!/usr/bin/env python

import rospy
import roslib
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from actionlib import SimpleActionClient, GoalStatus
from geometry_msgs.msg import *

def talker(x , y , w):
    rospy.init_node('talker', anonymous=True)

    sac = actionlib.SimpleActionClient('robot2/move_base', MoveBaseAction)
    rospy.loginfo('Sending point')
    sac.wait_for_server()
    goal = MoveBaseGoal()    #use self?
    #set goal
    goal.target_pose.header.frame_id = 'robot2_tf/odom'
    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose.position.x = x
    goal.target_pose.pose.position.y = y
    goal.target_pose.pose.orientation.w = w

    #start listner
    #sac.wait_for_server()

    #send goal
    sac.send_goal(goal)

    #finish
    sac.wait_for_result()
    
    if sac.get_state() == GoalStatus.SUCCEEDED:
        rospy.loginfo('Done')
    else:
        rospy.loginfo('Fail')
    
    

if __name__ == '__main__':
    try:
      
        talker( 6.75877,18.64450 , 0.9999)
        
    except rospy.ROSInterruptException:
        pass
