#!/usr/bin/env python
'''BD ROS Node'''
# license removed for brevity
import rospy
from std_msgs.msg import UInt64MultiArray
import serial
import math
#from lmu_pub import datafilter
#import numpy as np
#from math import sin, cos, atan

#经纬度转换为平面坐标系中的x,y 利用米勒坐标系
def millerToXY (lon, lat):
    xy_coordinate = []  # 转换后的XY坐标集
    L = 6381372*math.pi*2
    W = L
    H = L/2
    mill = 2.3
    x = lon*math.pi/180
    y = lat*math.pi/180
    y = 1.25*math.log(math.tan(0.25*math.pi+0.4*y))
    x = (W/2)+(W/(2*math.pi))*x
    y = (H/2)-(H/(2*mill))*y
    xy_coordinate.append((int(round(x)),int(round(y))))
    return xy_coordinate

def talker():
    '''lmu Publisher'''
    pub = rospy.Publisher('/position_real', UInt64MultiArray, queue_size=10)
    rospy.init_node('gnss', anonymous=True)
    rate = rospy.Rate(1) # 10hz
    try:
        ser=serial.Serial('/dev/ttyUSB0',9600)

    except Exception:
        print 'open serial failed.'
        exit(1)

    while True:
        s = ser.readline()
        am = str(s).strip().split(" ")
        if len(am)<30:
            continue
        else:
            lon=float(am[11])
            lat=float(am[12])


            while not rospy.is_shutdown():
                pos = millerToXY(lon, lat)
                pos_xy = [-pos[1],pos[0]]
                pub.publish(pos_xy)
                rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass