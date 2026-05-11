#! /usr/bin/env python3

import rospy
from services_quiz.srv import MoveInCircle, MoveInCircleRequest

if __name__ == '__main__':
    rospy.init_node('es_service_client')

    rospy.wait_for_service('/move_in_circle')

    es_service = rospy.ServiceProxy('/move_in_circle', MoveInCircle)

    es_request = MoveInCircleRequest()
    es_request.side = 1.0
    es_request.repetitions = 2

    es_result = es_service(es_request)
    rospy.loginfo("Success: %s", es_result.success)
