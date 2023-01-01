import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node


def generate_launch_description():

    return LaunchDescription(
        [
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(
                    [
                        os.path.join(
                            get_package_share_directory("turtlebot3_bringup"), "launch"
                        ),
                        "/robot.launch.py",
                    ]
                ),
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
