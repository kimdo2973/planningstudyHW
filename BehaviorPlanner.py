#!/usr/bin/env python
import rospy
from std_msgs.msg import String

class sub:
    def __init__(self):
        pass

    def callback(self,msg):
        rospy.loginfo(msg.data)

    def run(self):
        rospy.init_node("BehaviorPlanner",anonymous=False)
        rospy.Subscriber("Mission",String,self.callback)
        pub = rospy.Publisher("Behavior",String,queue_size=1)
        behavior = "Move"
        rate = rospy.Rate(1)
        while not rospy.is_shutdown():
            pub.publish(behavior)
            rate.sleep()


if __name__=="__main__":
    S  = sub()
    S.run()
