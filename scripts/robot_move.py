#!/usr/bin/env python
# encoding: utf-8
from gazebo_msgs.srv import DeleteModel
from gazebo_msgs.msg import ModelState
import rospy
import os

def add_model(modelname,px,py):
    GAZEBO_MODEL_PATH = "~/robot_Fahad"
    os.system("rosrun gazebo_ros spawn_model -file " + GAZEBO_MODEL_PATH +"/model.sdf -sdf -model " +  "%s -x %d -y %d" %(modelname,px,py))

def pose_publish(modelname):
    pose_pub = rospy.Publisher('gazebo/set_model_state', ModelState, queue_size=1)
    pose_msg = ModelState()
    pose_msg.model_name = '%s'%modelname

    pose_msg.pose.position.x = -35
    pose_msg.pose.position.y = 8
    pose_msg.pose.position.z = 0

    # rospy.loginfo('update position: %d,%d'%(px,py))
    while not rospy.is_shutdown():
        #rospy.loginfo(pose_msg.pose.position.x,pose_msg.pose.position.y)
        if pose_msg.pose.position.x <= -28:
            pose_msg.pose.position.x +=0.04
            pose_msg.pose.position.y -=0.00572

        elif pose_msg.pose.position.x <=-19:
            pose_msg.pose.position.x +=0.02
            pose_msg.pose.position.y -= 0.04

        else:
            break

        pose_msg.pose.position.z = 0
        pose_pub.publish(pose_msg)
        rospy.sleep(0.04)


if __name__ == '__main__':
    rospy.init_node('main', anonymous=True)
    add_model('robot',-100,120)
    pose_publish('robot')