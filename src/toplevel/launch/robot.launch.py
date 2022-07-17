import os

from ament_index_python import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():
    return LaunchDescription(
        [
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(
                    os.path.join(
                        get_package_share_directory("realsense2_camera"),
                        "launch/rs_launch.py",
                    )
                ),
                launch_arguments=[
                    ("device_name", "d455"),
                    # ("rgb_camera.profile", "1280x720x30"),
                    # ("depth_module.profile", "1280x720x30"),
                ],
            ),
        ]
    )
