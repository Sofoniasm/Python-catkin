#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def talk_to_me():
    pub = rospy.Publisher('talking_topic', String, queue_size=10)
    rospy.init_node('publisher_node', anonymous=True)
    rate = rospy.Rate(1)  # 1 Hz rate for publishing messages
    rospy.loginfo("Publisher Node started, now publishing messages")
    
    while not rospy.is_shutdown():
        msg = "Hello Sofi - %s" % rospy.get_time()
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        talk_to_me()
    except rospy.ROSInterruptException:
        pass

