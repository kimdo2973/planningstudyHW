#!/usr/bin/env python
import rospy
from std_msgs.msg import String

class sub:
    def __init__(self):
        pass

    def callback(self,msg):
        rospy.loginfo(msg.data)

    def run(self):
        rospy.init_node("MotionPlanner",anonymous=False)
        rospy.Subscriber("Behavior",String,self.callback)
        pub = rospy.Publisher("Motion",String,queue_size=1)
        motion = "turn left"
        rate = rospy.Rate(1)
        while not rospy.is_shutdown():
            pub.publish(motion)
            rate.sleep()

if __name__=="__main__":
    S = sub()
    S.run()