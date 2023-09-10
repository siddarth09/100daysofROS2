import rclpy 
from hundred_days_custom.srv import AreaOfSquare
from rclpy.node import Node 

class AreaServer(Node):
    def __init__(self):
        super().__init__("area_server")
        self.area=self.create_service(AreaOfSquare,"area",self.find_square)
        
    def find_square(self,request,response):
        response.area= pow(request.length,2)
        self.get_logger().info("RESPONSE WILL BE SENT FOR THE LENGTH {}".format(request.length))
        return response
    

def main():
    rclpy.init(args=None)
    server_call=AreaServer()
    rclpy.spin(server_call)
        
        
if __name__=="__main__":
    main()