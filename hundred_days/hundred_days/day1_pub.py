import rclpy 
from rclpy.node import Node 
from std_msgs.msg import String 
from time import sleep

class Pub(Node):
    
    def __init__(self):
        super().__init__("publisher")
        self.pub=self.create_publisher(String,"talker",10)

    def talker(self):
        
        while rclpy.ok():
            msg=String()
            msg.data="I AM BATMAN"
            self.pub.publish(msg)
            self.get_logger().info("PUBLISHING")
            sleep(2)
            
def main():
    rclpy.init(args=None)
    caller=Pub()
    caller.talker()
    
    
if __name__ == "__main__":
    main()