import rclpy 
from rclpy.node import Node
from geometry_msgs.msg import Twist 
from turtlesim.msg import Pose

import time

class SpeedController(Node):
    LINEAR_X= 1.0
    ANGULAR_Z= 0.1
    
    def __init__(self):
        super().__init__("speed")
        self.pub=self.create_publisher(Twist,'/turtle1/cmd_vel',10)
        
        timer_period=1.5 
        self.initial_time=time.time()
        self.timer=self.create_timer(timer_period,self.speed)
        self.counter=0
        self.position_sub=self.create_subscription(Pose,'/turtle1/pose',self.pose_callback,10)
        
    def speed(self):
        msg=Twist()
        final_time=time.time()
        msg.linear.x=SpeedController.LINEAR_X 
        msg.angular.z=SpeedController.ANGULAR_Z
        
        total_time_spent=final_time-self.initial_time
        
        distance_travelled= total_time_spent * msg.linear.x 
        self.get_logger().info("TIME SPENT:{}".format(total_time_spent))
        self.get_logger().info("DISTANCE TRAVELLED:{}".format(distance_travelled))
        
        if (distance_travelled > 3.0):
            msg.linear.x=0.0
            
            msg.angular.z=0.3
            self.pub.publish(msg)
            self.get_logger().fatal("STOPPED")
            rclpy.shutdown()
            
        else: 
            self.get_logger().info("TURTLE MOVING at {} m/s".format(msg.linear.x)) 
            
        self.pub.publish(msg)
            
        self.counter+=1
        
    def pose_callback(self,msg):
        self.get_logger().info("TURTLE POSITION \n X:{0} \t Y:{1} \t Z:{2}".format(msg.x,msg.y,msg.theta))
        
        
def main():
    rclpy.init(args=None)
    Controller=SpeedController()
    rclpy.spin(Controller)
    
    
if __name__=="__main__":
    main()
        