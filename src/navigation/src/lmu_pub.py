#!/usr/bin/env python
'''lmu ROS Node'''
# license removed for brevity
import rospy
from std_msgs.msg import Float64
import serial
import numpy as np
from math import sin, cos, atan


'''
def datafilter(input):
    ''采集连续的20个数据去掉最大值和最小值之后取中值'
    datalist = []
    if len(datalist)<20:
        datalist.append(input)
    else:
        del datalist[0]
        datalist.append(input)
    return(sum(datalist)/len(datalist))
''' 
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

    
            eta=atan(a_x/(np.sqrt(np.square(a_y)+np.square(a_z))))
            thita=atan(a_y/(np.sqrt(np.square(a_x)+np.square(a_z))))
            Hy=m_y*cos(thita)+m_x*sin(thita)*sin(eta)-m_z*cos(eta)*sin(thita)
            Hx=m_x*cos(eta)+m_z*sin(eta)
            phi=atan(Hy/Hx)


            while not rospy.is_shutdown():
                pub.publish(phi)
                rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
