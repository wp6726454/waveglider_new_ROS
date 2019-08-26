#!/usr/bin/env python
'''thrust_control ROS Node'''
import rospy
from std_msgs.msg import Float64
#import pigpio
from PID import PID

class PID_controllor():

    def __init__(self):
        rospy.init_node('pwmbuilder', anonymous=True)
        rate = rospy.Rate(1) # 1hz
        self.course_real = 0.0
        self.course_desired = 0.0
        rospy.Subscriber("/course_real", Float64, self.callback_real)
        rospy.Subscriber("/course_desired", Float64, self.callback_desired)
        controllor = PID(5, 6, 0.1, -10, 10, -0.5, 0.5)
        while not rospy.is_shutdown():
            #calculate thrust by PID
            F = controllor.update(self.course_real, self.course_desired)
            #calculate pwm signal
            dc=-2.9*F
            rospy.loginfo("the result is %f", dc)
            rate.sleep()


    def callback_real(self, msg): 
        rospy.loginfo("the real course now is : %f", msg.data)
        self.course_real = msg.data
        
    def callback_desired(self, msg): 
        rospy.loginfo("the desired course now is : %f", msg.data)
        self.course_desired = msg.data


        
       
        '''
        pi = pigpio.pi()
        pi.set_PWM_frequency(23,50)  
        pi.set_PWM_range(23,20000)
        try:
            while Ture:
                pi.set_PWM_dutycycle(23,dc)

        except:
            pass
        pi.stop()
        '''

if __name__ == '__main__':
    try:
        PID_controllor()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
    
