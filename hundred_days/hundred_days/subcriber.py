import rclpy as rc
from rclpy.node import Node
from std_msgs.msg import String

class Sub(Node):
    
    def __init__(self):
        super().__init__("Subcriber")
        self.subscribe=self.create_subscription(String,"talker",self.listener,10)
        
    def listener(self,msg):
        self.get_logger().warn("GOTHAM {}".format(msg.data))
        
    
def main():
    rc.init(args=None)
    subcriber=Sub()
    rc.spin(subcriber)
    
    subcriber.destroy_node()
    rc.shutdown()
    
    
if __name__=="__main__":
    main()
    
    