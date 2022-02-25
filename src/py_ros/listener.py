'''
Author: your name
Date: 2022-02-18 12:30:07
LastEditTime: 2022-02-18 13:10:57
LastEditors: Please set LastEditors
FilePath: /catkin_workspace/src/py_ros/listener.py
'''
import rospy
from sensor_msgs.msg import Image

import sys
# sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
# sys.path.append('/home/george/anaconda3/envs/tensorflow_gpu/lib/python3.6/site-packages')
import cv2
from cv_bridge import CvBridge
from cv_bridge.boost.cv_bridge_boost import getCvType


# sys.path.append('/opt/ros/kinetic/lib/python2.7/dist-packages')

cv2.namedWindow("image window")

def callback(data):
    bridge = CvBridge()
    image = bridge.imgmsg_to_cv2(data, "bgr8")
    print (type(image))
    
    cv2.imshow("image window", image)
    cv2.waitKey(1)

def lis():
    rospy.init_node('lis', anonymous=True)
    
    rospy.Subscriber('hua_ti_name', Image, callback, queue_size=1)

    rospy.spin()

if __name__ == '__main__':
    lis()