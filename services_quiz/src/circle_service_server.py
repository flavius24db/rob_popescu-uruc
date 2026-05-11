#! /usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from services_quiz.srv import MoveInCircle, MoveInCircleResponse

def es_callback(request):
    es_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    es_rate = rospy.Rate(10)

    es_radius = request.side
    es_repetitions = request.repetitions

    if es_radius <= 0 or es_repetitions <= 0:
        return MoveInCircleResponse(success=False)

    es_linear = 0.3
    es_angular = es_linear / es_radius

    es_twist = Twist()
    es_twist.linear.x = es_linear
    es_twist.angular.z = es_angular

    es_stop = Twist()

    es_duration = (2 * 3.14159 * es_radius / es_linear)

    for i in range(es_repetitions):
        es_start = rospy.Time.now()
        while (rospy.Time.now() - es_start).to_sec() < es_duration:
            es_pub.publish(es_twist)
            es_rate.sleep()

    es_pub.publish(es_stop)
    return MoveInCircleResponse(success=True)

if __name__ == '__main__':
    rospy.init_node('es_service_server')
    es_service = rospy.Service("/move_in_circle", MoveInCircle, es_callback)
    rospy.spin()
