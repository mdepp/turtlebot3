import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    TURTLEBOT3_MODEL = os.environ["TURTLEBOT3_MODEL"]

    tb3_param_dir = LaunchConfiguration(
        "tb3_param_dir",
        default=os.path.join(
            get_package_share_directory("turtlebot3_bringup"),
            "param",
            TURTLEBOT3_MODEL + ".yaml",
        ),
    )

    return LaunchDescription(
        [
            Node(
                package="turtlebot3_node",
                executable="turtlebot3_ros",
                parameters=[tb3_param_dir],
                arguments=["-i", "/dev/ttyACM0"],
                output="screen",
            ),
            Node(
                package="cv_camera",
                executable="cv_camera_node",
                namespace="camera/depth",
                parameters=[{"device_id": 0, "device_path": "/dev/robot/camera/depth"}],
            ),
            Node(
                package="cv_camera",
                executable="cv_camera_node",
                namespace="camera/rgb",
                parameters=[{"device_id": 0, "device_path": "/dev/robot/camera/rgb"}],
            ),
        ]
    )
