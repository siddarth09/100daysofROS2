import rclpy 
from rclpy.node import Node 
from turtlesim.msg import Color
from turtlesim.srv import SetPen
from geometry_msgs.msg import Twist
class Chamelon(Node):
    def __init__(self):
        super().__init__('chameleon')
        self.pub=self.create_publisher(Twist,'/turtle1/cmd_vel',10)
        self.client= self.create_client(SetPen,'turtle1/set_pen')
        while not self.client.wait_for_service(timeout_sec=0.1):
            self.get_logger().info('service not available, waiting again...')
        self.request=SetPen.Request()
                
            
    def change_color(self,r,b,g):
       self.request.r = r
       self.request.b = b
       self.request.g = g
       self.request.width=10
       self.future = self.client.call_async(self.request)
       rclpy.spin_until_future_complete(self, self.future)
       return self.future.result()
   
    def velocity_controller(self):
        i=0
        msg=Twist()
        while rclpy.ok():
            for i in range(100):
                if i%2 == 0 or i/3 == 0:
                    
                    msg.linear.x=0.0
                    msg.angular.z=0.5
                    i+=1
                    self.change_color(255,0,0)
                    self.get_logger().warn("Going right")
                else:
                    msg.linear.x=0.5
                    self.change_color(255,255,255)
                    self.get_logger().warn("Going straight and is white")
                    i+=1
                
            self.pub.publish(msg)
            self.get_logger().info("Turtle is moving")
                
        
        
   
            
def main():
    rclpy.init(args=None)
    color_changer=Chamelon()
    color_changer.velocity_controller()
   
    
    
if __name__=="__main__":
    main()