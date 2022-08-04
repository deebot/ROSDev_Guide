#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/msg/string.hpp"
#include "geometry_msgs/msg/twist.hpp"
class TwistControlNode : public rclcpp::Node
{
public:
   TwistControlNode() : Node("robot_news_station")
    {
        publisher_ = this->create_publisher<geometry_msgs::msg::Twist>("turtle1/cmd_vel", 10);
        timer_ = this->create_wall_timer(std::chrono::milliseconds(50),
                                         std::bind(&TwistControlNode::publishNews, this));
        RCLCPP_INFO(this->get_logger(), "Sending Twist instructions.");
    }

private:
    void publishNews()
    {
        auto msg = geometry_msgs::msg::Twist();
        msg.linear.x = 0.5;
        msg.angular.z =0.5;
        publisher_->publish(msg);
    }


    rclcpp::Publisher<geometry_msgs::msg::Twist>::SharedPtr publisher_;
    rclcpp::TimerBase::SharedPtr timer_;
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<TwistControlNode>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}
