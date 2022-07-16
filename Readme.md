# Turtlebot3 setup

See the [ROBOTICS manual](https://emanual.robotis.com/docs/en/platform/turtlebot3/overview/).
This is from memory and may be missing steps.

  - Install ros galactic
  - Put the following in `~/.bashrc`

    ```bash
    source /opt/ros/galactic/setup.bash
    export TURTLEBOT3_MODEL=burger
    export LDS_MODEL=LDS-02
    ```

  - Copy the [turtlebot3 udev rules](https://github.com/ROBOTIS-GIT/turtlebot3/blob/galactic-devel/turtlebot3_bringup/99-turtlebot3-cdc.rules) to `/etc/udev/rules.d/`, as well as all rules in `udev/`. Then reload:

    ```bash
    sudo udevadm control --reload-rules
    sudo udevadm trigger
    ```

  - Update the firmware

    ```bash
    make update-opencr-firmware
    ```
