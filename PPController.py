#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32
from std_msgs.msg import String

class sub:
    def __init__(self):
        pass

    def callback(self,msg):
        rospy.loginfo(msg.data)

    def run(self):
        rospy.init_node("PPController",anonymous=False)
        rospy.Subscriber("Motion",String,self.callback)
        rospy.Subscriber("x",Int32,self.callback)
        rospy.Subscriber("y",Int32,self.callback)
        while not rospy.is_shutdown():
            pass

if __name__=="__main__":
    S  = sub()
    S.run()