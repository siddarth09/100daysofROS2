import rclpy 
from rclpy.node import Node 
from std_msgs.msg import String
from time import sleep

class first(Node):
    def __init__(self):
        super().__init__('first_publisher')
        #declare publisher
        self.pub=self.create_publisher(String,'talker',10)
        
        
    def scream(self):
       
        while rclpy.ok():
            msg=String()
            msg.data="Welcome back batman"
            self.pub.publish(msg)
            self.get_logger().info("PUBLISHING")
            sleep (0.5)
            
def main():
    rclpy.init(args=None)
    publisher=first()
    publisher.scream()
    
if __name__=="__main__":
    main()