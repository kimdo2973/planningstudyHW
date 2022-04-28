#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32

class pub:
    def __init__(self):
        pass

    def run(self):
        rospy.init_node("ControlInput",anonymous=False)
        pub1 = rospy.Publisher("x",Int32,queue_size=1)
        pub2 = rospy.Publisher("y",Int32,queue_size=1)
        x = 3
        y = 4
        rate = rospy.Rate(1)
        while not rospy.is_shutdown():
            pub1.publish(x)
            pub2.publish(y)

if __name__=="__main__":
    P = pub()
    P.run()