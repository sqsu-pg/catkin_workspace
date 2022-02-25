'''
Author: your name
Date: 2022-02-18 11:53:08
LastEditTime: 2022-02-18 14:42:56
LastEditors: Please set LastEditors
FilePath: /catkin_workspace/src/py_ros/listener_with_mask.py
'''
import sys
import rospy
from sensor_msgs.msg import Image


# sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
# sys.path.append('/home/george/anaconda3/envs/tensorflow_gpu/lib/python3.6/site-packages')

import cv2

from cv_bridge import CvBridge
from cv_bridge.boost.cv_bridge_boost import getCvType



# sys.path.append('/opt/ros/kinetic/lib/python2.7/dist-packages')
# sys.path.remove('/home/george/anaconda3/envs/tensorflow_gpu/lib/python3.6/site-packages')

import glob
import os

import numpy as np

from beginner_tutorials.msg import Img_vec

bridge = CvBridge()

cv2.namedWindow("Listener_Image")
cv2.namedWindow("Listener_Image_mask")


def callback(data):
    rospy.loginfo("I heard")
    
    time_pic = data.timestamp
    image_pic = bridge.imgmsg_to_cv2(data.image_left).copy()
    image_mask = bridge.imgmsg_to_cv2(data.image_mask).copy()

    print(type(image_pic))
    print (image_pic.shape)
    print (image_pic.dtype)
    print (type(image_mask))
    print (image_mask.shape)
    print (image_mask.dtype)

    cv2.imshow("Listener_Image", image_pic)
    cv2.waitKey(3)
    cv2.imshow("Listener_Image_mask", image_mask)
    cv2.waitKey(3)


def listener():
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber('pic_with_mask', Img_vec, callback, queue_size=1)

    rospy.spin()


if __name__ == '__main__':
    listener()
