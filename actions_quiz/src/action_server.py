#! /usr/bin/env python3

import rospy
import actionlib
from std_msgs.msg import Empty
from actions_quiz.msg import ArdroneAction, ArdroneFeedback, ArdroneResult

class SocoluiActionServer(object):

    _socului_feedback = ArdroneFeedback()
    _socului_result = ArdroneResult()

    def __init__(self):
        self._as = actionlib.SimpleActionServer("ardrone_action_server", ArdroneAction, self.socului_goal_callback, False)
        self._as.start()

    def socului_goal_callback(self, goal):
        socului_rate = rospy.Rate(1)
        socului_takeoff_pub = rospy.Publisher('/drone/takeoff', Empty, queue_size=1)
        socului_land_pub = rospy.Publisher('/drone/land', Empty, queue_size=1)

        if goal.command == "TAKEOFF":
            socului_takeoff_pub.publish(Empty())
            for i in range(3):
                self._socului_feedback.action = "TAKEOFF"
                self._as.publish_feedback(self._socului_feedback)
                socului_rate.sleep()

        elif goal.command == "LAND":
            socului_land_pub.publish(Empty())
            for i in range(3):
                self._socului_feedback.action = "LAND"
                self._as.publish_feedback(self._socului_feedback)
                socului_rate.sleep()

        self._as.set_succeeded(self._socului_result)

if __name__ == '__main__':
    rospy.init_node('socului_action_server')
    SocoluiActionServer()
    rospy.spin()
