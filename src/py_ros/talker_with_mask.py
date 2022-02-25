'''
Author: your name
Date: 2022-02-18 10:42:42
LastEditTime: 2022-02-18 17:53:20
LastEditors: Please set LastEditors
FilePath: /catkin_workspace/src/py_ros/talker_with_mask.py
'''
import rospy
from sensor_msgs.msg import Image

import sys
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
sys.path.append('/home/george/anaconda3/envs/tensorflow_gpu/lib/python3.6/site-packages')
import cv2
from cv_bridge import CvBridge
from cv_bridge.boost.cv_bridge_boost import getCvType

import glob
import os

import numpy as np


sys.path.append('/opt/ros/kinetic/lib/python2.7/dist-packages')

from beginner_tutorials.msg import Img_vec

def talker():
    pub = rospy.Publisher('pic_with_mask', Img_vec, queue_size=1)

    rospy.init_node('talker', anonymous=True)

    rate = rospy.Rate(1)

    bridge = CvBridge()

    # dtype_pic, n_channels_pic = bridge.encoding_to

    path = "/home/george/data_sets/03/image_0/"
    path_mask = "/home/george/data_sets/03/image_0_mask/"
    images = glob.glob(os.path.join(path, '*.png'))
    images_mask = glob.glob(os.path.join(path_mask, '*.txt'))

    images = sorted(images)
    # print (images)
    images_mask = sorted(images_mask)
    # print (images_mask)

    count = 0

    cv2.namedWindow("Image")
    cv2.namedWindow("Image_mask")

    while not rospy.is_shutdown():
        my_img_msg = Img_vec()
        my_img_msg.timestamp = rospy.get_rostime()
        image_pic = cv2.imread(images[count])
        my_img_msg.image_path = images[count]
        rospy.loginfo('[%s]', images[count])
        image_mask = np.loadtxt(images_mask[count])
        # image_mask = np.genfromtxt(images_mask[count])
        # image_mask = image_mask.astype(np.int32)
        my_img_msg.image_mask_path = images_mask[count]
        
        print (type(image_mask))
        print (image_mask.shape)
        print (image_mask.dtype)
        rospy.loginfo('[%s]', images_mask[count])

        cv2.imshow("Image", image_pic)
        cv2.waitKey(1)
        cv2.imshow("Image_mask", image_mask)
        cv2.waitKey(20)

        count += 1

        my_img_msg.image_left = bridge.cv2_to_imgmsg(image_pic)
        my_img_msg.image_mask = bridge.cv2_to_imgmsg(image_mask)
        
        rospy.loginfo("[%s]", my_img_msg.timestamp)

        pub.publish(my_img_msg)

        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInternalException:
        pass