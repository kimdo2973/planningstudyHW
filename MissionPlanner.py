#!/usr/bin/env python
import rospy
from std_msgs.msg import String

class pub:
    def __init__(self):
        pass

    def run(self):
        rospy.init_node("MissionPlanner",anonymous=False)
        pub = rospy.Publisher("Mission",String,queue_size=1)
        mission = "Hello"
        rate = rospy.Rate(1)
        while not rospy.is_shutdown():
            pub.publish(mission)
            rate.sleep()

if __name__=="__main__":
    P = pub()
    P.run()