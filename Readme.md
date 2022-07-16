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

  - Update the firmware

    ```bash
    make update-opencr-firmware
    ```
