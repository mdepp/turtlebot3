from launch_ros.actions import Node

from launch import LaunchDescription


def generate_launch_description():
    return LaunchDescription(
        [
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
