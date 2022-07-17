.phony: all
all: build

# We install librealsense2 from source separately, so don't try to install
# the ROS version
SKIP_KEYS = librealsense2
# To make librealsense2 link properly, since it's installed using vcpkg
VCPKG_DIR ?= $$(HOME)/source/vcpkg

.phony: check-dependencies
check-dependencies:
	rosdep check --from-paths src --skip-keys=$(SKIP_KEYS)

.PHONY: build
build: check-dependencies
	colcon build \
		--cmake-args -DCMAKE_EXPORT_COMPILE_COMMANDS=ON \
		--cmake-args -DCMAKE_TOOLCHAIN_FILE=$(VCPKG_DIR)/scripts/buildsystems/vcpkg.cmake \
		--symlink-install

.PHONY: clean
clean:
	rm -rf build/ install/ log/

.PHONY: rosdep
rosdep:
	rosdep install --from-paths src -y --skip-keys=$(SKIP_KEYS)

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
