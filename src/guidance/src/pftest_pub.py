#!/usr/bin/env python
'''pftest ROS Node'''
# license removed for brevity
import rospy
from std_msgs.msg import Float64
import random

def talker():
    '''pftest Publisher'''
    pub = rospy.Publisher('/course_desired', Float64, queue_size=10)
    rospy.init_node('pftest', anonymous=True)
    rate = rospy.Rate(1) # 1hz
    while not rospy.is_shutdown():
        course_des = random.uniform(0, 1)
        rospy.loginfo("The customized desired course is: %s", str(course_des) )
        pub.publish(course_des)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
