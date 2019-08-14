#!/usr/bin/env python
'''lmutest ROS Node'''
# license removed for brevity
import rospy
from std_msgs.msg import Float64

def talker():
    '''lmutest Publisher'''
    pub = rospy.Publisher('/course_real', Float64, queue_size=10)
    rospy.init_node('lmutest', anonymous=True)
    rate = rospy.Rate(1) # 1hz
    while not rospy.is_shutdown():
        course_real = 2.0
        rospy.loginfo("The customized real course is : %s", str(course_real))
        pub.publish(course_real)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
