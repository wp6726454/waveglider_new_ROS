#!/usr/bin/env python
'''thrust_control ROS Node'''
import rospy
from std_msgs.msg import Float64
from PID import PID

class PID_controllor():

    def __init__(self):
          rospy.init_node('pwmbuilder', anonymous=True)
          rate = rospy.Rate(10) # 10hz
          self.pub = rospy.Publisher('/pwm_signal', Float64, queue_size=10)
          rospy.Subscriber("/course_real", Float64, self.callback_real)
          rospy.Subscriber("/course_desired", Float64, self.callback_desired)
          rate.sleep()


    def callback_real(self, msg):
        
        global course_real 
        course_real = msg.data
        rospy.loginfo("the real course now is : %f", msg.data)
        
    def callback_desired(self, msg):

        global course_desired 
        course_desired = msg.data
        rospy.loginfo("the desired course now is : %f", msg.data)

    def pwm(self, course_desired, course_real):

        while not rospy.is_shutdown():

            self.controllor = PID(kp, kd, ki, minOutput, maxOutput, integratorMin, integratorMax)
            self.dc=f(self.controller.update(course_real, course_desired))
            self.pub.publish(self.dc)

if __name__ == '__main__':
# spin() simply keeps python from exiting until this node is stopped
    rospy.spin()
    PID_controllor()
