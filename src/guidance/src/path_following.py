#!/usr/bin/env python
'''path_following ROS Node'''
import rospy
from std_msgs.msg import Float32MultiArray
from std_msgs.msg import Float64
from math import pi, acos
import numpy as np
from position_keeping import Position_keeping

class Path_following():

    def __init__(self):
          rospy.init_node('path_following', anonymous=True)
          rate = rospy.Rate(1) # 1hz
          self.pub = rospy.Publisher('/course_desired', Float32MultiArray, queue_size=10)
          rospy.Subscriber("/position_real", Float32MultiArray, self.Realposition)
          rospy.Subscriber("/waypoints", Float32MultiArray, self.Pointswayfun)
          rospy.Subscriber("/flag", Int8, self.Callback)
          self.radius = 10
          self.deta = 8
          rate.sleep()
       
    def Realposition(self,msg):
        rospy.loginfo("wave glider position:: %s", str(msg.data))
        pos = self.millerToXY(msg.data[0],msg.data[1])
        pos_1 = [-pos[1],pos[0]]
        self.realposition = pos_1
        
    def Pointswayfun(self,msg):
        self.pointsway = msg.data

    def Callback(self,msg):
        if msg.data == 2:
            self.course_desired=Position_keeping.p_s(self.set_position[0],self.set_position[1],self.realposition[0],self.realposition[1])
            self.pub.publish(self.course_desired)
            rospy.loginfo("wave glider desired course:: %f", self.course_desired)
        else:
            pass


    def p_f(self):
#该函数用来确认航迹段上的LOS点
#判断当前航迹段

        d=np.zeros((1, len(self.pointsway)))  
        for i in range(len(self.pointsway)):
            d[i]=np.norm(self.pointsway[i]-self.realposition)
        d=list(d)
        b,a = min(enumerate(d), key = operator.itemgetter(1)) #寻找最近轨迹点的位置
       
        if b==0:

            A=self.pointsway(b+1,1)-self.pointsway(b,1)
            B=self.pointsway(b,0)-self.pointsway(b+1,0)
            C=self.pointsway(b+1,0)*self.pointsway(b,1)-self.pointsway(b,0)*self.pointsway(b+1,1)
            #求垂足
            y0=(B*B*self.realposition[1]-A*B*self.realposition[0]-A*C)/(A*A+B*B)
            x0=(-A*B*self.realposition[1]+A*A*self.realposition[0]-B*C)/(A*A+B*B)
            yd=y0-np.sign(self.pointsway(b,0)-self.pointsway(b+1,0))*np.sqrt(np.square(self.deta)/np.square(1+(abs(self.pointsway(b,1)-self.pointsway(b+1,1))/\
            (self.pointsway(b,0)-self.pointsway(b+1,0)))))
            xd=x0-np.sign(self.pointsway(b,1)-self.pointsway(b+1,1))*(abs((self.pointsway(b,1)-self.pointsway(b+1,1))/(self.pointsway(b,0)-self.pointsway(b+1,0))))*\
            (y0-yd)

        elif b==len(self.pointsway)-1:

            A=self.pointsway(b,1)-self.pointsway(b-1,1)
            B=self.pointsway(b-1,0)-self.pointsway(b,0)
            C=self.pointsway(b,0)*self.pointsway(b-1,1)-self.pointsway(b-1,0)*self.pointsway(b,1)
            #求垂足
            y0=(B*B*self.realposition[1]-A*B*self.realposition[0]-A*C)/(A*A+B*B)
            x0=(-A*B*self.realposition[1]+A*A*self.realposition[0]-B*C)/(A*A+B*B)
            yd=y0-np.sign(self.pointsway(b-1,0)-self.pointsway(b,0))*np.sqrt(np.square(self.deta)/np.square(1+(abs(self.pointsway(b-1,1)-self.pointsway(b,1))/\
            (self.pointsway(b-1,0)-self.pointsway(b,0)))))
            xd=x0-np.sign(self.pointsway(b-1,1)-self.pointsway(b,1))*(abs((self.pointsway(b-1,1)-self.pointsway(b,1))/(self.pointsway(b-1,0)-self.pointsway(b,0))))*\
            (y0-yd)     

        else:

            PbPt = self.realposition-self.pointsway(b)
            PbPb_1 = self.pointsway(b-1)-self.pointsway(b)
            PbPb_1 = self.pointsway(b+1)-self.pointsway(b)

            if self.angle(PbPt, PbPb_1) < self.angle(PbPt, PbPb1):

                A=self.pointsway(b,1)-self.pointsway(b-1,1)
                B=self.pointsway(b-1,0)-self.pointsway(b,0)
                C=self.pointsway(b,0)*self.pointsway(b-1,1)-self.pointsway(b-1,0)*self.pointsway(b,1)
                #求垂足
                y0=(B*B*self.realposition[1]-A*B*self.realposition[0]-A*C)/(A*A+B*B)
                x0=(-A*B*self.realposition[1]+A*A*self.realposition[0]-B*C)/(A*A+B*B)
                yd=y0-np.sign(self.pointsway(b-1,0)-self.pointsway(b,0))*np.sqrt(np.square(self.deta)/np.square(1+(abs(self.pointsway(b-1,1)-self.pointsway(b,1))/\
                (self.pointsway(b-1,0)-self.pointsway(b,0)))))
                xd=x0-np.sign(self.pointsway(b-1,1)-self.pointsway(b,1))*(abs((self.pointsway(b-1,1)-self.pointsway(b,1))/(self.pointsway(b-1,0)-self.pointsway(b,0))))*\
                (y0-yd)   

            else:

                A=self.pointsway(b+1,1)-self.pointsway(b,1)
                B=self.pointsway(b,0)-self.pointsway(b+1,0)
                C=self.pointsway(b+1,0)*self.pointsway(b,1)-self.pointsway(b,0)*self.pointsway(b+1,1)
                #求垂足
                y0=(B*B*self.realposition[1]-A*B*self.realposition[0]-A*C)/(A*A+B*B)
                x0=(-A*B*self.realposition[1]+A*A*self.realposition[0]-B*C)/(A*A+B*B)
                yd=y0-np.sign(self.pointsway(b,0)-self.pointsway(b+1,0))*np.sqrt(np.square(self.deta)/np.square(1+(abs(self.pointsway(b,1)-self.pointsway(b+1,1))/\
                (self.pointsway(b,0)-self.pointsway(b+1,0)))))
                xd=x0-np.sign(self.pointsway(b,1)-self.pointsway(b+1,1))*(abs((self.pointsway(b,1)-self.pointsway(b+1,1))/(self.pointsway(b,0)-self.pointsway(b+1,0))))*\
                (y0-yd)                

        self.set_point = np.array([xd,yd]) 
        return (self.set_point)

    def angle(self,a,b):
        c = np.dot(a,b)
        d = np.dot(a,a)
        e = np.sqrt(d)
        f = np.dot(b,b)
        g = np.aqrt(f)
        h = c/(e*g)
        z = acos(h)
    return z

 

if __name__ == '__main__':
    try:
        Path_following()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass