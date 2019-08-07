#!/usr/bin/env python
'''station_keeping ROS Node'''
import rospy
from std_msgs.msg import UInt64MultiArray
from std_msgs.msg import Float64
from math import pi, atan
import numpy
from numpy import *

class Station_keeping():

    def __init__(self):
          rospy.init_node('station_keeping', anonymous=True)
          rate = rospy.Rate(10) # 10hz
          self.set_point=rospy.get_param('set_point',array([0,0]))
          self.pub = rospy.Publisher('/course_desired', Float64, queue_size=10)
          self.radius=rospy.get_param('radius',10)
          rospy.Subscriber("/position_real", UInt64MultiArray, self.callback)
          rate.sleep()

    def p_s(self,setpoint_x,setpoint_y,realposition_x,realposition_y):

        '''calculate the desired course based on the real-time location and set point'''
        if (numpy.square(setpoint_x-realposition_x)+numpy.square(setpoint_y-realposition_y)) > numpy.square(self.radius):
            
            if setpoint_x == realposition_x and setpoint_y > realposition_y:
                self.phid = pi/2

            elif setpoint_x == realposition_x and setpoint_y < realposition_y:
                self.phid = -pi/2

            elif setpoint_x > realposition_x and setpoint_y >= realposition_y:
                self.phid = atan((setpoint_y-realposition_y)/(setpoint_x-realposition_x))

            elif setpoint_x < realposition_x and setpoint_y >= realposition_y:
                self.phid = atan((setpoint_y-realposition_y)/(setpoint_x-realposition_x)) + pi           
   
            elif setpoint_x < realposition_x and setpoint_y < realposition_y:
                self.phid = atan((setpoint_y-realposition_y)/(setpoint_x-realposition_x)) - pi           
   
            else:
                self.phid = atan((setpoint_y-realposition_y)/(setpoint_x-realposition_x))

            return (self.phid)

        else:
            pass

    def callback(self,msg):
        '''station_keeping Callback Function'''
        rospy.loginfo("wave glider position:: %s", msg.data)
        
        while not rospy.is_shutdown():

            self.course_desired=self.p_s(self.set_point[0,0],self.set_point[0,1],msg.data[0,0],msg.data[0,1])

            self.pub.publish(self.course_desired)
            
 

if __name__ == '__main__':
    try:
        Station_keeping()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
