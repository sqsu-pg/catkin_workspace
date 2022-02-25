'''
Author: your name
Date: 2021-12-08 15:47:32
LastEditTime: 2022-01-29 10:24:15
LastEditors: Please set LastEditors

FilePath: /catkin_workspace/src/py_ros/talker.py
'''



import rospy
from sensor_msgs.msg import Image

import sys
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
sys.path.append('/home/george/anaconda3/envs/tensorflow_gpu/lib/python3.6/site-packages')
import cv2
from cv_bridge import CvBridge
from cv_bridge.boost.cv_bridge_boost import getCvType


sys.path.append('/opt/ros/kinetic/lib/python2.7/dist-packages')

def talker():
    print('1')
    pub = rospy.Publisher('hua_ti_name', Image, queue_size=1)
    print('1')
    rospy.init_node('talker', anonymous=True)
    print('1')

    rate = rospy.Rate(30)
    print('1')
    bridge = CvBridge()
    print('1')
    Video = cv2.VideoCapture(0)

    while not rospy.is_shutdown():
        ret, img = Video.read()
        cv2.imshow('talker', img)
        cv2.waitKey(3)
        pub.publish(bridge.cv2_to_imgmsg(img, "bgr8"))
        rate.sleep()


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
    # print('1')
    # talker()