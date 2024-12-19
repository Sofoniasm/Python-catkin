#!/usr/bin/env python3

from std_msgs.msg import String
import rospy

def callback(data):
    rospy.loginfo("I heard: %s", data.data)

def subscriber():
    rospy.init_node('subscriber_node', anonymous=True)
    rospy.Subscriber('talking_topic', String, callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        subscriber()
    except rospy.ROSInterruptException:
        pass
