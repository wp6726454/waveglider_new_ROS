#!/usr/bin/env python
'''BD ROS Node'''
# license removed for brevity
import rospy
from std_msgs.msg import Float32MultiArray
import serial
import math
import json
import fileinput
#from lmu_pub import datafilter
#import numpy as np
#from math import sin, cos, atan

def talker():
    '''GNSS Publisher'''
    pub = rospy.Publisher('/position_real', Float32MultiArray, queue_size=10)
    rospy.init_node('gnss', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        try:
            ser=serial.Serial('/dev/ttyUSB0',9600)
        except Exception:
            print ('open serial failed.')
            exit(1)
        while True:
            s = ser.readline()
            am = str(s).strip().split(",")
            if len(am)<15:
                continue
            else:
                lon=float(am[11])
                lat=float(am[12])
 
                lon_save='lon.json'
                with open(lon_save,'a') as lon_obj:
                    lon_obj.write('\n'+str(lon))
                count = len(open(lon_save, 'r').readlines())
                if count < 200:
                    pass
                else:
                    for line in fileinput.input('lon.json', inplace=1):
                        if not fileinput.isfirstline():
                            print(line.replace('\n',''))
                    for line in fileinput.input('lon.json', inplace=1):
                        if not fileinput.isfirstline():
                            print(line.replace('\n',''))
                lon_read=[]
                with open(lon_save) as f:
                    for line in f:
                        if line.count('\n')==len(line):
                            pass
                        else:
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
                    
                lat_save='lat.json'
                with open(lat_save,'a') as lat_obj:
                    lat_obj.write('\n'+str(lat))
                count = len(open(lat_save, 'r').readlines())
                if count < 200:
                    pass
                else:
                    for line in fileinput.input('lat.json', inplace=1):
                        if not fileinput.isfirstline():
                            print(line.replace('\n',''))
                    for line in fileinput.input('lat.json', inplace=1):
                        if not fileinput.isfirstline():
                            print(line.replace('\n',''))
            
                lat_read=[]
                with open(lat_save) as f:
                    for line in f:
                        if line.count('\n')==len(line):
                            pass
                        else:
                            lat_read.append(line.strip('\n'))
                lat_read = list(map(float, lat_read))
                if len(lat_read)<20:
                    lat_publish=lon
                else:
                    lat_read.reverse()
                    lat_filter=lat_read[0:19]
                    lat_filter.remove(max(lat_filter))
                    lat_filter.remove(min(lat_filter))
                    lat_publish=sum(lat_filter)/len(lat_filter)

                pos_1 = [lon, lat]
                pos = Float32MultiArray(data=pos_1)
                pub.publish(pos)
                rospy.loginfo(pos.data)
                rate.sleep()
       
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
