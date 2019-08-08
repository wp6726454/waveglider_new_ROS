#!/usr/bin/env python
'''thrust_control ROS Node'''
import rospy
from std_msgs.msg import Float64
import pigpio
from PID import PID

class PID_controllor():

    def __init__(self):
          rospy.init_node('pwmbuilder', anonymous=True)
          rate = rospy.Rate(10) # 10hz
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
        
        self.controllor = PID(kp, kd, ki, minOutput, maxOutput, integratorMin, integratorMax)
        F=self.controller.update(course_real, course_desired)
        dc=-2.979e-07*F^6 + 1.496e-05*F^5 + 0.0003753*F^4 - 0.02246*F^3 -0.1342*F^2 + 21.09*F + 1497
        pi = pigpio.pi()
        pi.set_PWM_frequency(23,50)  #根据实际连接接口确定
        pi.set_PWM_range(23,20000)
        try:
            while Ture:
                pi.set_PWM_dutycycle(23,dc)

        except:
            pass
        pi.stop()


if __name__ == '__main__':
    rospy.spin()
    PID_controllor()