import rclpy 
import math 
import copy 
from rclpy.node import Node 
from geometry_msgs.msg import Twist 
from turtlesim.msg import Pose 
import time 
from rcl_interfaces.msg import Log

class RobotPose():
    def __init__(self,x=0.0,y=0.0,theta=0.0):
        self.x=x
        self.y=y
        self.theta=theta
        
class Robotcleaner(Node):
    def __init__(self):
        super().__init__('robotcleaner')
        self.vel_pub=self.create_publisher(Twist,'/turtle1/cmd_vel',10)
        self.pose_sub=self.create_subscription(Pose,'/turtle1/pose',self.pose_callback,10)
        timer=0.5
        self.rosout_sub=self.create_subscription(Log,'/rosout',self.error_cb,10)
        self.pose=RobotPose()
        
    def error_cb(self,msg):
        if msg.level == 40:
            print("TURTLE HIT THE WALL")
       
        
    def pose_callback(self,msg):
        #position callback using a subcriber
        #TO UPDATE: POSITION OF THE TURTLE
        
        self.pose.x=msg.x
        self.pose.y=msg.y
        self.pose.theta=msg.theta 
        
    
    def move(self,speed,distance,is_forward):
        print("STARTING THE CLEANING")
        vel_msg=Twist()
        rclpy.spin_once(self)
        
        if (speed>1.0):
            self.get_logger().error("Speed cannot be more than 1m/s")
            return -1
        vel_msg.linear.x=abs(speed) if is_forward else -abs(speed)
        vel_msg.linear.x=abs(speed) * (1 if is_forward else -1)
        
       
        start_pose=copy.copy(self.pose)
       
        
        distance_to_goal=self.get_distance(start_pose,self.pose)
        
        while distance_to_goal<=distance:
            print("START POSE (x={}, y={}, theta={})\nUPDATED POSE (x={}, y={}, theta={})".format(
                                                                            start_pose.x, start_pose.y, start_pose.theta,
                                                                            self.pose.x, self.pose.y, self.pose.theta
                                                                        ))

            
            self.vel_pub.publish(vel_msg)
            #rclpy.spin_once(self)
            self.get_logger().info("DISTANCE = {}".format(distance_to_goal))
            
            time.sleep(0.05)
            #rclpy.spin_once(self)
            distance_to_goal=self.get_distance(start_pose,self.pose)
            rclpy.spin_once(self)
            
        vel_msg.linear.x=0.0
        self.vel_pub.publish(vel_msg)
        
        
        print("STOPPED")     
        
    def get_distance(self,start,destination):
        distance_achieved=math.sqrt((destination.x-start.x)**2)+((destination.y-start.y)**2)
        return distance_achieved
    
    
def main():
    rclpy.init(args=None)
    robot=Robotcleaner()
    robot.move(0.5,3,True)
    rclpy.spin(robot)
    
    
    robot.destroy_node()
    rclpy.shutdown()
    
if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    