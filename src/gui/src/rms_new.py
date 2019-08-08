#!/usr/bin/env python
#encoding:utf-8  
'''test ROS Node'''
# license removed for brevity
import rospy
import numpy as np
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QTimer, QCoreApplication, QDateTime
from RMS import Ui_RMS
from std_msgs.msg import Float32MultiArray
from CoordinateTransfer import millerToXY
from std_msgs.msg import String



class RMS_show(QMainWindow,Ui_RMS):

    def __init__(self,parent=None):
        super(RMS_show,self).__init__(parent)
        self.setupUi(self)
        self.PrepWidgets()
        #self.Timer=QTimer()
        self.CallBackFunctions()
 

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

        rospy.init_node('RMS_UI', anonymous=True)
        rate = rospy.Rate(1)  # 1hz
        if self.checkBox_1.isChecked():
        #ros节点定义，并创建订阅者与发布者
            self.positionkeeping_pub = rospy.Publisher('/set_point', Float32MultiArray, queue_size=10)
            #rospy.Subscriber("/position_real", Float32MultiArray, self.Position_show)
            #rate.sleep()
            while not rospy.is_shutdown():
                setpoint = millerToXY(float(self.PositionKeeping_Lon.text()),float(self.PositionKeeping_Lat.text()))
                setpoint_1 = np.array([-setpoint[1],setpoint[0]])
                setpoint_xy = Float32MultiArray(data=setpoint_1)
                rospy.loginfo(setpoint_xy.data)
                self.positionkeeping_pub.publish(setpoint_xy)
                rate.sleep()

        elif self.checkBox_2.isChecked():
            self.pathfollowing_pub = rospy.Publisher('/waypoints', Float32MultiArray, queue_size=10)
            while not rospy.is_shutdown():
                Point1_xy = millerToXY(float(self.Point1_Lon.text()),float(self.Point1_Lat.text()))               
                Point2_xy = millerToXY(float(self.Point2_Lon.text()),float(self.Point2_Lat.text()))
                Point3_xy = millerToXY(float(self.Point3_Lon.text()),float(self.Point3_Lat.text()))
                Point4_xy = millerToXY(float(self.Point4_Lon.text()),float(self.Point4_Lat.text()))
                Point5_xy = millerToXY(float(self.Point5_Lon.text()),float(self.Point5_Lat.text()))
                waypoints_1 = np.array([[-Point1_xy[1],Point1_xy[0]],[-Point2_xy[1],Point2_xy[0]],[-Point3_xy[1],Point3_xy[0]],[-Point4_xy[1],Point4_xy[0]],[-Point5_xy[1],Point5_xy[0]]])
                waypoints_xy = Float32MultiArray(data=waypoints_1)
                self.pathfollowing_pub.publish(waypoints_xy)
                rospy.loginfo(waypoints_xy.data)
                rate.sleep()

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


    def CallBackFunctions(self):
        #self.Timer.timeout.connect(self.Showtime)
        self.PushButton_start.clicked.connect(self.Start)
        self.PushButton_suspend.clicked.connect(self.Suspend)
        self.PushButton_quit.clicked.connect(self.ExitApp)
        self.checkBox_1.clicked.connect(self.checkBox_1_fun)
        self.checkBox_2.clicked.connect(self.checkBox_2_fun)

if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)
        ui=RMS_show()
        ui.show()
        sys.exit(app.exec_())
    except rospy.ROSInterruptException:
        pass
