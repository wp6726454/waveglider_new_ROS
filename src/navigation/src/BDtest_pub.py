#!/usr/bin/env python
'''BDtest ROS Node'''
# license removed for brevity
import rospy
from std_msgs.msg import Float32MultiArray

def talker():
    '''BDtest Publisher'''
    pub = rospy.Publisher('/position_real', Float32MultiArray, queue_size=10)
    rospy.init_node('BDtest', anonymous=True)
    rate = rospy.Rate(1) # 1hz
    while not rospy.is_shutdown():
        pos_1 = [121, 31]
        pos = Float32MultiArray(data=pos_1)
        pub.publish(pos)
        rospy.loginfo(pos.data)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
