#!/usr/bin/env python
'''lmu ROS Node'''
# license removed for brevity
import rospy
from std_msgs.msg import Float64
import serial
import numpy as np
from math import sin, cos, atan
import json
import fileinput

def talker():
    '''lmu Publisher'''
    pub = rospy.Publisher('/course_real', Float64, queue_size=10)
    rospy.init_node('lmu', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    try:
        ser=serial.Serial('/dev/ttyACM0',9600)
    except Exception:
        print 'open serial failed.'
        exit(1)

    while True:
        s = ser.readline()
        am=str(s).strip().split(" ")
        if len(am)<14:
            continue
        else:
            a_x=float(am[2])
            a_y=float(am[4])
            a_z=float(am[6])
            m_x=float(am[9])
            m_y=float(am[11])
            m_z=float(am[13])

            #计算航向
            eta=atan(a_x/(np.sqrt(np.square(a_y)+np.square(a_z))))
            thita=atan(a_y/(np.sqrt(np.square(a_x)+np.square(a_z))))
            Hy=m_y*cos(thita)+m_x*sin(thita)*sin(eta)-m_z*cos(eta)*sin(thita)
            Hx=m_x*cos(eta)+m_z*sin(eta)
            phi=atan(Hy/Hx)
            #滤波程序
            phi_save='phi.json'
            with open(phi_save,'w') as phi_obj:
                json.dump(phi,phi_obj)
            count = len(open(phi_save, 'r').readlines())
            if count <200:
                continue
            else:
                for line in fileinput.input('phi.json', inplace=1):
                    if not fileinput.isfirstline():
                        print(line.replace('\n',''))

            phi_read=[]
            with open(phi_save) as f:
                for line in f:
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

            while not rospy.is_shutdown():
                pub.publish(phi_publish)
                rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
