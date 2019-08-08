#!/usr/bin/env python
'''BD ROS Node'''
# license removed for brevity
import rospy
from std_msgs.msg import UInt64MultiArray
import serial
import math
import json
import fileinput
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
            
    lon_save='lon.json'
    lat_save='lat.json'

    with open(lon_save,'w') as lon_obj:
        json.dump(lon,lon_obj)
    with open(lat_save,'w') as lat_obj:
        json.dump(lat,lat_obj)

    count = len(open(lon_save, 'r').readlines())
    if count <200:
        continue
    else:
        for line in fileinput.input('lon.json', inplace=1):
            if not fileinput.isfirstline():
                print(line.replace('\n',''))

    lon_read=[]
    with open(lon_save) as f:
        for line in f:
            lon_read.append(line.strip('\n'))
    lon_read = list(map(float, lon_read))
    if len(lon_read)<20:
        lon_publish=lon
    else:
        lon_read.reverse()
        lon_filter=lon_read[0:19]
        lon_filter.remove(max(lon_filter))
        lon_filter.remove(min(lon_filter))
        lon_publish=sum(lon_filter)/len(lon_filter)

    lat_read=[]
    with open(lat_save) as f:
        for line in f:
            lat_read.append(line.strip('\n'))
    lat_read = list(map(float, lat_read))
    if len(lat)<20:
        lat_publish=lat
    else:
        lat.reverse()
        lat_filter=lon[0:19]
        lat_filter.remove(max(lat_filter))
        lat_filter.remove(min(lat_filter))
        lat_publish=sum(lat_filter)/len(lat_filter)

    while not rospy.is_shutdown():
                pos = millerToXY(lon_publish, lat_publish)
                pos_xy = [-pos[1],pos[0]]
                pub.publish(pos_xy)
                rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass