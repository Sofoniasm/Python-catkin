#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from tutorials.msg import Position  

def talk_to_me():
    pub = rospy.Publisher('talking_topic', Position, queue_size=10)
    rospy.init_node('publisher_node', anonymous=True)
    rate = rospy.Rate(1)  # 1 Hz rate for publishing messages
    rospy.loginfo("Publisher Node started, now publishing messages")
    
    while not rospy.is_shutdown():
        msg = Position()
        msg.message = "My Position is: "
        msg.x = 2.0
        msg.y = 1.5
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        talk_to_me()
    except rospy.ROSInterruptException:
        pass

