.PHONY: build
build:
	colcon build \
		--cmake-args -DCMAKE_EXPORT_COMPILE_COMMANDS=ON \
		--allow-overriding turtlesim

.PHONY: clean
clean:
	rm -rf build/ install/ log/


OPENCR_PORT=/dev/ttyACM0
OPENCR_MODEL=burger


.PHONY: update-opencr-firmware
update-opencr-firmware:
	rm -rf opencr_update.tar.bz2
	rm -rf opencr_update
	wget https://github.com/ROBOTIS-GIT/OpenCR-Binaries/raw/master/turtlebot3/ROS2/latest/opencr_update.tar.bz2 
	tar -xvf opencr_update.tar.bz2 
	cd opencr_update && ./update.sh $(OPENCR_PORT) $(OPENCR_MODEL).opencr


.PHONY: update-subtrees
update-subtrees:
	git subtree pull --prefix src/ld08_driver \
		https://github.com/ROBOTIS-GIT/ld08_driver.git \
		ros2-devel \
		--squash
