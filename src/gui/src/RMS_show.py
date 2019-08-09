#!/usr/bin/env python
#encoding:utf-8  
'''RMS_show ROS Node'''

import rospy
import numpy as np
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QTimer, QCoreApplication, QDateTime
from RMS import Ui_RMS
from std_msgs.msg import Float32MultiArray
from CoordinateTransfer import millerToXY
#from PyQt5.QtGui import QPixmap
#import time

class RMS_show(QMainWindow,Ui_RMS):

    def __init__(self,parent=None):
        super(RMS_show,self).__init__(parent)
        self.setupUi(self)
        self.PrepWidgets()
        self.Timer=QTimer()
        self.CallBackFunctions()
 #ros节点定义，并创建订阅者与发布者
        rospy.init_node('RMS_UI', anonymous=True)
        rate = rospy.Rate(1)  # 10hz
        self.pathfollowing_pub = rospy.Publisher('/waypoints', Float32MultiArray, queue_size=10)
        self.positionkeeping_pub = rospy.Publisher('/set_point', Float32MultiArray, queue_size=10)
        rospy.Subscriber("/position_real", Float32MultiArray, self.Position_show)
        rate.sleep()

    def PrepWidgets(self):
        self.checkBox_1.setEnabled(True)
        self.checkBox_2.setEnabled(True)
        self.PushButton_start.setEnabled(False)
        self.PushButton_suspend.setEnabled(False)
        self.PushButton_save.setEnabled(False)
        self.PushButton_quit.setEnabled(False)
        self.PositionKeeping_Lat.setEnabled(False)
        self.PositionKeeping_Lon.setEnabled(False)
        self.Point1_Lat.setEnabled(False)
        self.Point1_Lon.setEnabled(False)
        self.Point2_Lat.setEnabled(False)
        self.Point2_Lon.setEnabled(False)
        self.Point3_Lat.setEnabled(False)
        self.Point3_Lon.setEnabled(False)
        self.Point4_Lat.setEnabled(False)
        self.Point4_Lon.setEnabled(False)
        self.Point5_Lat.setEnabled(False)
        self.Point5_Lon.setEnabled(False)

    
    def checkBox_1_fun(self):
        if self.checkBox_1.isChecked():
            self.PushButton_start.setEnabled(True)
            self.PositionKeeping_Lat.setEnabled(True)
            self.PositionKeeping_Lon.setEnabled(True)
            self.Point1_Lat.setEnabled(False)
            self.Point1_Lon.setEnabled(False)
            self.Point2_Lat.setEnabled(False)
            self.Point2_Lon.setEnabled(False)
            self.Point3_Lat.setEnabled(False)
            self.Point3_Lon.setEnabled(False)
            self.Point4_Lat.setEnabled(False)
            self.Point4_Lon.setEnabled(False)
            self.Point5_Lat.setEnabled(False)
            self.Point5_Lon.setEnabled(False)
        else:
            self.PositionKeeping_Lat.setEnabled(False)
            self.PositionKeeping_Lon.setEnabled(False)

    def checkBox_2_fun(self):
        if self.checkBox_2.isChecked():
            self.PushButton_start.setEnabled(True)
            self.PositionKeeping_Lat.setEnabled(False)
            self.PositionKeeping_Lon.setEnabled(False)
            self.Point1_Lat.setEnabled(True)
            self.Point1_Lon.setEnabled(True)
            self.Point2_Lat.setEnabled(True)
            self.Point2_Lon.setEnabled(True)
            self.Point3_Lat.setEnabled(True)
            self.Point3_Lon.setEnabled(True)
            self.Point4_Lat.setEnabled(True)
            self.Point4_Lon.setEnabled(True)
            self.Point5_Lat.setEnabled(True)
            self.Point5_Lon.setEnabled(True)
        else:
            self.Point1_Lat.setEnabled(False)
            self.Point1_Lon.setEnabled(False)
            self.Point2_Lat.setEnabled(False)
            self.Point2_Lon.setEnabled(False)
            self.Point3_Lat.setEnabled(False)
            self.Point3_Lon.setEnabled(False)
            self.Point4_Lat.setEnabled(False)
            self.Point4_Lon.setEnabled(False)
            self.Point5_Lat.setEnabled(False)
            self.Point5_Lon.setEnabled(False)

    def Start(self):
        self.PushButton_start.setEnabled(False)
        self.PushButton_suspend.setEnabled(True)
        self.PushButton_save.setEnabled(True)
        self.PushButton_quit.setEnabled(True)
        self.checkBox_1.setEnabled(False)
        self.checkBox_2.setEnabled(False)
        self.PositionKeeping_Lat.setEnabled(False)
        self.PositionKeeping_Lon.setEnabled(False)
        self.Point1_Lat.setEnabled(False)
        self.Point1_Lon.setEnabled(False)
        self.Point2_Lat.setEnabled(False)
        self.Point2_Lon.setEnabled(False)
        self.Point3_Lat.setEnabled(False)
        self.Point3_Lon.setEnabled(False)
        self.Point4_Lat.setEnabled(False)
        self.Point4_Lon.setEnabled(False)
        self.Point5_Lat.setEnabled(False)
        self.Point5_Lon.setEnabled(False)
        self.textEdit.setText('开始')

        if self.checkBox_1.isChecked():
            try:
                setpoint = millerToXY(self.PositionKeeping_Lon.text(),self.PositionKeeping_Lat.text())
                setpoint_1 = [-setpoint[1],setpoint[0]]
                setpoint_xy = Float32MultiArray(data=setpoint_1)
                self.positionkeeping_pub.publish(setpoint_xy)
                rospy.loginfo(setpoint_xy)
            except Exception:
                self.textEdit.setText("Fail to load set point")
        elif self.checkBox_2.isChecked():
            try:
                Point1_xy = millerToXY(self.Point1_Lon.value(),self.Point1_Lat.value())                
                Point2_xy = millerToXY(self.Point2_Lon.value(),self.Point2_Lat.value())
                Point3_xy = millerToXY(self.Point3_Lon.value(),self.Point3_Lat.value())
                Point4_xy = millerToXY(self.Point4_Lon.value(),self.Point4_Lat.value())
                Point5_xy = millerToXY(self.Point5_Lon.value(),self.Point5_Lat.value())
                waypoints_xy = np.array([[-Point1_xy[1],Point1_xy[0]],[-Point2_xy[1],Point2_xy[0]],[-Point3_xy[1],Point3_xy[0]],[-Point4_xy[1],Point4_xy[0]],[-Point5_xy[1],Point5_xy[0]]])
                self.pathfollowing_pub.publish(waypoints_xy)
                rospy.loginfo("pointsway is set as:: %f", waypoints_xy)
            except Exception:
                self.textEdit.setText("Fail to load waypoints")


    def Suspend(self):
        self.PushButton_start.setEnabled(True)
        self.PushButton_suspend.setEnabled(False)
        self.PushButton_save.setEnabled(True)
        self.PushButton_quit.setEnabled(True)
        self.checkBox_1.setEnabled(True)
        self.checkBox_2.setEnabled(True)


    def ExitApp(self):
        self.Timer.Stop()
        self.textEdit.setPlainText('Exiting the application..')
        QCoreApplication.quit()


    def Showtime(self):
        time = QDateTime.currentDateTime()
        timeDisplay = time.toString("yyyy-MM-dd hh:mm:ss dddd")
        self.Date.setText(timeDisplay)

    def Position_show(self, data):
        global Lat_real_get
        Lat_real_get = data.data[0]
        global Lon_real_get
        Lon_real_get = data.data[1]
        self.Lat_real.setText(Lat_real_get)
        self.Lon_real.setText(Lon_real_get)
   
    def CallBackFunctions(self):
        self.Timer.timeout.connect(self.Showtime)
        self.PushButton_start.clicked.connect(self.Start)
        self.PushButton_suspend.clicked.connect(self.Suspend)
        self.PushButton_quit.clicked.connect(self.ExitApp)
        self.checkBox_1.clicked.connect(self.checkBox_1_fun)
        self.checkBox_2.clicked.connect(self.checkBox_2_fun)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui=RMS_show()
    ui.show()
    sys.exit(app.exec_())