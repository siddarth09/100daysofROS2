import rclpy
from std_msgs.msg import String
from rclpy.node import Node 

class Sub(Node):
    
    def __init__(self):
        super().__init__('subscriber')
        self.subcribe=self.create_subscription(String,"talker",self.listener,10)
        
    def listener(self,msg):
        self.get_logger().warn("GOTHAM We have a news:{}".format(msg.data))
        
def main():
    rclpy.init()
    subs=Sub()
    rclpy.spin(subs)
    
if __name__ == "__main__":
    main()