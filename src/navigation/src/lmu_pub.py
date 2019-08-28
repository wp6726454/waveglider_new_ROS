#!/usr/bin/env python
'''lmu ROS Node'''

# license removed for brevity
# encoding:utf-8
<<<<<<< HEAD
=======

>>>>>>> origin/master
import binascii
import rospy
from std_msgs.msg import Float64
import serial
import numpy as np
import math
from math import sin, cos, atan
import json
import fileinput
import math



def talker():
    '''lmu Publisher'''
    rospy.init_node('lmu', anonymous=True)
<<<<<<< HEAD
    pub = rospy.Publisher('/course_real', Float64, queue_size=10)
    rate = rospy.Rate(5) # 5hz
    while not rospy.is_shutdown():

        ser=serial.Serial('/dev/ttyUSB0',9600)
        data = str(binascii.b2a_hex(ser.read(14)))
        eve = data[21:25]
        course=float(eve)/10
        course_out=course*math.pi/180
        if course_out > math.pi:
            real_course = course_out-2*math.pi
        elif course_out < -math.pi:
            real_course = course_out+2*math.pi
        else:
            real_course = course_out

        phi=real_course
        phi_save='phi.json'
        with open(phi_save,'a') as phi_obj:
            phi_obj.write('\n'+str(phi))
        count = len(open(phi_save, 'r').readlines())
        if count <200:
            pass
        else:
            for line in fileinput.input('phi.json', inplace=1):
                if not fileinput.isfirstline():
                    print(line.replace('\n',''))
            for line in fileinput.input('phi.json', inplace=1):
                if not fileinput.isfirstline():
                    print(line.replace('\n',''))

        phi_read=[]
        with open(phi_save) as f:
            for line in f:
                if line.count('\n')==len(line):
                    pass
                else:
                    phi_read.append(line.strip('\n'))
        phi_read = list(map(float, phi_read))
        if len(phi_read) < 20:
            phi_publish=phi
        else:
            phi_read.reverse()
            phi_filter=phi_read[0:19]
            phi_filter.remove(max(phi_filter))
            phi_filter.remove(min(phi_filter))
            phi_publish=sum(phi_filter)/len(phi_filter)
        
        pub.publish(real_course)
        rospy.loginfo(real_course)
        rate.sleep()

        
=======
    rate = rospy.Rate(10) # 10hz

    while not rospy.is_shutdown():
        try:
            ser=serial.Serial('/dev/ttyUSB1',9600)
        except Exception:
            print ('open serial failed.')

        while True:
            data = str(binascii.b2a_hex(ser.read(14)))
            eve = data[21:25]
            course=float(eve)/10
            course_out=course*math.pi/180
            if course_out > math.pi:
                real_course = course_out-2*math.pi
            elif course_out < -math.pi:
                real_course = course_out+2*math.pi
            else:
                real_course = course_out

            phi=real_course
            phi_save='phi.json'
            with open(phi_save,'a') as phi_obj:
                phi_obj.write('\n'+str(phi))
            count = len(open(phi_save, 'r').readlines())
            if count <200:
                pass
            else:
                for line in fileinput.input('phi.json', inplace=1):
                    if not fileinput.isfirstline():
                        print(line.replace('\n',''))
                for line in fileinput.input('phi.json', inplace=1):
                    if not fileinput.isfirstline():
                        print(line.replace('\n',''))

            phi_read=[]
            with open(phi_save) as f:
                for line in f:
                    if line.count('\n')==len(line):
                        pass
                    else:
                        phi_read.append(line.strip('\n'))
            phi_read = list(map(float, phi_read))
            if len(phi_read) < 20:
                phi_publish=phi
            else:
                phi_read.reverse()
                phi_filter=phi_read[0:19]
                phi_filter.remove(max(phi_filter))
                phi_filter.remove(min(phi_filter))
                phi_publish=sum(phi_filter)/len(phi_filter)
            pub.publish(phi_publish)
            rospy.loginfo(phi_publish)
            rate.sleep()
>>>>>>> origin/master
                

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass